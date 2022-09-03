from html.parser import HTMLParser
import re


class OpenXrDocstringParser(HTMLParser):
    def __init__(self, function_name: str):
        super().__init__()
        self.function_name = function_name
        self.in_header = False
        self.in_paragraph = False
        self.brief_description = None
        self.tag_stack = list()

    @property
    def docstring(self):
        return f"""{self.brief_description}"""  # TODO: more

    def handle_endtag(self, tag: str) -> None:
        # print(f"end {tag}")
        pop = self.tag_stack.pop()
        while pop != tag:
            pop = self.tag_stack.pop()
        assert pop == tag
        if tag == "p":
            self.in_paragraph = False

    def handle_starttag(self, tag: str, attrs: list) -> None:
        self.tag_stack.append(tag)
        d = {k: v for k, v in attrs}
        # print(f"start {tag} {d}")
        if tag == "div" and "id" in d:
            self.in_header = d["id"] == "header"
        if tag == "p":
            self.in_paragraph = True

    def handle_data(self, data: str) -> None:
        if self.in_header and self.in_paragraph:
            if self.function_name in data:
                match = re.match(f"{self.function_name} - (\S.*)", data)
                assert match
                brief_description = match.group(1)
                brief_description = brief_description.strip()
                if not brief_description.endswith("."):
                    brief_description += "."
                # e.g. "Gets a function pointer for an OpenXR function."
                self.brief_description = brief_description


def create_docstring(function_name: str) -> str:
    html_file_name = f"C:/Users/cmbruns/Documents/git/OpenXR-Registry/specs/1.0/man/html/{function_name}.html"
    parser = OpenXrDocstringParser(function_name)
    with open(html_file_name, "r") as fh:
        page = fh.read()
    parser.feed(page)
    return parser.docstring


def main():
    print(create_docstring("xrGetInstanceProcAddr"))


if __name__ == "__main__":
    main()
