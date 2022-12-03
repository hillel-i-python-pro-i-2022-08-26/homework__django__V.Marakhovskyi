from django.contrib import messages
from django.db.models import Sum, Count
from django.views.generic import ListView

from apps.middleware_custom.models import ActionStatistic


class AllInfoView(ListView):
    model = ActionStatistic
    template_name = "middleware_custom/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All session info"
        # Get_useful_info__start
        action_instance = ActionStatistic.objects.all()
        sum_of_requests = ActionStatistic.objects.aggregate(Sum("count_of_visits"))
        qtty_of_pages = ActionStatistic.objects.aggregate(Count("path"))

        # Get_useful_info__stop
        context["object_list"] = action_instance
        context["sum_of_requests"] = sum_of_requests.get("count_of_visits__sum")
        context["qtty_o_pages"] = qtty_of_pages.get("path__count")

        return context


class ExactSessionView(ListView):
    model = ActionStatistic
    template_name = "middleware_custom/session_statistic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "exact session info"
        # Get_useful_info__start
        action_instance = ActionStatistic.objects.filter(session_key=self.request.session.session_key)
        sum_of_requests = action_instance.aggregate(Sum("count_of_visits"))
        qtty_of_pages = action_instance.aggregate(Count("path"))

        # Get_useful_info__stop
        context["object_list"] = action_instance
        context["sum_of_requests"] = sum_of_requests.get("count_of_visits__sum")
        context["qtty_o_pages"] = qtty_of_pages.get("path__count")

        return context


class ExactUserView(ListView):
    model = ActionStatistic
    template_name = "middleware_custom/user_statistic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "exact user info"
        # Get_useful_info__start
        if self.request.user.is_authenticated:
            action_instance = ActionStatistic.objects.filter(user=self.request.user.pk)
            sum_of_requests = action_instance.aggregate(Sum("count_of_visits"))
            qtty_of_pages = action_instance.aggregate(Count("path"))

            # Get_useful_info__stop
            context["object_list"] = action_instance
            context["sum_of_requests"] = sum_of_requests.get("count_of_visits__sum")
            context["qtty_o_pages"] = qtty_of_pages.get("path__count")
        else:
            context["title"] = "AAA"
            messages.warning(self.request, "For monitoring user statistic authorize first")
        return context
