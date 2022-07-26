import logging
import sys
import traceback
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(settings.APPLICATION_NAME)

# Exception Logging middleware
class ExceptionAutoLoggingMiddleware(MiddlewareMixin):
    """
    This middleware provides logging of exception in requests.
    """
    def process_exception(self, request, exception):
        """
        Processes exceptions during handling of a http request.
        Logs them with *ERROR* level.
        """
        _, _, stacktrace = sys.exc_info()
        params = None
        if request and hasattr(request, 'method'):
            if request.method == "GET":
                params = request.GET
            elif request.method == "POST":
                params = request.POST

        logger.error(
  """%s [URL: %s].
  %s: %s
  Traceback:%s""",
            exception, request.path, request.method, params, ''.join(traceback.format_tb(stacktrace))
        )
        return None