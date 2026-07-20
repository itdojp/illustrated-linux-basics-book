#!/usr/bin/env python3
"""Validate DNF/YUM generation, diagnosis, and source-note contracts (Issue #102)."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "chapter3": Path("docs/chapter3/index.md"),
    "chapter4": Path("docs/chapter4/index.md"),
    "appendix": Path("docs/appendix/index.md"),
}


class ContractError(RuntimeError):
    pass


@dataclass(frozen=True)
class Snapshot:
    files: Dict[str, str]


def require(text: str, token: str, label: str) -> None:
    if token not in text:
        raise ContractError(f"{label}: missing {token!r}")


def reject(text: str, token: str, label: str) -> None:
    if token in text:
        raise ContractError(f"{label}: forbidden/obsolete token {token!r}")


def read_text(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ContractError(f"{label} unreadable: {path}: {exc}") from exc


def load_source(root: Path = ROOT) -> Snapshot:
    return Snapshot({name: read_text(root / path, name) for name, path in TARGETS.items()})


def check_order(text: str, tokens: list[str], label: str) -> None:
    positions = []
    for token in tokens:
        require(text, token, label)
        positions.append(text.index(token))
    if positions != sorted(positions) or len(set(positions)) != len(positions):
        raise ContractError(f"{label}: expected order is broken")


def check_source(snapshot: Snapshot, root: Path = ROOT, check_workflow: bool = True) -> None:
    chapter3 = snapshot.files["chapter3"]
    chapter4 = snapshot.files["chapter4"]
    appendix = snapshot.files["appendix"]

    for token in [
        'id="dnf-yum-generations"',
        "DNF / YUM互換",
        "dnf install, dnf upgrade",
        "RHEL 9はDNF",
        "RHEL 8はDNF技術を使うYUM v4",
        "Fedora 41以降",
        "dnf --version",
        "$ sudo dnf install httpd",
        "$ sudo dnf remove &lt;package-name&gt;",
        "$ dnf check-upgrade",
        "$ sudo dnf upgrade",
        "DNF4の<code>update</code>は<code>upgrade</code>の非推奨alias",
        "yum update --obsoletes",
        "「常に同義」と扱いません",
    ]:
        require(chapter3, token, "chapter 3 DNF route")
    for token in [
        "$ sudo yum install httpd",
        "$ sudo yum remove &lt;package-name&gt;",
        "$ sudo yum update",
        "$ sudo yum upgrade  # update と同義",
        "yum install, dnf update",
    ]:
        reject(chapter3, token, "chapter 3 legacy route")

    recovery = chapter4[chapter4.index('id="dnf-recovery"') :]
    check_order(
        recovery,
        [
            'id="dnf-recovery"',
            "$ cat /etc/os-release",
            "$ dnf --version",
            "$ dnf check",
            "$ dnf history list",
            "$ dnf history info &lt;transaction-id&gt;",
            "インストール済みRPMの不整合",
            "中断したトランザクション",
            "リポジトリメタデータ",
            "リポジトリとのバージョン差",
            "旧YUMの<code>yum-complete-transaction</code>",
        ],
        "chapter 4 diagnosis",
    )
    for token in [
        "パッケージを変更しない確認から始めます",
        "（パッケージ変更なし）",
        "history undo",
        "パッケージの削除・downgrade",
        "sudo dnf clean metadata",
        "sudo dnf makecache",
        "メタデータcacheだけを再作成",
        "インストール済みパッケージは変更しません",
        "sudo dnf --assumeno distro-sync",
        "全インストール済みパッケージが対象",
        "upgradeまたはdowngrade",
        "確認できるまで承認しません",
        "中断した旧YUMトランザクションを再開する専用ツール",
        "依存関係エラー一般の解決策でも",
        "../appendix/#dnf-source-notes",
    ]:
        require(chapter4, token, "chapter 4 impact boundary")
    reject(chapter4, "$ sudo yum-complete-transaction", "chapter 4 generic repair")
    reject(chapter4, "$ sudo dnf distro-sync", "chapter 4 unpreviewed distro-sync")

    for token in [
        "<td>トランザクション（transaction）</td>",
        "パッケージのinstall・upgrade・remove等を一まとまりで計画・記録する単位",
        'id="dnf-source-notes"',
        "確認日: 2026-07-20",
        "https://dnf.readthedocs.io/en/stable/command_ref.html",
        "https://dnf.readthedocs.io/en/stable/cli_vs_yum.html",
        "https://dnf5.readthedocs.io/en/stable/dnf5.8.html",
        "https://dnf5.readthedocs.io/en/stable/commands/check-upgrade.8.html",
        "https://fedoraproject.org/wiki/Changes/SwitchToDnf5",
        "software-management_considerations-in-adopting-rhel-8",
        "assembly_software-management_considerations-in-adopting-rhel-9",
        "assembly_handling-package-management-history_managing-software-with-the-dnf-tool",
        "sec2-yum-complete-transaction",
        "DNF4固有aliasの保証には使わない",
        "RHEL 8/9の一般修復には適用しない",
    ]:
        require(appendix, token, "appendix DNF source notes")

    if check_workflow:
        workflow = read_text(root / ".github/workflows/book-qa.yml", "Book QA workflow")
        for token in [
            "python3 scripts/check-dnf-yum-contract.py --self-test",
            "python3 scripts/check-dnf-yum-contract.py",
            "python3 scripts/check-dnf-yum-contract.py --built-site _site",
        ]:
            require(workflow, token, "Book QA workflow")


def load_built(site: Path) -> Snapshot:
    paths = {
        "chapter3": site / "chapter3/index.html",
        "chapter4": site / "chapter4/index.html",
        "appendix": site / "appendix/index.html",
    }
    return Snapshot({name: read_text(path, f"built {name}") for name, path in paths.items()})


def check_built(snapshot: Snapshot) -> None:
    chapter3 = snapshot.files["chapter3"]
    chapter4 = snapshot.files["chapter4"]
    appendix = snapshot.files["appendix"]
    for name, text, tokens in [
        (
            "chapter3",
            chapter3,
            [
                'id="dnf-yum-generations"',
                "DNFとYUMの世代差",
                "$ sudo dnf upgrade",
                "yum update --obsoletes",
                "常に同義",
            ],
        ),
        (
            "chapter4",
            chapter4,
            [
                'id="dnf-recovery"',
                "$ dnf check",
                "$ dnf history list",
                "sudo dnf --assumeno distro-sync",
                "確認できるまで承認しません",
                'href="../appendix/#dnf-source-notes"',
            ],
        ),
        (
            "appendix",
            appendix,
            ['id="dnf-source-notes"', "確認日: 2026-07-20", "DNF4 Command Reference", "RHEL 6 Completing Transactions"],
        ),
    ]:
        for token in tokens:
            require(text, token, f"built {name}")
    reject(chapter3, "$ sudo yum upgrade  # update と同義", "built chapter3")
    reject(chapter4, "$ sudo yum-complete-transaction", "built chapter4")
    print("Built DNF/YUM generation and recovery contract passed (3 pages).")


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

    def mutated(name: str, old: str, new: str) -> Snapshot:
        files = dict(baseline.files)
        if old not in files[name]:
            raise ContractError(f"self-test fixture missing: {name}: {old!r}")
        files[name] = files[name].replace(old, new, 1)
        return Snapshot(files)

    expect_failure(
        "old equivalence",
        lambda: check_source(mutated("chapter3", "$ sudo dnf upgrade", "$ sudo yum upgrade  # update と同義"), check_workflow=False),
        "dnf upgrade",
    )
    expect_failure(
        "generic yum repair",
        lambda: check_source(mutated("chapter4", "$ dnf check", "$ sudo yum-complete-transaction"), check_workflow=False),
        "$ dnf check",
    )
    expect_failure(
        "unpreviewed distro-sync",
        lambda: check_source(
            mutated("chapter4", "sudo dnf --assumeno distro-sync", "$ sudo dnf distro-sync"),
            check_workflow=False,
        ),
        "--assumeno",
    )
    expect_failure(
        "missing impact",
        lambda: check_source(mutated("chapter4", "upgradeまたはdowngrade", "packageを調整"), check_workflow=False),
        "upgradeまたはdowngrade",
    )
    expect_failure(
        "stale source note",
        lambda: check_source(mutated("appendix", "確認日: 2026-07-20", "確認日なし"), check_workflow=False),
        "確認日",
    )
    expect_failure(
        "missing legacy boundary",
        lambda: check_source(
            mutated("appendix", "RHEL 8/9の一般修復には適用しない", "すべてのRHELに適用"),
            check_workflow=False,
        ),
        "一般修復",
    )
    print("DNF/YUM contract self-test passed (6 negative mutations).")


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
    else:
        check_source(load_source())
        print("DNF/YUM generation and recovery source contract passed (3 pages).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ContractError as exc:
        print(f"DNF/YUM contract failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
