#!/usr/bin/env python3
"""
Reformat _DATABASE class variable in vendor Python files to a pretty-printed
format with every key-value pair on its own line, using double quotes.

Usage:
    python scripts/format_database.py path/to/vendor_file.py [path/to/another.py ...]
    python scripts/format_database.py --all  # find all vendor files automatically
"""

import ast
import glob
import os
import sys
from typing import Any


def pretty_print_value(value: Any, indent: int = 0) -> str:
    """Pretty-print a Python literal value with consistent indentation."""
    tab = "    "
    ind = tab * indent
    ind_inner = tab * (indent + 1)

    if isinstance(value, dict):
        if not value:
            return "{}"
        items = []
        for k, v in value.items():
            k_repr = pretty_print_value(k, indent + 1)
            v_str = pretty_print_value(v, indent + 1)
            items.append(f"{ind_inner}{k_repr}: {v_str},")
        return "{\n" + "\n".join(items) + f"\n{ind}}}"

    elif isinstance(value, list):
        if not value:
            return "[]"
        items = []
        for item in value:
            items.append(pretty_print_value(item, indent + 1))
        if all(len(item) <= 80 for item in items):
            inner = ", ".join(items)
            if len(inner) + len(ind) + 2 < 100:
                return f"[{inner}]"
        return "[\n" + ",\n".join(f"{ind_inner}{item}" for item in items) + f"\n{ind}]"

    elif isinstance(value, tuple):
        items = [pretty_print_value(item, indent) for item in value]
        inner = ", ".join(items)
        if len(items) == 1:
            inner += ","
        return f"({inner})"

    elif isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'

    elif isinstance(value, bool):
        return "True" if value else "False"

    elif value is None:
        return "None"

    else:
        return repr(value)


def find_database_nodes(tree: ast.AST) -> list[ast.Assign]:
    """Find all _DATABASE = ... assignment nodes in the AST."""
    nodes = []

    class Finder(ast.NodeVisitor):
        def visit_Assign(self, node):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "_DATABASE":
                    nodes.append(node)
                    return  # don't recurse into the value
            self.generic_visit(node)

    Finder().visit(tree)
    return nodes


def format_database_source(filepath: str) -> tuple[bool, str]:
    """Reformat all _DATABASE assignments in a Python file.

    Returns (changed, new_source).
    """
    with open(filepath) as f:
        source = f.read()

    tree = ast.parse(source)
    nodes = find_database_nodes(tree)

    if not nodes:
        return False, source

    lines = source.splitlines(keepends=True)
    modified = False

    # Process nodes in reverse order so line offsets stay valid
    for node in reversed(nodes):
        try:
            db_value = ast.literal_eval(node.value)
        except ValueError as e:
            print(
                f"  Warning: could not evaluate _DATABASE literal: {e}",
                file=sys.stderr,
            )
            continue

        pretty = pretty_print_value(db_value, indent=1)
        replacement = f"    _DATABASE = {pretty}"

        start_line = node.lineno - 1  # 0-indexed
        end_line = node.end_lineno  # exclusive
        original_block = "".join(lines[start_line:end_line])

        if original_block.strip() == replacement.strip():
            continue  # already matches

        before = "".join(lines[:start_line])
        after = "".join(lines[end_line:])
        lines = [before + replacement + "\n" + after]
        modified = True

    result = "".join(lines)

    # Strip trailing whitespace from each line
    result_lines = result.splitlines(keepends=True)
    result_lines = [line.rstrip() + "\n" for line in result_lines]
    result = "".join(result_lines).rstrip() + "\n"

    return modified, result


def find_all_vendor_files() -> list[str]:
    """Discover all vendor .py files under apts/opticalequipment/."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    pattern = os.path.join(
        project_root, "apts", "opticalequipment", "**", "vendors", "*.py"
    )
    return sorted(glob.glob(pattern, recursive=True))


def main():
    files = []
    if "--all" in sys.argv:
        files = find_all_vendor_files()
    else:
        files = [f for f in sys.argv[1:] if not f.startswith("--")]

    if not files:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    for filepath in files:
        short = os.path.relpath(filepath, os.getcwd())
        try:
            changed, result = format_database_source(filepath)
        except SyntaxError as e:
            print(f"{short}: Syntax error, skipping: {e}")
            continue

        if not changed:
            print(f"{short}: No _DATABASE found or already formatted.")
        else:
            with open(filepath, "w") as f:
                f.write(result)
            print(f"{short}: Reformatted.")


if __name__ == "__main__":
    main()
