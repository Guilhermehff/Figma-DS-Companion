from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .core import ROOT, validate_active_docs, validate_repo, write_registry


def _resolve_root(value: str | None) -> Path:
    return ROOT if value is None else Path(value).resolve()


def cmd_validate(root: Path) -> int:
    errors = validate_repo(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("governance validation passed")
    return 0


def cmd_build_registry(root: Path) -> int:
    output_path = write_registry(root)
    print(output_path.relative_to(root))
    return 0


def cmd_check_docs(root: Path) -> int:
    errors = validate_active_docs(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("active docs are in sync")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m scripts.figma_governance")
    parser.add_argument("--root", help="Repository root override")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("build-registry")
    subparsers.add_parser("check-docs")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = _resolve_root(args.root)
    if args.command == "validate":
        return cmd_validate(root)
    if args.command == "build-registry":
        return cmd_build_registry(root)
    if args.command == "check-docs":
        return cmd_check_docs(root)
    parser.error(f"Unknown command: {args.command}")
    return 2
