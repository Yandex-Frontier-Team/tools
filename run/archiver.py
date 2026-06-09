from tools.archive_utils import archive_selected, resolve_selected_dirs


root = "/Users/dark-creator/solomon/yandex/packages/dialog-quality"


archive_path = archive_selected(root, [
    "analysis",
    # "resources/sample",
    "src",
    "run",
    "tests",
    ".gitignore",
    "pyproject.toml",
    "README.md",
])

print(archive_path)