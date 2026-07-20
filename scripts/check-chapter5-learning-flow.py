#!/usr/bin/env python3
"""Validate the staged Chapter 5 learning and runtime contract (Issue #101)."""

from __future__ import annotations

import argparse
import html
import os
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = Path("docs/chapter5/index.md")
BASELINE_BYTES = 8067
MAX_BYTES = int(BASELINE_BYTES * 1.10)


class ContractError(RuntimeError):
    pass


@dataclass(frozen=True)
class Snapshot:
    text: str

    @property
    def byte_count(self) -> int:
        return len(self.text.encode("utf-8"))


def require(text: str, token: str, label: str) -> None:
    if token not in text:
        raise ContractError(f"{label}: missing {token!r}")


def reject(text: str, token: str, label: str) -> None:
    if token in text:
        raise ContractError(f"{label}: forbidden token {token!r}")


def read_text(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ContractError(f"{label} unreadable: {path}: {exc}") from exc


def load_source(root: Path = ROOT) -> Snapshot:
    return Snapshot(read_text(root / CHAPTER, "chapter 5 source"))


def check_order(text: str, tokens: list[str], label: str) -> None:
    positions = []
    for token in tokens:
        require(text, token, label)
        positions.append(text.index(token))
    if positions != sorted(positions) or len(set(positions)) != len(positions):
        raise ContractError(f"{label}: staged concept order is broken")


def check_source(snapshot: Snapshot, root: Path = ROOT, check_workflow: bool = True) -> None:
    text = snapshot.text
    if snapshot.byte_count > MAX_BYTES:
        raise ContractError(
            f"chapter 5 size {snapshot.byte_count} exceeds {MAX_BYTES} bytes "
            f"(baseline {BASELINE_BYTES} + 10%)"
        )

    order = [
        'id="concept-variables"',
        'id="concept-command-substitution"',
        'id="concept-status"',
        'id="concept-strict-mode"',
        'id="backup-example"',
        'id="standalone-verification"',
        'id="cron-placeholder-example"',
    ]
    check_order(text, order, "chapter 5")

    prefix = text[: text.index('id="concept-command-substitution"')]
    reject(prefix, "$(date", "chapter 5 before command-substitution introduction")

    for token in [
        'SOURCE="$HOME/Documents"',
        '<code>"$SOURCE"</code>と引用',
        'DATE=$(date +%Y%m%d_%H%M%S)',
        "成功時に0、失敗時に0以外",
        "if tar ...; then",
        "set -euo pipefail",
        "停止しない文脈",
        "後始末も自動では行いません",
        "必要な箇所では<code>if</code>と<code>exit</code>を明示",
        "$ ./backup.sh &gt; backup.log 2&gt;&amp;1",
        "$ status=$?",
        '$ echo "$status"',
        "$ tail -n 20 backup.log",
        "0以外なら定期実行せず",
        "前節で終了ステータス0とログを確認した同じスクリプトだけ",
    ]:
        require(text, token, "chapter 5 learning contract")

    for token in [
        'SOURCE="$HOME/Documents"',
        'BACKUP_DIR="$HOME/backups"',
        'if [ ! -d "$SOURCE" ]; then',
        'if tar -czf "$BACKUP_DIR/$BACKUP_FILE" "$SOURCE"; then',
        'find "$BACKUP_DIR" -type f -name "backup_*.tar.gz" -mtime +7 -print',
        '0 3 * * * /home/&lt;user-name&gt;/scripts/backup.sh >> '
        '/home/&lt;user-name&gt;/logs/backup.log 2>&amp;1',
    ]:
        require(text, token, "chapter 5 safety contract")

    require(text, "-mtime +7 -delete  # 実際に削除する場合は", "chapter 5 opt-in deletion")
    reject(text, "echo \"今日は $(date) です\"", "minimal hello example")

    if check_workflow:
        workflow = read_text(root / ".github/workflows/book-qa.yml", "Book QA workflow")
        for token in [
            "python3 scripts/check-chapter5-learning-flow.py --self-test",
            'python3 scripts/check-chapter5-learning-flow.py --runtime-test --work-root "${RUNNER_TEMP}"',
            "python3 scripts/check-chapter5-learning-flow.py --built-site _site",
        ]:
            require(workflow, token, "Book QA workflow")


def extract_backup_script(text: str) -> str:
    match = re.search(
        r'<h3 id="backup-example">.*?</h3>\s*'
        r'<pre class="code-box"><code class="language-bash">(.*?)</code></pre>',
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise ContractError("chapter 5: backup.sh code block not found")
    return html.unescape(match.group(1)).strip() + "\n"


def run_checked(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(command, text=True, capture_output=True, timeout=30, check=False, **kwargs)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ContractError(f"runtime command failed to start/finish: {command}: {exc}") from exc


def runtime_test(work_root: Path) -> None:
    work_root.mkdir(parents=True, exist_ok=True)
    script_text = extract_backup_script(load_source().text)
    with tempfile.TemporaryDirectory(prefix="chapter5-runtime-", dir=work_root) as temp_name:
        temp = Path(temp_name)
        script = temp / "backup.sh"
        script.write_text(script_text, encoding="utf-8")

        syntax = run_checked(["bash", "-n", str(script)])
        if syntax.returncode != 0:
            raise ContractError(f"backup.sh bash -n failed: {syntax.stderr.strip()}")

        home = temp / "home with space"
        source = home / "Documents"
        backup_dir = home / "backups"
        source.mkdir(parents=True)
        backup_dir.mkdir(parents=True)
        (source / "sample.txt").write_text("chapter 5 runtime fixture\n", encoding="utf-8")
        old_archive = backup_dir / "backup_old.tar.gz"
        old_archive.write_text("do not delete\n", encoding="utf-8")
        old_time = time.time() - 8 * 24 * 60 * 60
        os.utime(old_archive, (old_time, old_time))

        env = os.environ.copy()
        env["HOME"] = str(home)
        normal = run_checked(["bash", str(script)], cwd=temp, env=env)
        if normal.returncode != 0:
            raise ContractError(
                f"backup.sh normal case returned {normal.returncode}: "
                f"stdout={normal.stdout!r} stderr={normal.stderr!r}"
            )
        require(normal.stdout, "バックアップ成功", "backup.sh normal output")
        require(normal.stdout, str(old_archive), "backup.sh -print output")
        if not old_archive.is_file():
            raise ContractError("backup.sh deleted the old archive although deletion must be opt-in")
        created = [path for path in backup_dir.glob("backup_*.tar.gz") if path != old_archive]
        if len(created) != 1 or created[0].stat().st_size == 0:
            raise ContractError(f"backup.sh normal case created unexpected archives: {created}")

        missing_home = temp / "missing home"
        missing_home.mkdir()
        env["HOME"] = str(missing_home)
        missing = run_checked(["bash", str(script)], cwd=temp, env=env)
        if missing.returncode != 1:
            raise ContractError(f"backup.sh missing-source case returned {missing.returncode}, expected 1")
        require(missing.stdout, "バックアップ元が見つかりません", "backup.sh missing-source output")

    print("Chapter 5 runtime contract passed (bash -n, normal, missing source, opt-in deletion).")


def check_built(site: Path) -> None:
    text = read_text(site / "chapter5/index.html", "built chapter 5")
    check_order(
        text,
        [
            'id="concept-variables"',
            'id="concept-command-substitution"',
            'id="concept-status"',
            'id="concept-strict-mode"',
            'id="backup-example"',
            'id="standalone-verification"',
            'id="cron-placeholder-example"',
        ],
        "built chapter 5",
    )
    for token in [
        "完成例で使う4つの要素",
        "停止しない文脈",
        "cronへ進む前の単体確認",
        "$ status=$?",
        "バックアップ成功",
        "-mtime +7 -print",
    ]:
        require(text, token, "built chapter 5")
    print("Built Chapter 5 learning-flow contract passed.")


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

    def mutated(old: str, new: str) -> Snapshot:
        if old not in baseline.text:
            raise ContractError(f"self-test fixture missing: {old!r}")
        return Snapshot(baseline.text.replace(old, new, 1))

    def swapped(first: str, second: str) -> Snapshot:
        if first not in baseline.text or second not in baseline.text:
            raise ContractError("self-test order fixture missing")
        placeholder = "__CHAPTER5_ORDER_PLACEHOLDER__"
        text = baseline.text.replace(first, placeholder, 1)
        text = text.replace(second, first, 1).replace(placeholder, second, 1)
        return Snapshot(text)

    expect_failure(
        "early command substitution",
        lambda: check_source(mutated("echo \"Hello, Linux World!\"", "echo \"$(date)\""), check_workflow=False),
        "before command-substitution introduction",
    )
    expect_failure(
        "missing strict-mode limit",
        lambda: check_source(mutated("停止しない文脈", "常に停止する"), check_workflow=False),
        "停止しない文脈",
    )
    expect_failure(
        "missing status gate",
        lambda: check_source(mutated("$ status=$?", "$ echo done"), check_workflow=False),
        "$ status=$?",
    )
    expect_failure(
        "unsafe deletion",
        lambda: check_source(mutated("-mtime +7 -print", "-mtime +7 -delete"), check_workflow=False),
        "-mtime +7 -print",
    )
    expect_failure(
        "broken order",
        lambda: check_source(swapped('id="concept-status"', 'id="backup-example"'), check_workflow=False),
        "staged concept order",
    )
    oversized = Snapshot(baseline.text + "x" * (MAX_BYTES - baseline.byte_count + 1))
    expect_failure("size budget", lambda: check_source(oversized, check_workflow=False), "exceeds")
    print("Chapter 5 learning-flow self-test passed (6 negative mutations).")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--runtime-test", action="store_true")
    parser.add_argument("--work-root", type=Path)
    parser.add_argument("--built-site", type=Path)
    args = parser.parse_args()
    selected = sum([args.self_test, args.runtime_test, args.built_site is not None])
    if selected > 1:
        raise ContractError("choose only one of --self-test, --runtime-test, or --built-site")
    if args.work_root and not args.runtime_test:
        raise ContractError("--work-root requires --runtime-test")

    if args.self_test:
        self_test()
    elif args.runtime_test:
        if args.work_root is None:
            raise ContractError("--runtime-test requires --work-root")
        runtime_test(args.work_root.resolve())
    elif args.built_site:
        check_built(args.built_site.resolve())
    else:
        snapshot = load_source()
        check_source(snapshot)
        print(f"Chapter 5 learning-flow source contract passed ({snapshot.byte_count}/{MAX_BYTES} bytes).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ContractError as exc:
        print(f"Chapter 5 learning-flow contract failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
