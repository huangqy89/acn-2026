# Advanced Computer Networks · Fall 2026

中山大学研究生《高级计算机网络》课程网站。教师：Qianyi Huang。

沿用 [cn-2026](https://github.com/huangqy89/cn-2026) 的 Jekyll 模板、蓝色页眉、橙色分隔线、字体和学校标志，保留原模板 MIT 许可证。

## 页面

- **Home**：研究生课程介绍及教师信息。
- **Lectures**：按 `order` 排序，每次课同时显示课件链接和有序论文列表。
- **Reading List**：按主题列出论文；与 Lectures 共用 `_data/papers.yml`。
- **Materials**：补充学习资料。

没有助教、Assignments 或 Laboratories 页面。未提供的课件、论文和上课日期保持待发布状态；当前 Introduction 仅作为可编辑的第一讲条目。课程介绍和阅读主题是初始草稿，可自行修改。

## 首次发布到 GitHub

建议仓库名：`huangqy89/acn-2026`。以下目标地址仅在创建仓库、启用 Pages 并成功部署后生效：

`https://huangqy89.github.io/acn-2026/`

1. 在 GitHub 新建名为 **acn-2026** 的公开仓库。
2. 将本目录中的全部源文件上传并提交到 `main` 分支。注意包含 `.github/workflows/jekyll.yml`；不要上传外层压缩包，也不要把整个 `acn-2026` 文件夹再套一层。
3. 在 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
4. 在 **Actions → Build and deploy course website** 运行工作流，或提交一次更新触发构建。
5. 等待工作流完成，再打开上面的课程网址。

若使用其他仓库名，请同步修改 `_config.yml` 中的 `baseurl` 和 `repository`。目前没有在 GitHub 上创建或启用这个仓库。

也可以在本地使用 Git 上传（在本项目目录执行）：

```bash
git init -b main
git add .
git commit -m "Create Advanced Computer Networks course website"
git remote add origin https://github.com/huangqy89/acn-2026.git
git push -u origin main
```

## 添加每次课的 PPT 和论文

### 1. 上传课件

将 PPT/PDF 放入 `static_files/lectures/`。建议采用不含空格的英文文件名。

### 2. 登记论文

编辑 `_data/papers.yml`。首次添加时删除文件末尾的空数组 `[]`，改为下面的列表。
以下只是字段示例，请替换为真实信息；不要直接发布示例题目。

```yaml
- id: paper-unique-id
  title: "Paper title"
  authors: "Author A, Author B"
  venue: "SIGCOMM"
  year: 2026
  topic: "Networking for AI"
  url: "https://example.org/paper.pdf"
  slides: "/static_files/papers/presentation.pdf"
  note: "Optional discussion focus"
```

`id` 必须唯一，`topic` 必须与 `_data/reading_topics.yml` 中的一项完全相同。
`authors`、`venue`、`year`、`url`、`slides` 和 `note` 均可省略。
论文和 slides 支持外部链接，也支持仓库内以 `/static_files/` 开头的路径；不要手动添加 `/acn-2026` 前缀。
同一论文只登记一次，可以被多次课引用。

### 3. 新增或修改 Lecture

复制 `_lectures/01_introduction.md`，例如命名为 `_lectures/02_networking_for_ai.md`：

```yaml
---
type: lecture
order: 2
title: "Lecture 2: Networking for AI"
tldr: "A brief description of this lecture."
# 确认时间后再填写，省略时不显示日期。
# class_date: 2026-09-14
links:
  - name: PPT
    url: /static_files/lectures/lecture-02.pptx
  - name: PDF
    url: /static_files/lectures/lecture-02.pdf
paper_ids:
  - paper-unique-id
---

Optional lecture notes in Markdown.
```

`order` 决定课次顺序，`paper_ids` 的顺序决定这次课中论文列表的显示顺序。
同一节课可添加多份课件及任意数量的论文。没有资料时保留 `links: []` 和 `paper_ids: []`，页面不会生成无效下载链接。

## 修改其他内容

| 内容 | 文件 |
| --- | --- |
| 课程名称、学期、简介、网址 | `_config.yml` |
| 教师姓名、照片、主页 | `_data/people.yml` |
| 导航 | `_data/nav.yml` |
| 阅读主题及顺序 | `_data/reading_topics.yml` |
| 论文元信息 | `_data/papers.yml` |
| 每次课的资料 | `_lectures/*.md` |
| 补充资料 | `materials.md` |
| 继承的配色 | `_sass/_user_vars.scss` |
| 新增页面样式 | `_sass/_graduate.scss` |

## 本地构建

GitHub Pages 使用标准 Jekyll 构建。安装 Ruby 和 Bundler 后：

```bash
bundle install
bundle exec jekyll serve
```

没有 Ruby 时，可用附带的 Python 辅助程序生成当前模板的静态预览。它复用同一套 Liquid/SCSS 文件，仅支持本课程模板涉及的语法，不替代完整 Jekyll：

```bash
pip install -r requirements-build.txt
python scripts/build_preview.py --baseurl "" --output dist
```

修改后重新构建即可。上传到 GitHub 的源码不需要 `dist/` 预览产物。

## 来源

- 本科课程仓库：https://github.com/huangqy89/cn-2026
- 原模板许可证：见 `LICENSE`（保留原版权声明）。
