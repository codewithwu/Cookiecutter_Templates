# Cookiecutter_Templates

Cookiecutter 项目模板集，基于 cookiecutter 框架构建。

## 模板列表

- `{{ cookiecutter.project_slug }}/` - Python 项目基础模板

## 使用方式

### 本地使用

```bash
# 使用默认配置生成项目
cookiecutter <path-to-template> --no-input

# 交互式生成（可自定义变量值）
cookiecutter <path-to-template>

# 指定输出目录
cookiecutter <path-to-template> -o <output-directory>

# 跳过交互，指定参数
cookiecutter <path-to-template> --no-input \
    project_slug=mypackage \
    description="My awesome package" \
    python_version=3.12
```

### 远程使用（通过 GitHub）

```bash
cookiecutter gh:<github-username>/Cookiecutter_Templates
```

## 模板变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `project_slug` | 项目目录名（小写、下划线分隔） | myproject |
| `description` | 项目描述 | A Python project |
| `python_version` | 目标 Python 版本 | 3.13 |
