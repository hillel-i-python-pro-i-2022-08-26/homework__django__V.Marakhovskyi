import logging
from collections.abc import Callable


class SimpleLoggingMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info("Init")

    def __call__(self, request):
        self.logger.info("Before")
        response = self.get_response(request)
        self.logger.info("After")
        return response
