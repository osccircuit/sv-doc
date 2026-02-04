"""HTML rendering strategy placeholder."""

from sv_doc.interfaces import Renderer
from sv_doc.models.document import Documentation


class HtmlRenderer(Renderer):
    """Render documentation to HTML (placeholder)."""

    def render(self, documentation: Documentation) -> str:
        raise NotImplementedError
