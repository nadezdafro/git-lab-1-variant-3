"""Генерация описания функций из docstring модуля app.py."""
import ast
from pathlib import Path

root = Path(__file__).resolve().parent.parent
module = ast.parse((root / "app.py").read_text(encoding="utf-8"))
version = (root / "VERSION").read_text(encoding="utf-8").strip()
lines = ["# Документация учебного проекта", "", f"Версия: {version}", ""]
for item in module.body:
    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
        lines.extend([
            f"## {item.name}", "",
            ast.get_docstring(item) or "Описание отсутствует.", ""
        ])
output_dir = root / "generated_docs"
output_dir.mkdir(exist_ok=True)
(output_dir / "API.md").write_text("\n".join(lines), encoding="utf-8")
print("Документация сформирована: generated_docs/API.md")
