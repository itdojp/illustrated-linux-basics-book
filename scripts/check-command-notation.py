#!/usr/bin/env python3
"""Fail-closed contract for the beginner command-notation legend (Issue #100)."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "index": "index.md",
    "chapter1": "chapter1/index.md",
    "chapter2": "chapter2/index.md",
    "chapter3": "chapter3/index.md",
    "chapter4": "chapter4/index.md",
    "chapter5": "chapter5/index.md",
    "appendix": "appendix/index.md",
}


class ContractError(RuntimeError):
    pass


@dataclass
class Snapshot:
    files: Dict[str, str]


def require(text: str, token: str, label: str) -> None:
    if token not in text:
        raise ContractError(f"{label}: missing {token!r}")


def reject(text: str, token: str, label: str) -> None:
    if token in text:
        raise ContractError(f"{label}: obsolete/bare notation remains: {token!r}")


def load_source(root: Path = ROOT) -> Snapshot:
    files: Dict[str, str] = {}
    for name, rel in TARGETS.items():
        path = root / "docs" / rel
        try:
            files[name] = path.read_text(encoding="utf-8")
        except OSError as exc:
            raise ContractError(f"source page unreadable ({name}): {path}: {exc}") from exc
    return Snapshot(files)


def check_source(snapshot: Snapshot) -> None:
    index = snapshot.files["index"]
    for token in [
        "## コマンド例の読み方 {#command-notation}",
        "`$ command`", "`# command`", "`<user-name>`", "`$PATH` / `$HOME`",
        "通常は `$` を入力せず", "`<` や `>` をそのままシェルへ貼り付けません",
        "管理者権限を使う `sudo`", "./chapter1/#command-examples",
        "./chapter3/#package-placeholder-example", "./chapter4/#path-placeholder-example",
        "./chapter5/#cron-placeholder-example", "./appendix/#glossary",
    ]:
        require(index, token, "docs/index.md")

    chapter1 = snapshot.files["chapter1"]
    require(chapter1, 'id="command-examples"', "chapter1")
    require(chapter1, '../#command-notation', "chapter1")
    if chapter1.index('../#command-notation') > chapter1.index('class="command-box"'):
        raise ContractError("chapter1: legend link must precede the first command example")

    chapter5 = snapshot.files["chapter5"]
    require(chapter5, 'id="cron-placeholder-example"', "chapter5")
    require(chapter5, '../#command-notation', "chapter5")
    if chapter5.index('../#command-notation') > chapter5.index('class="command-box"'):
        raise ContractError("chapter5: legend link must precede the first command example")

    required_by_file = {
        "chapter1": ["&lt;user-name&gt;:&lt;group-name&gt;"],
        "chapter2": ["&lt;user-name&gt;", "&lt;group-name&gt;"],
        "chapter3": ['id="package-placeholder-example"', "&lt;package-name&gt;"],
        "chapter4": ['id="path-placeholder-example"', "&lt;directory-path&gt;", "$ sudo passwd &lt;user-name&gt;"],
        "chapter5": ["&lt;user-name&gt;"],
        "appendix": ["プロンプト", "プレースホルダー", "<code>PATH</code>", "<code>HOME</code>"],
    }
    for name, tokens in required_by_file.items():
        for token in tokens:
            require(snapshot.files[name], token, name)

    combined = "\n".join(snapshot.files.values())
    for token in ["&lt;linuxuser&gt;", "$ passwd username", "chown user:group", "/new/path", "&lt;new-path&gt;"]:
        reject(combined, token, "docs")
    without_canonical = combined.replace("&lt;package-name&gt;", "").replace("<package-name>", "")
    reject(without_canonical, "package-name", "docs")


def load_built(site: Path) -> Snapshot:
    paths = {
        "index": site / "index.html",
        "chapter1": site / "chapter1" / "index.html",
        "chapter2": site / "chapter2" / "index.html",
        "chapter3": site / "chapter3" / "index.html",
        "chapter4": site / "chapter4" / "index.html",
        "chapter5": site / "chapter5" / "index.html",
        "appendix": site / "appendix" / "index.html",
    }
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise ContractError("built pages missing: " + ", ".join(missing))
    return Snapshot({name: path.read_text(encoding="utf-8") for name, path in paths.items()})


def check_built(snapshot: Snapshot) -> None:
    for name, token in {
        "index": 'id="command-notation"',
        "chapter1": 'id="command-examples"',
        "chapter3": 'id="package-placeholder-example"',
        "chapter4": 'id="path-placeholder-example"',
        "chapter5": 'id="cron-placeholder-example"',
        "appendix": 'id="glossary"',
    }.items():
        require(snapshot.files[name], token, f"built {name}")
    combined = "\n".join(snapshot.files.values())
    for token in [
        "コマンド例の読み方", "通常は", "を入力せず",
        "&lt;user-name&gt;", "&lt;package-name&gt;", "&lt;directory-path&gt;",
        "プロンプト", "プレースホルダー", "環境変数",
    ]:
        require(combined, token, "built site")
    for token in ["&lt;linuxuser&gt;", "$ passwd username", "chown user:group", "/new/path", "&lt;new-path&gt;"]:
        reject(combined, token, "built site")


def expect_failure(label: str, action, expected: str) -> None:
    try:
        action()
    except ContractError as exc:
        if expected in str(exc):
            return
        raise ContractError(f"self-test {label}: wrong error: {exc}") from exc
    raise ContractError(f"self-test {label}: mutation was accepted")


def self_test() -> None:
    baseline = load_source()
    check_source(baseline)

    expect_failure("missing source page", lambda: load_source(ROOT / "missing-fixture"), "source page unreadable (index)")

    def mutated(name: str, old: str, new: str) -> Snapshot:
        files = dict(baseline.files)
        if old not in files[name]:
            raise ContractError(f"self-test fixture missing: {old}")
        files[name] = files[name].replace(old, new, 1)
        return Snapshot(files)

    expect_failure("legend", lambda: check_source(mutated("index", "## コマンド例の読み方", "## 例の読み方")), "コマンド例")
    expect_failure("old user placeholder", lambda: check_source(mutated("chapter5", "&lt;user-name&gt;", "&lt;linuxuser&gt;")), "linuxuser")
    expect_failure("bare package", lambda: check_source(mutated("chapter3", "&lt;package-name&gt;", "package-name")), "package-name")
    expect_failure("missing backlink", lambda: check_source(mutated("chapter1", "../#command-notation", "../")), "command-notation")
    expect_failure("glossary", lambda: check_source(mutated("appendix", "プレースホルダー", "置換値")), "プレースホルダー")
    print("Command notation self-test passed (6 negative mutations).")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--built-site", type=Path)
    args = parser.parse_args()
    if args.self_test and args.built_site:
        raise ContractError("choose either --self-test or --built-site")
    if args.self_test:
        self_test()
    elif args.built_site:
        check_built(load_built(args.built_site.resolve()))
        print("Built command notation contract passed (7 pages).")
    else:
        check_source(load_source())
        print("Source command notation contract passed (7 pages).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ContractError as exc:
        print(f"Command notation contract failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
