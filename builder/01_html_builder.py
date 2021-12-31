from __future__ import annotations


class HtmlTag:
    tag: str
    elements: list[HtmlTag]

    INDENT = 2

    def __init__(self, tag: str, value: str = ""):
        self.tag = tag
        self.value = value
        self.elements = []

    def _show(self, indent: int) -> str:
        lines = []
        tag_indent = type(self).INDENT * indent * " "
        lines.append(f"{tag_indent}<{self.tag}>")

        if self.value:
            value_indent = type(self).INDENT * (indent+1) * " "
            lines.append(f"{value_indent}{self.value}")

        for element in self.elements:
            lines.append(element._show(indent + 1))

        lines.append(f"{tag_indent}</{self.tag}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self._show(0)


class HtmlBuilder:
    _parent_tag: str
    _parent_value: str
    _parent: HtmlTag

    def __init__(self, tag: str, value: str = ""):
        self._parent_tag = tag
        self._parent_value = value
        self._parent = HtmlTag(tag, value)

    def add_child(self, child_tag: str | HtmlBuilder, child_value="") -> HtmlBuilder:
        appended_child = (child_tag._parent if isinstance(child_tag, HtmlBuilder)
                          else HtmlTag(child_tag, child_value))
        self._parent.elements.append(appended_child)
        return self

    def clear(self):
        self._parent = HtmlTag(self._parent_tag, self._parent_value)

    def __str__(self) -> str:
        return str(self._parent)


if __name__ == '__main__':
    builder = HtmlBuilder("ul")
    builder.add_child("li", "Hello")
    builder.add_child("li", "World")
    builder.add_child(HtmlBuilder("p", "Hi"))
    print(builder)
