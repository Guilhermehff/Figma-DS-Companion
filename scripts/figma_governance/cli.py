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
    sync_brand_font_inventory,
    validate_repo,
)


def _resolve_root(value: str | None) -> Path:
    return ROOT if value is None else Path(value).resolve()


def cmd_validate(root: Path) -> int:
    try:
        sync_brand_font_inventory(root)
    except GovernanceError as exc:
        for error in str(exc).splitlines():
            print(error, file=sys.stderr)
        return 1

    errors = validate_repo(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("governance validation passed")
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


def cmd_sync_brand_fonts(root: Path) -> int:
    try:
        paths = sync_brand_font_inventory(root)
    except GovernanceError as exc:
        for error in str(exc).splitlines():
            print(error, file=sys.stderr)
        return 1
    for path in paths:
        print(f"synced {path.relative_to(root)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python3 -m scripts.figma_governance")
    parser.add_argument("--root", help="Repository root override")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("sync-brand-fonts")
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
    if args.command == "sync-brand-fonts":
        return cmd_sync_brand_fonts(root)
    if args.command == "reset-mcp":
        return cmd_reset_mcp(
            port_start=args.port_start,
            port_end=args.port_end,
            keep_ports=args.keep_port,
            dry_run=args.dry_run,
        )
    parser.error(f"Unknown command: {args.command}")
    return 2
