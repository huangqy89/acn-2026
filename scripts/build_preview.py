"""Render this course's Jekyll templates for a portable static preview.

GitHub Pages uses Jekyll via .github/workflows/jekyll.yml. This helper renders
the shared Liquid templates when Ruby is unavailable; it is not a general
replacement for Jekyll. Run from the repository root.
"""
import argparse
import re
import shutil
from pathlib import Path
import markdown
import sass
import yaml
from liquid import Environment, DictLoader


def frontmatter(path):
    text = path.read_text()
    if text.startswith('---\n'):
        _, header, body = text.split('---', 2)
        return yaml.safe_load(header) or {}, body.lstrip('\n')
    return {}, text


def slugify(value):
    return re.sub(r'[^\w-]+', '-', str(value).lower()).strip('-')


def convert_includes(text):
    # Map Jekyll's include parameters to Liquid include parameters.
    text = re.sub(r'include\.(\w+)', r'include_\1', text)
    def replace(match):
        filename, args = match.groups()
        pairs = re.findall(r'(\w+)=(\S+)', args)
        suffix = ''.join(f', include_{key}: {value}' for key, value in pairs)
        return "{% include '" + filename + "'" + suffix + ' %}'
    return re.sub(r'{%\s*include\s+([\w.\-/]+)(.*?)%}', replace, text)


def build(root, output, baseurl=None, origin=None):
    site = yaml.safe_load((root/'_config.yml').read_text())
    if baseurl is not None:
        site['baseurl'] = baseurl.rstrip('/')
    if origin is not None:
        site['url'] = origin.rstrip('/')
    site['data'] = {p.stem: yaml.safe_load(p.read_text()) for p in (root/'_data').glob('*.yml')}
    site['announcements'] = []
    includes = {p.name: convert_includes(p.read_text()) for p in (root/'_includes').glob('*.html')}
    env = Environment(loader=DictLoader(includes), globals={'site': site})
    env.add_filter('relative_url', lambda url: site['baseurl'] + '/' + str(url).lstrip('/'))
    env.add_filter('slugify', slugify)
    def render(text, **context):
        return env.from_string(convert_includes(text)).render(**context)
    def layout(name, content, page):
        if not name:
            return content
        metadata, template = frontmatter(root/'_layouts'/f'{name}.html')
        html = render(template, page=page, content=content)
        return layout(metadata.get('layout'), html, page)
    lectures = []
    for path in sorted((root/'_lectures').glob('*.md')):
        data, body = frontmatter(path)
        data.update(slug=path.stem, url=f'/lectures/{path.stem}/')
        data['content'] = markdown.markdown(render(body, page=data), extensions=['tables', 'fenced_code'])
        lectures.append(data)
    site['lectures'] = lectures
    for path in sorted((root/'_announcements').glob('*.md')):
        data, body = frontmatter(path)
        data['content'] = markdown.markdown(body)
        site['announcements'].append(data)
    validate_content(site)
    output.mkdir(parents=True, exist_ok=True)
    for page_path in [root/'index.md', root/'lectures.md', root/'reading-list.md', root/'materials.md']:
        page, body = frontmatter(page_path)
        page['url'] = page.get('permalink', '/')
        html = markdown.markdown(render(body, page=page), extensions=['tables', 'fenced_code'])
        dest = output/page['url'].lstrip('/')/'index.html'
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(layout(page['layout'], html, page))
    for lecture in lectures:
        dest = output/lecture['url'].lstrip('/')/'index.html'
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(layout('lecture', lecture['content'], lecture))
    _, scss = frontmatter(root/'_css/main.scss')
    (output/'_css').mkdir(exist_ok=True)
    (output/'_css/main.css').write_text(sass.compile(string=scss, include_paths=[str(root/'_sass')], output_style='expanded'))
    for name in ['_images', 'static_files']:
        shutil.copytree(root/name, output/name, dirs_exist_ok=True)
    (output/'.nojekyll').touch()
    print(f'Built {4 + len(lectures)} pages in {output}')


def validate_content(site):
    papers = site['data']['papers'] or []
    topics = site['data']['reading_topics']
    ids = [p['id'] for p in papers]
    if len(ids) != len(set(ids)):
        raise ValueError('Paper IDs must be unique')
    for paper in papers:
        if not paper.get('title') or paper.get('topic') not in topics:
            raise ValueError(f'Paper needs a title and an existing topic: {paper}')
    orders = [lecture['order'] for lecture in site['lectures']]
    if len(orders) != len(set(orders)):
        raise ValueError('Lecture order values must be unique')
    for lecture in site['lectures']:
        for paper_id in lecture.get('paper_ids', []):
            if paper_id not in ids:
                raise ValueError(f'{lecture["slug"]}: unknown paper ID {paper_id}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path.cwd())
    parser.add_argument('--output', type=Path, default=Path('dist'))
    parser.add_argument('--baseurl', default=None)
    parser.add_argument('--url', default=None)
    args = parser.parse_args()
    build(args.source.resolve(), args.output.resolve(), args.baseurl, args.url)
