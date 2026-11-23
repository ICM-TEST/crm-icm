#!/usr/bin/env python3
"""What this repo must be true of before it's released. Run from the repo root:
    python3 tools/tests/test_structure.py
Needs only Python 3.10+. It reads the repo and nothing else: there is no client data to test against."""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
WS = REPO / "workspace"
ERROR_500 = "Error 500 - Sorry, this request cannot be carried out"
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
TEMPLATES = ("client-card", "report-dashboard", "client-history", "page-years")


def workspace_files():
    return [p for p in WS.rglob("*") if p.is_file() and p.name != ".DS_Store"]


def outside_fences(text):
    kept, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            kept.append(line)
    return "\n".join(kept)


class Structure(unittest.TestCase):
    def test_workspace_is_markdown_only(self):
        self.assertEqual([str(p.relative_to(REPO)) for p in workspace_files() if p.suffix != ".md"], [])

    def test_relative_links_resolve(self):
        missing = []
        for f in WS.rglob("*.md"):
            text = INLINE_CODE.sub("", outside_fences(f.read_text(encoding="utf-8")))
            for ref in LINK.findall(text):
                if ref.startswith(("http:", "https:", "mailto:", "#")) or "<" in ref or "{" in ref:
                    continue
                target = ref.split("#")[0]
                if target and not (f.parent / target).exists():
                    missing.append(f"{f.relative_to(REPO)}: {ref}")
        self.maxDiff = None
        self.assertEqual(missing, [])

    def test_the_map_exists_is_short_and_holds_the_lock(self):
        claude = WS / "CLAUDE.md"
        self.assertTrue(claude.exists())
        text = claude.read_text(encoding="utf-8")
        self.assertLessEqual(len(text.splitlines()), 80, "the map routes; it holds no content")
        self.assertIn(ERROR_500, text)

    def test_version_file_has_a_version(self):
        self.assertRegex((WS / "version.md").read_text(encoding="utf-8"), r"(?m)^version: \d+\.\d+\.\d+$")

    def test_html_templates_have_one_html_block_with_placeholders(self):
        for name in TEMPLATES:
            text = (WS / "templates" / f"{name}.md").read_text(encoding="utf-8")
            blocks = re.findall(r"```html\n(.*?)```", text, re.S)
            self.assertEqual(len(blocks), 1, f"{name}.md must have exactly one html block")
            self.assertIn("{{", blocks[0], f"{name}.md html block has no {{{{ placeholder")

    def test_project_instruction_has_provider_and_lock(self):
        text = (REPO / "setup/project-instructions.md").read_text(encoding="utf-8")
        self.assertIn("System provider:", text)
        self.assertIn("Lock:", text)

    def test_workspace_is_small(self):
        total = sum(p.stat().st_size for p in workspace_files())
        self.assertLess(total, 100_000, "workspace/ is attached to every chat: keep it small")

    def test_no_connectors_mentioned(self):
        bad = []
        for f in workspace_files():
            for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                if "connector" in line.lower() and "No Google connectors" not in line:
                    bad.append(f"{f.relative_to(REPO)}:{n}")
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main(verbosity=1)
