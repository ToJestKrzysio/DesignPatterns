class HtmlTag:
    INDENT = 2

    def __init__(self, tag: str):
        self.tag = tag
        self.elements = []

    def _show(self, indent: int) -> str:
        lines = []
        line_indent = type(self).INDENT * indent * " "
        lines.append(f"{line_indent}<{self.tag}>")

        for element in self.elements:
            lines.append(element.show(indent + 1))

        lines.append(f"{line_indent}</{self.tag}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self._show(0)
