from __future__ import annotations

from dataclasses import InitVar, dataclass
from functools import cached_property
import nbformat
import re
from typing import Any, Callable, List, Optional


@dataclass
class TagPreSaveHook:
    # https://nbformat.readthedocs.io/en/latest/changelog.html#id4
    normalize: bool = False
    comment_marker: str = "#"
    prefix: str = "%tags"

    # Jupyter logging accesses this during startup
    __name__ = "TagPreSaveHook"

    @cached_property
    def tag_pattern(self):
        return re.compile(
            rf"^\s*{self.comment_marker}[{self.comment_marker}\s]*{self.prefix}\s*:\s*(?P<tags>.+)$",
            re.MULTILINE,
        )

    def extract_tags(self, cell_source: str) -> List[str]:
        if m := self.tag_pattern.search(cell_source):
            tags = m.group("tags")
            return [t.strip() for t in tags.split(",")]
        return []

    def __call__(self, model, **kwargs):
        if model["type"] != "notebook":
            return

        self._set_tags(model)

        if self.normalize:
            _changes, model["content"] = nbformat.validator.normalize(model["content"])

    def _set_tags(self, model):
        for cell in model["content"]["cells"]:
            tags = self.extract_tags(cell["source"])
            cell["metadata"]["tags"] = tags
