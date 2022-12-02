from django.views.generic import ListView

from apps.middleware_custom.models import SessionStatistic


class AllInfoView(ListView):
    model = SessionStatistic
    template_name = "middleware_custom/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All session info"
        # Get_useful_info__start
        session_handler = SessionStatistic.objects.all()
        # total_visits = session_handler.aggregate(Sum('count_of_visits'))
        # total_pages = session_handler.aggregate(Count('path'))
        # Get_useful_info__stop
        context["object_list"] = session_handler
        # context['total_visits'] = total_visits["count_of_visits__sum"]
        # context['count_of_visited_pages'] = total_pages["path__count"]

        return context


# Create your views here.
