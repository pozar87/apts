import logging
from string import Template
from typing import Optional

from ...i18n import language_context
from .templates import ReportTemplateMixIn
from .data import ReportDataMixIn

logger = logging.getLogger(__name__)

class HtmlExportMixIn(ReportTemplateMixIn, ReportDataMixIn):
    def to_html(
        self,
        custom_template=None,
        css=None,
        language: Optional[str] = None,
    ):
        with language_context(language):
            template_content = self._load_template(custom_template)
            if css:
                template_content = self._inject_css(template_content, css)

            template = Template(template_content)
            data = self._prepare_html_data(language)
            return str(template.substitute(data))
