"""HTML rendering strategy."""

from jinja2 import Environment, FileSystemLoader

from sv_doc.models.document import Documentation


class HtmlRenderer:
    """Render documentation to HTML."""

    file_loader = FileSystemLoader("./templates")
    env = Environment(loader=file_loader)

    def render(self, documentation: Documentation) -> str:
        data = {
            "title": "Documentation SystemVerilog",
            "sections": documentation.sections,
        }
        template = self.env.get_template("index.html")
        return template.render(data)
