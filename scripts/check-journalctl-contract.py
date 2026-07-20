#!/usr/bin/env python3
"""Validate systemd journal guidance across chapters and the appendix (Issue #103)."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
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
        'id="journalctl-basics"',
        "$ tail -f application.log",
        "システムログのfile pathはlogging設定によって異なる",
        "$ systemctl status &lt;unit-name&gt; --no-pager",
        "$ journalctl -u &lt;unit-name&gt; -b -n 50 --no-pager",
        "$ journalctl -f -u &lt;unit-name&gt;",
        "現在のuser権限で実行",
        "ログ確認のために権限設定を変更しません",
        "../chapter4/#journal-troubleshooting",
    ]:
        require(chapter3, token, "chapter 3 journal basics")
    for token in [
        "$ tail -f /var/log/syslog",
        "$ tail -f /var/log/messages",
        "$ journalctl -f  # systemd-journald",
    ]:
        reject(chapter3, token, "chapter 3 fixed-path-first guidance")

    require(chapter4, 'id="journal-troubleshooting"', "chapter 4 journal diagnosis")
    diagnosis = chapter4[chapter4.index('id="journal-troubleshooting"') :]
    check_order(
        diagnosis,
        [
            'id="journal-troubleshooting"',
            "$ systemctl status &lt;unit-name&gt; --no-pager",
            "$ journalctl -u &lt;unit-name&gt; -b -n 100 --no-pager",
            "$ journalctl -u &lt;unit-name&gt; --since \"&lt;start-time&gt;\" --until \"&lt;end-time&gt;\" --no-pager",
            "$ journalctl -p err -b -n 100 --no-pager",
            "$ journalctl -f -u &lt;unit-name&gt;",
            'id="logging-stack-boundary"',
            "journalctl --list-boots",
            "systemctl status rsyslog --no-pager",
            "journalctl -xe",
        ],
        "chapter 4 purpose order",
    )
    for token in [
        "errorとそれより重大なpriorityだけを表示",
        "情報が足りなければpriority filterを外します",
        "所属groupと運用ルールを確認",
        "許可されている場合だけ同じ照会を<code>sudo</code>で再実行",
        "volatileな<code>/run/log/journal</code>",
        "persistentな<code>/var/log/journal</code>",
        "設定・保持期間・disk状況により過去bootが残らない",
        "logging daemonと設定がfileへ書く場合の例",
        "/etc/rsyslog.conf",
        "/etc/rsyslog.d/",
        "設定で確定したfileだけを<code>tail</code>",
        "unit・boot・時刻を自動では絞りません",
        "万能な初手にせず",
        "../appendix/#logging-source-notes",
    ]:
        require(chapter4, token, "chapter 4 logging boundary")
    for token in [
        "$ sudo tail -f /var/log/syslog",
        "$ sudo tail -f /var/log/messages",
        "$ sudo journalctl -xe",
    ]:
        reject(chapter4, token, "chapter 4 fixed-path/unscoped first step")

    for token in [
        "<code>tail -f application.log</code>",
        "<code>journalctl</code>",
        "-u, -b, -p, -f, --since, --until",
        "journalctl -u &lt;unit-name&gt; -b -n 50 --no-pager",
        'id="logging-stack-reference"',
        "<code>systemd-journald</code>がservice等のmessageを収集",
        "<code>journalctl</code>が参照可能なjournal entryの標準表示手段",
        "<code>rsyslogd</code>等を併用する構成では",
        "journalのsyslog messageを読み",
        "存在する場合の例",
        "ディストリビューション名だけでは決めません",
        'id="logging-source-notes"',
        "Logging Source Notes（確認日: 2026-07-20）",
        "https://www.freedesktop.org/software/systemd/man/latest/journalctl.html",
        "https://www.freedesktop.org/software/systemd/man/latest/journald.conf.html",
        "https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html",
        "configuring-logging_configuring-basic-system-settings",
        "各distributionの実設定を保証する資料ではありません",
        "他distributionのfile pathを保証する資料ではありません",
        "../chapter4/#journal-troubleshooting",
    ]:
        require(appendix, token, "appendix logging reference")
    for token in [
        "<code>tail -f /var/log/syslog</code>",
        "<code>tail -f /var/log/messages</code>",
        "systemd 環境では <code>journalctl</code> でも確認できます",
    ]:
        reject(appendix, token, "appendix fixed-path table")

    if check_workflow:
        workflow = read_text(root / ".github/workflows/book-qa.yml", "Book QA workflow")
        for token in [
            "python3 scripts/check-journalctl-contract.py --self-test",
            "python3 scripts/check-journalctl-contract.py",
            "python3 scripts/check-journalctl-contract.py --runtime-test",
            "python3 scripts/check-journalctl-contract.py --built-site _site",
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
    for name, tokens in {
        "chapter3": [
            'id="journalctl-basics"',
            "$ journalctl -u &lt;unit-name&gt; -b -n 50 --no-pager",
            "ログ確認のために権限設定を変更しません",
        ],
        "chapter4": [
            'id="journal-troubleshooting"',
            "$ journalctl -u &lt;unit-name&gt; --since \"&lt;start-time&gt;\" --until \"&lt;end-time&gt;\" --no-pager",
            "journalctl --list-boots",
            "設定で確定したfileだけを<code>tail</code>",
            "万能な初手にせず",
            'href="../appendix/#logging-source-notes"',
        ],
        "appendix": [
            'id="logging-stack-reference"',
            'id="logging-source-notes"',
            "存在する場合の例",
            "systemd journalctl manual",
            "RHEL 8 Configuring logging",
        ],
    }.items():
        text = snapshot.files[name]
        for token in tokens:
            require(text, token, f"built {name}")
    combined = "\n".join(snapshot.files.values())
    for token in [
        "$ sudo tail -f /var/log/syslog",
        "$ sudo tail -f /var/log/messages",
        "$ sudo journalctl -xe",
    ]:
        reject(combined, token, "built logging guidance")
    print("Built systemd journal guidance contract passed (3 pages).")


def runtime_test() -> None:
    def run(command: list[str]) -> subprocess.CompletedProcess[str]:
        try:
            return subprocess.run(command, check=False, capture_output=True, text=True, timeout=15)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise ContractError(f"runtime probe could not run {command[0]!r}: {exc}") from exc

    deadline = time.monotonic() + 30
    while True:
        state = run(["systemctl", "is-system-running"])
        system_state = state.stdout.strip()
        if system_state in {"running", "degraded"}:
            break
        if system_state not in {"initializing", "starting"} or time.monotonic() >= deadline:
            raise ContractError(f"runtime probe requires running systemd (state={system_state or 'unavailable'})")
        time.sleep(1)

    probes = [
        ["systemctl", "status", "systemd-journald.service", "--no-pager"],
        ["journalctl", "-u", "systemd-journald.service", "-b", "-n", "50", "--no-pager"],
        ["journalctl", "-u", "systemd-journald.service", "--since", "-1h", "--until", "now", "--no-pager"],
        ["journalctl", "-p", "err", "-b", "-n", "100", "--no-pager"],
        ["journalctl", "--list-boots", "--no-pager"],
    ]
    for command in probes:
        result = run(command)
        if result.returncode != 0:
            raise ContractError(f"runtime probe failed (rc={result.returncode}): {' '.join(command)}")

    try:
        followed = subprocess.run(
            ["journalctl", "-f", "-u", "systemd-journald.service", "--no-pager"],
            check=False,
            capture_output=True,
            text=True,
            timeout=2,
        )
    except subprocess.TimeoutExpired:
        followed = None
    except OSError as exc:
        raise ContractError(f"runtime follow probe could not run journalctl: {exc}") from exc
    if followed is not None and followed.returncode != 0:
        raise ContractError(f"runtime follow probe failed (rc={followed.returncode})")
    print(f"systemd journal runtime contract passed (state={system_state}, 6 read-only probes).")


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
        "fixed syslog first",
        lambda: check_source(mutated("chapter3", "$ tail -f application.log", "$ tail -f /var/log/syslog"), check_workflow=False),
        "application.log",
    )
    expect_failure(
        "unscoped journal first",
        lambda: check_source(mutated("chapter4", "$ journalctl -u &lt;unit-name&gt; -b -n 100 --no-pager", "$ sudo journalctl -xe"), check_workflow=False),
        "journalctl -u",
    )
    expect_failure(
        "missing current boot",
        lambda: check_source(mutated("chapter3", "&lt;unit-name&gt; -b -n 50", "&lt;unit-name&gt; -n 50"), check_workflow=False),
        "-b -n 50",
    )
    expect_failure(
        "missing permission boundary",
        lambda: check_source(mutated("chapter3", "ログ確認のために権限設定を変更しません", "必要なら権限を変更します"), check_workflow=False),
        "権限設定",
    )
    expect_failure(
        "missing file-output condition",
        lambda: check_source(mutated("appendix", "存在する場合の例", "全環境の標準path"), check_workflow=False),
        "存在する場合",
    )
    expect_failure(
        "stale source note",
        lambda: check_source(
            mutated(
                "appendix",
                "Logging Source Notes（確認日: 2026-07-20）",
                "Logging Source Notes（確認日なし）",
            ),
            check_workflow=False,
        ),
        "確認日",
    )
    expect_failure(
        "missing source limit",
        lambda: check_source(mutated("appendix", "他distributionのfile pathを保証する資料ではありません", "すべての環境へ適用"), check_workflow=False),
        "保証する資料",
    )
    print("systemd journal contract self-test passed (7 negative mutations).")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--built-site", type=Path)
    parser.add_argument("--runtime-test", action="store_true")
    args = parser.parse_args()
    modes = sum([args.self_test, args.built_site is not None, args.runtime_test])
    if modes > 1:
        raise ContractError("choose one of --self-test, --built-site, or --runtime-test")
    if args.self_test:
        self_test()
    elif args.built_site:
        check_built(load_built(args.built_site.resolve()))
    elif args.runtime_test:
        runtime_test()
    else:
        check_source(load_source())
        print("systemd journal guidance source contract passed (3 pages).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ContractError as exc:
        print(f"systemd journal contract failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
