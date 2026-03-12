from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .core import (
    MCP_PORT_END,
    MCP_PORT_START,
    ROOT,
    GovernanceError,
    reset_mcp_listeners,
    validate_active_docs,
    validate_export_inputs,
    validate_repo,
    write_registry,
)


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


def cmd_build_registry(root: Path, *, base_only: bool = False) -> int:
    try:
        output_path = write_registry(root, base_only=base_only)
    except GovernanceError as exc:
        for error in str(exc).splitlines():
            print(error, file=sys.stderr)
        return 1
    print(output_path.relative_to(root))
    return 0


def cmd_validate_exports(root: Path, *, base_only: bool = False) -> int:
    errors = validate_export_inputs(root, base_only=base_only)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("export inputs are ready")
    return 0


def cmd_check_docs(root: Path) -> int:
    errors = validate_active_docs(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("active docs are in sync")
    return 0


def cmd_reset_mcp(
    *,
    port_start: int = MCP_PORT_START,
    port_end: int = MCP_PORT_END,
    keep_ports: list[int] | None = None,
    dry_run: bool = False,
) -> int:
    try:
        result = reset_mcp_listeners(
            port_start=port_start,
            port_end=port_end,
            keep_ports=set() if keep_ports is None else set(keep_ports),
            dry_run=dry_run,
        )
    except GovernanceError as exc:
        for error in str(exc).splitlines():
            print(error, file=sys.stderr)
        return 1

    if not result.listeners:
        print(f"no MCP listeners found in ports {port_start}-{port_end}")
        return 0

    verb = "would terminate" if dry_run else "terminated"
    for listener in result.terminated:
        print(f"{verb} pid={listener.pid} port={listener.port} command={listener.command}")

    for listener in result.preserved:
        print(f"preserved pid={listener.pid} port={listener.port} command={listener.command}")

    if not result.terminated:
        print(f"nothing to reset in ports {port_start}-{port_end}")

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python3 -m scripts.figma_governance")
    parser.add_argument("--root", help="Repository root override")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    build_registry_parser = subparsers.add_parser("build-registry")
    build_registry_parser.add_argument(
        "--base-only",
        action="store_true",
        help="Build a compatibility export from only the dated snapshots listed in figma/exports/index.yml",
    )
    validate_exports_parser = subparsers.add_parser("validate-exports")
    validate_exports_parser.add_argument(
        "--base-only",
        action="store_true",
        help="Validate only collection snapshot export inputs and skip extension snapshot requirements",
    )
    subparsers.add_parser("check-docs")
    reset_mcp_parser = subparsers.add_parser("reset-mcp")
    reset_mcp_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which node-based MCP listeners would be terminated without sending SIGTERM",
    )
    reset_mcp_parser.add_argument(
        "--keep-port",
        action="append",
        default=[],
        type=int,
        help="Preserve a specific MCP listener port instead of terminating it",
    )
    reset_mcp_parser.add_argument(
        "--port-start",
        default=MCP_PORT_START,
        type=int,
        help="First reserved MCP port to inspect",
    )
    reset_mcp_parser.add_argument(
        "--port-end",
        default=MCP_PORT_END,
        type=int,
        help="Last reserved MCP port to inspect",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = _resolve_root(args.root)
    if args.command == "validate":
        return cmd_validate(root)
    if args.command == "build-registry":
        return cmd_build_registry(root, base_only=args.base_only)
    if args.command == "validate-exports":
        return cmd_validate_exports(root, base_only=args.base_only)
    if args.command == "check-docs":
        return cmd_check_docs(root)
    if args.command == "reset-mcp":
        return cmd_reset_mcp(
            port_start=args.port_start,
            port_end=args.port_end,
            keep_ports=args.keep_port,
            dry_run=args.dry_run,
        )
    parser.error(f"Unknown command: {args.command}")
    return 2
