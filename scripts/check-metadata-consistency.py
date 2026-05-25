#!/usr/bin/env python3
"""Validate published metadata/navigation for illustrated-linux-basics-book."""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_NAV = {
    "chapters": ["/chapter{}/".format(i) for i in range(0, 6)],
    "appendices": ["/appendix/"],
}

errors = []  # type: List[str]


def fail(message: str) -> None:
    errors.append(message)


def repo_path(path: str) -> Path:
    return ROOT / path


def read_text(path: str) -> Optional[str]:
    try:
        return repo_path(path).read_text(encoding="utf-8")
    except OSError as exc:
        fail("{}: failed to read ({})".format(path, exc))
        return None


def read_json(path: str) -> Dict[str, Any]:
    text = read_text(path)
    if text is None:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        fail("{}: invalid JSON ({})".format(path, exc))
        return {}
    if not isinstance(data, dict):
        fail("{}: expected JSON object".format(path))
        return {}
    return data


def normalize_scalar(value: Optional[str]) -> Optional[str]:
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


def parse_top_level_yaml(path: str) -> Dict[str, str]:
    text = read_text(path)
    if text is None:
        return {}
    data = {}  # type: Dict[str, str]
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            data[match.group(1)] = normalize_scalar(match.group(2)) or ""
    return data


def parse_front_matter(path: str) -> Tuple[Dict[str, str], str]:
    text = read_text(path)
    if text is None:
        return {}, ""
    if not text.startswith("---\n"):
        fail("{}: missing YAML front matter".format(path))
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        fail("{}: missing closing YAML front matter delimiter".format(path))
        return {}, text
    raw = text[4:end]
    data = {}  # type: Dict[str, str]
    for line in raw.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            data[match.group(1)] = normalize_scalar(match.group(2)) or ""
    return data, text[end + len("\n---") :]


def parse_navigation(path: str) -> Dict[str, List[str]]:
    text = read_text(path)
    if text is None:
        return {}
    nav = {}  # type: Dict[str, List[str]]
    current = None  # type: Optional[str]
    for line in text.splitlines():
        section = re.match(r"^([A-Za-z0-9_-]+):\s*$", line)
        if section:
            current = section.group(1)
            nav.setdefault(current, [])
            continue
        path_match = re.match(r"^\s*path:\s*(.+?)\s*$", line)
        if current and path_match:
            nav.setdefault(current, []).append(normalize_scalar(path_match.group(1)) or "")
    return nav


def expect_equal(label: str, actual: Any, expected: Any) -> None:
    if actual != expected:
        fail("{}: expected {!r}, got {!r}".format(label, expected, actual))


def require_string(source: str, data: Dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        fail("{} {}: expected non-empty string".format(source, key))
        return ""
    return value.strip()


def repo_slug_from_url(repo_url: str) -> str:
    match = re.match(r"^https://github\.com/([^/]+)/([^/]+)/?$", repo_url)
    if not match:
        fail("book-config.json repository.url: expected https://github.com/<owner>/<repo>")
        return ""
    owner, repo_name = match.groups()
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]
    return "{}/{}".format(owner, repo_name)


def expected_from_book_config(cfg: Dict[str, Any]) -> Dict[str, str]:
    repository = cfg.get("repository")
    if not isinstance(repository, dict):
        fail("book-config.json repository: expected object")
        repository = {}

    repo_url = require_string("book-config.json repository", repository, "url")
    repo_slug = repo_slug_from_url(repo_url) if repo_url else ""
    owner = repo_slug.split("/", 1)[0] if "/" in repo_slug else ""
    repo_name = repo_slug.split("/", 1)[1] if "/" in repo_slug else ""
    site_url = "https://{}.github.io".format(owner) if owner else ""

    return {
        "title": require_string("book-config.json", cfg, "title"),
        "description": require_string("book-config.json", cfg, "description"),
        "author": require_string("book-config.json", cfg, "author"),
        "version": require_string("book-config.json", cfg, "version"),
        "language": require_string("book-config.json", cfg, "language"),
        "license": require_string("book-config.json", cfg, "license"),
        "repo": repo_slug,
        "repo_url": repo_url,
        "pages_url": "{}/{}/".format(site_url, repo_name) if site_url and repo_name else "",
        "baseurl": "/{}".format(repo_name) if repo_name else "",
        "site_url": site_url,
        "branch": require_string("book-config.json repository", repository, "branch"),
    }


def validate_book_config() -> Dict[str, str]:
    cfg = read_json("book-config.json")
    expected = expected_from_book_config(cfg)
    expect_equal("book-config.json repository.branch", expected.get("branch"), "main")
    return expected


def validate_jekyll_config(expected: Dict[str, str]) -> None:
    cfg = parse_top_level_yaml("docs/_config.yml")
    expect_equal("docs/_config.yml title", cfg.get("title"), expected["title"])
    expect_equal("docs/_config.yml description", cfg.get("description"), expected["description"])
    expect_equal("docs/_config.yml author", cfg.get("author"), expected["author"])
    expect_equal("docs/_config.yml version", cfg.get("version"), expected["version"])
    expect_equal("docs/_config.yml lang", cfg.get("lang"), expected["language"])
    expect_equal("docs/_config.yml baseurl", cfg.get("baseurl"), expected["baseurl"])
    expect_equal("docs/_config.yml url", cfg.get("url"), expected["site_url"])
    expect_equal("docs/_config.yml repository", cfg.get("repository"), expected["repo"])


def validate_index(expected: Dict[str, str]) -> None:
    front_matter, body = parse_front_matter("docs/index.md")
    expect_equal("docs/index.md front matter layout", front_matter.get("layout"), "book")
    expect_equal("docs/index.md front matter title", front_matter.get("title"), expected["title"])
    expect_equal("docs/index.md front matter author", front_matter.get("author"), expected["author"])
    expect_equal("docs/index.md front matter version", front_matter.get("version"), expected["version"])
    expect_equal(
        "docs/index.md front matter description",
        front_matter.get("description"),
        expected["description"],
    )
    expect_equal("docs/index.md front matter permalink", front_matter.get("permalink"), "/")
    if expected["description"] not in body:
        fail("docs/index.md body: missing canonical description")
    for path_value in EXPECTED_NAV["chapters"] + EXPECTED_NAV["appendices"]:
        relative = "./{}/".format(path_value.strip("/"))
        if relative not in body:
            fail("docs/index.md ToC: missing link target {}".format(relative))


def validate_navigation() -> None:
    nav = parse_navigation("docs/_data/navigation.yml")
    for section, expected_paths in EXPECTED_NAV.items():
        expect_equal("docs/_data/navigation.yml {} paths".format(section), nav.get(section), expected_paths)
    all_paths = [path for paths in nav.values() for path in paths]
    duplicates = sorted({path for path in all_paths if all_paths.count(path) > 1})
    if duplicates:
        fail("docs/_data/navigation.yml duplicate paths: {}".format(duplicates))
    for path_value in EXPECTED_NAV["chapters"] + EXPECTED_NAV["appendices"]:
        page = repo_path("docs") / path_value.strip("/") / "index.md"
        if not page.is_file():
            fail("navigation path {}: missing {}".format(path_value, page.relative_to(ROOT)))


def validate_readme(expected: Dict[str, str]) -> None:
    readme = read_text("README.md")
    if readme is None:
        return
    required_markers = [
        expected["title"],
        expected["pages_url"],
        expected["license"].replace(" ", ""),
        "knowledge@itdo.jp",
        "python3 scripts/check-metadata-consistency.py",
    ]
    compact = readme.replace(" ", "")
    for marker in required_markers:
        haystack = compact if marker == expected["license"].replace(" ", "") else readme
        if marker not in haystack:
            fail("README.md: missing marker {!r}".format(marker))


def main() -> int:
    expected = validate_book_config()
    validate_jekyll_config(expected)
    validate_index(expected)
    validate_navigation()
    validate_readme(expected)
    if errors:
        print("Metadata consistency check failed:", file=sys.stderr)
        for error in errors:
            print("- {}".format(error), file=sys.stderr)
        return 1
    print("Metadata consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
