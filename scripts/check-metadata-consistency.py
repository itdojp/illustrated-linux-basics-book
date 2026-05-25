#!/usr/bin/env python3
"""Validate published metadata/navigation for illustrated-linux-basics-book."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

EXPECTED = {
    "title": "図解でわかるLinux基礎",
    "description": "図解とイラストでLinuxの基礎をやさしく学ぶ技術書",
    "author": "株式会社アイティードゥ",
    "version": "1.0.1",
    "language": "ja",
    "license": "CC BY-NC-SA 4.0",
    "repo": "itdojp/illustrated-linux-basics-book",
    "repo_url": "https://github.com/itdojp/illustrated-linux-basics-book",
    "pages_url": "https://itdojp.github.io/illustrated-linux-basics-book/",
    "baseurl": "/illustrated-linux-basics-book",
    "site_url": "https://itdojp.github.io",
}

EXPECTED_NAV = {
    "chapters": [f"/chapter{i}/" for i in range(0, 6)],
    "appendices": ["/appendix/"],
}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def read_text(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"{path}: failed to read ({exc})")
        return ""


def read_json(path: str) -> dict:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"{path}: invalid JSON ({exc})")
        return {}


def normalize_scalar(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    if " #" in value:
        value = value.split(" #", 1)[0].strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        value = value[1:-1]
    return value


def parse_top_level_yaml(path: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in read_text(path).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            data[match.group(1)] = normalize_scalar(match.group(2)) or ""
    return data


def parse_front_matter(path: str) -> tuple[dict[str, str], str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML front matter")
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{path}: missing closing YAML front matter delimiter")
        return {}, text
    raw = text[4:end]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            data[match.group(1)] = normalize_scalar(match.group(2)) or ""
    return data, text[end + len("\n---") :]


def parse_navigation(path: str) -> dict[str, list[str]]:
    nav: dict[str, list[str]] = {}
    current: str | None = None
    for line in read_text(path).splitlines():
        section = re.match(r"^([A-Za-z0-9_-]+):\s*$", line)
        if section:
            current = section.group(1)
            nav.setdefault(current, [])
            continue
        path_match = re.match(r"^\s*path:\s*(.+?)\s*$", line)
        if current and path_match:
            nav.setdefault(current, []).append(normalize_scalar(path_match.group(1)) or "")
    return nav


def expect_equal(label: str, actual: object, expected: object) -> None:
    if actual != expected:
        fail(f"{label}: expected {expected!r}, got {actual!r}")


def validate_book_config() -> None:
    cfg = read_json("book-config.json")
    expect_equal("book-config.json title", cfg.get("title"), EXPECTED["title"])
    expect_equal("book-config.json description", cfg.get("description"), EXPECTED["description"])
    expect_equal("book-config.json author", cfg.get("author"), EXPECTED["author"])
    expect_equal("book-config.json version", cfg.get("version"), EXPECTED["version"])
    expect_equal("book-config.json language", cfg.get("language"), EXPECTED["language"])
    expect_equal("book-config.json license", cfg.get("license"), EXPECTED["license"])
    repo = cfg.get("repository") or {}
    expect_equal("book-config.json repository.url", repo.get("url"), EXPECTED["repo_url"])
    expect_equal("book-config.json repository.branch", repo.get("branch"), "main")


def validate_jekyll_config() -> None:
    cfg = parse_top_level_yaml("docs/_config.yml")
    expect_equal("docs/_config.yml title", cfg.get("title"), EXPECTED["title"])
    expect_equal("docs/_config.yml description", cfg.get("description"), EXPECTED["description"])
    expect_equal("docs/_config.yml author", cfg.get("author"), EXPECTED["author"])
    expect_equal("docs/_config.yml version", cfg.get("version"), EXPECTED["version"])
    expect_equal("docs/_config.yml lang", cfg.get("lang"), EXPECTED["language"])
    expect_equal("docs/_config.yml baseurl", cfg.get("baseurl"), EXPECTED["baseurl"])
    expect_equal("docs/_config.yml url", cfg.get("url"), EXPECTED["site_url"])
    expect_equal("docs/_config.yml repository", cfg.get("repository"), EXPECTED["repo"])


def validate_index() -> None:
    front_matter, body = parse_front_matter("docs/index.md")
    expect_equal("docs/index.md front matter layout", front_matter.get("layout"), "book")
    expect_equal("docs/index.md front matter title", front_matter.get("title"), EXPECTED["title"])
    expect_equal("docs/index.md front matter author", front_matter.get("author"), EXPECTED["author"])
    expect_equal("docs/index.md front matter version", front_matter.get("version"), EXPECTED["version"])
    expect_equal("docs/index.md front matter description", front_matter.get("description"), EXPECTED["description"])
    expect_equal("docs/index.md front matter permalink", front_matter.get("permalink"), "/")
    if EXPECTED["description"] not in body:
        fail("docs/index.md body: missing canonical description")
    for path_value in [*EXPECTED_NAV["chapters"], *EXPECTED_NAV["appendices"]]:
        relative = f"./{path_value.strip('/')}" + "/"
        if relative not in body:
            fail(f"docs/index.md ToC: missing link target {relative}")


def validate_navigation() -> None:
    nav = parse_navigation("docs/_data/navigation.yml")
    for section, expected_paths in EXPECTED_NAV.items():
        expect_equal(f"docs/_data/navigation.yml {section} paths", nav.get(section), expected_paths)
    all_paths = [path for paths in nav.values() for path in paths]
    duplicates = sorted({path for path in all_paths if all_paths.count(path) > 1})
    if duplicates:
        fail(f"docs/_data/navigation.yml duplicate paths: {duplicates}")
    for path_value in [*EXPECTED_NAV["chapters"], *EXPECTED_NAV["appendices"]]:
        page = Path("docs") / path_value.strip("/") / "index.md"
        if not page.is_file():
            fail(f"navigation path {path_value}: missing {page}")


def validate_readme() -> None:
    readme = read_text("README.md")
    required_markers = [
        EXPECTED["title"],
        EXPECTED["pages_url"],
        EXPECTED["license"].replace(" ", ""),
        "knowledge@itdo.jp",
        "python3 scripts/check-metadata-consistency.py",
    ]
    compact = readme.replace(" ", "")
    for marker in required_markers:
        haystack = compact if marker == EXPECTED["license"].replace(" ", "") else readme
        if marker not in haystack:
            fail(f"README.md: missing marker {marker!r}")


def main() -> int:
    validate_book_config()
    validate_jekyll_config()
    validate_index()
    validate_navigation()
    validate_readme()
    if errors:
        print("Metadata consistency check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Metadata consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
