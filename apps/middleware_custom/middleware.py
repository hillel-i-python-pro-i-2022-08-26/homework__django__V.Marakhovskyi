import logging
from collections.abc import Callable

from django.core.handlers.wsgi import WSGIRequest

from apps.middleware_custom.models import ActionStatistic


class AllRequestLoggingMiddleware:
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

        action_instance = ActionStatistic.objects.filter(
            session_key=request.session.session_key, path=request.path
        ).first()

        if action_instance is not None:
            count_of_visits = action_instance.count_of_visits + 1
        else:
            count_of_visits = 1

        user = request.user if request.user.is_authenticated else None

        defaults = {"count_of_visits": count_of_visits, "user": user}
        try:
            action_instance = ActionStatistic.objects.get(session_key=request.session.session_key, path=request.path)
            for key, value in defaults.items():
                setattr(action_instance, key, value)
            action_instance.save()
        except ActionStatistic.DoesNotExist:
            if not request.session.session_key:
                request.session.save()
            new_values = {"session_key": request.session.session_key, "path": request.path} | defaults
            action_instance = ActionStatistic(**new_values)
            action_instance.save()

        return response
