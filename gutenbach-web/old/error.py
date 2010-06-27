import os.path

import paste.fileapp
import tg
from pylons.controllers.util import forward
from pylons.middleware import error_document_template, media_path

from sipbmp3web.lib.base import BaseController

class ErrorController(object):
    """Generates error documents as and when they are required.

    The ErrorDocuments middleware forwards to ErrorController when error
    related status codes are returned from the application.

    This behaviour can be altered by changing the parameters to the
    ErrorDocuments middleware in your config/middleware.py file.
    """

    @tg.expose('sipbmp3web.templates.error')
    def document(self, *args, **kwargs):
        """Render the error document"""
        resp = tg.request.environ.get('pylons.original_response')
        default_message = ("<p>We're sorry but we weren't able to process "
        " this request.</p>")
        values = dict(prefix=tg.request.environ.get('SCRIPT_NAME', ''),
                 code=tg.request.params.get('code', resp.status_int),
                 message=tg.request.params.get('message', default_message))
        return values
