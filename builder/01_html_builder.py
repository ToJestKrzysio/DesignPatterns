from __future__ import annotations


class HtmlTag:
    tag: str
    elements: list[HtmlTag]

    INDENT = 2

    def __init__(self, tag: str):
        self.tag = tag
        self.elements = []

    def _show(self, indent: int) -> str:
        lines = []
        line_indent = type(self).INDENT * indent * " "
        lines.append(f"{line_indent}<{self.tag}>")

        for element in self.elements:
            lines.append(element._show(indent + 1))

        lines.append(f"{line_indent}</{self.tag}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self._show(0)


class HtmlBuilder:

    def __init__(self, tag: str):
        self._parent_tag = tag
        self._parent = HtmlTag(tag)

    def add_child(self, child_tag: str) -> HtmlBuilder:
        self._parent.elements.append(
            HtmlTag(child_tag)
        )
        return self

    def clear(self):
        self._parent = HtmlTag(self._parent_tag)

    def __str__(self) -> str:
        return str(self._parent)
