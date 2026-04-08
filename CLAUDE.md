# 仓库说明

本仓库用于存放 [项目领域] 的 Cookiecutter 模板。
模板基于 cookiecutter 框架构建，通过 `{{ cookiecutter.变量名 }}` 语法实现项目脚手架生成。

## 模板架构
- **核心模板目录**: `{{ cookiecutter.project_slug }}/` 包含生成项目的骨架文件
- **配置定义**: `cookiecutter.json` 定义了用户在生成项目时需填写的全部变量
- **钩子脚本**: `hooks/` 目录下的 `pre_gen_project.py` 和 `post_gen_project.py` 用于执行生成前后的校验与处理

## 变量命名约定
模板内使用以下核心变量（定义在 cookiecutter.json 中）：
- `project_name`: 用户输入的项目名称（可含空格、大小写）
- `project_slug`: 自动格式化后的项目目录名（小写、下划线分隔，Python/模块友好）
- `author_name`: 作者姓名
- `author_email`: 作者邮箱
- `python_version`: 目标 Python 版本（默认 "3.11"）
- `use_docker`: 是否包含 Docker 配置（布尔值，默认 true）
- `license`: 许可证类型（MIT/Apache-2.0/Proprietary）

## 模板逻辑处理规则

### 条件生成
- 文件或目录名包含 `{% if cookiecutter.use_docker == 'yes' %}` 条件时，仅在对应选项启用时才被包含。
- `hooks/post_gen_project.py` 中会根据 `use_docker` 等布尔变量删除不需要的文件。

### 变量过滤
- 在 `cookiecutter.json` 中定义 `_copy_without_render` 列表，避免二进制文件或包含 Jinja2 语法的文件被二次渲染。

### 钩子脚本职责
- `hooks/pre_gen_project.py`: 校验 `project_slug` 是否符合命名规范（例如是否为有效的 Python 模块名）。
- `hooks/post_gen_project.py`: 清理未选用的可选文件，初始化 Git 仓库（若 `init_git` 为 yes）。

## 开发注意事项

- 修改 `{{ cookiecutter.project_slug }}/` 内任何文件时，注意区分**静态内容**和 **Jinja2 模板变量**。静态内容直接编辑，动态部分需通过 `cookiecutter.json` 控制。
- 新增可选功能时，需同时更新：
    1. `cookiecutter.json` 中添加对应的布尔/选项变量。
    2. 在模板文件中使用 `{% if cookiecutter.新变量 == 'yes' %}` 条件包裹相关内容。
    3. 在 `hooks/post_gen_project.py` 中处理未选中时的文件清理。
- 测试模板变更：
    1. 在仓库根目录执行 `cookiecutter . --no-input` 进行快速生成测试。
    2. 使用 `cookiecutter .` 进入交互式测试，验证默认值与提示文本。

## 常用命令

```bash
# 本地测试模板生成（使用默认值，跳过交互）
cookiecutter . --no-input

# 测试模板并指定输出目录
cookiecutter . -o /tmp/test-output

# 查看模板变量帮助
cookiecutter . --help