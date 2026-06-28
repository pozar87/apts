import re
import logging
from importlib import resources

logger = logging.getLogger(__name__)

class ReportTemplateMixIn:
    NOTIFICATION_TEMPLATE = resources.files("apts").joinpath(
        "templates/notification.html.template"
    )

    def _load_template(self, custom_template) -> str:
        if custom_template:
            # Security: restrict to allowed template extensions and prevent path traversal.
            str_template = str(custom_template)
            if ".." in str_template:
                raise ValueError("Path traversal detected in custom template path.")

            if not str_template.lower().endswith((".template", ".html", ".htm")):
                raise ValueError(
                    "Only .template, .html, or .htm files are allowed as custom templates."
                )
            with open(custom_template, "r", encoding="utf-8") as f:
                return f.read()
        else:
            return self.NOTIFICATION_TEMPLATE.read_text(encoding="utf-8")

    def _inject_css(self, template_content: str, css: str) -> str:
        # Sanitize CSS to prevent breaking out of <style> block.
        sanitized_css = re.sub(r"</style\s*/?>", "", str(css), flags=re.IGNORECASE)
        # Escape '$' to '$$' to prevent string.Template from interpreting it as a variable.
        sanitized_css = sanitized_css.replace("$", "$$")
        style_end_pos = template_content.find("</style>")
        if style_end_pos != -1:
            return (
                template_content[:style_end_pos]
                + sanitized_css
                + template_content[style_end_pos:]
            )
        return template_content
