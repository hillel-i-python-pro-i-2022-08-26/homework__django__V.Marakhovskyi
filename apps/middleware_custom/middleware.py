import logging
from collections.abc import Callable

from django.core.handlers.wsgi import WSGIRequest

from apps.middleware_custom.models import SessionStatistic


class SimpleLoggingMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info("Initialized server")

    def __call__(self, request: WSGIRequest):
        # Get_user_session__start
        if not request.session.session_key:
            request.session.save()
        # Get_user_session__stop

        http_message_for_logger = f"Path:{request.path} - User:{request.user} - Session:{request.session.session_key}"

        # Get_response__start
        self.logger.info("----------------Before-----------------")
        self.logger.info(http_message_for_logger)
        response = self.get_response(request)
        self.logger.info("________________After____________________")
        self.logger.info(http_message_for_logger)
        # Get_response__stop

        visit_handler = SessionStatistic.objects.filter(
            session_key=request.session.session_key, path=request.path
        ).first()

        if visit_handler is not None:
            count_of_visits = visit_handler.count_of_visits + 1
        else:
            count_of_visits = 1

        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        defaults = {"count_of_visits": count_of_visits, "user": user}
        try:
            visit_handler = SessionStatistic.objects.get(session_key=request.session.session_key, path=request.path)
            for key, value in defaults.items():
                setattr(visit_handler, key, value)
            visit_handler.save()
        except SessionStatistic.DoesNotExist:
            if not request.session.session_key:
                request.session.save()
            new_values = {"session_key": request.session.session_key, "path": request.path}
            new_values.update(defaults)
            visit_handler = SessionStatistic(**new_values)
            visit_handler.save()

        return response
