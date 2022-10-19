import datetime
import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

KEY__COUNT_OF_VISITS = "num_visits"


def session_view(request: HttpRequest) -> HttpResponse:
    num_visits = request.session.get(KEY__COUNT_OF_VISITS, 0)
    request.session[KEY__COUNT_OF_VISITS] = num_visits + 1

    json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)

    date_time = request.session.get("date_time", json.dumps(datetime.datetime.now()))
    request.session["date_time"] = json.dumps(datetime.datetime.now())

    return render(
        request,
        "session_info/index.html",
        {
            "session_id": request.session.session_key,
            "num_visits": num_visits,
            "date_time": date_time,
            "title": "Session info",
        },
    )


# Create your views here.
