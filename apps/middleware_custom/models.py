from django.db import models


class ActionStatistic(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    session_key = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    count_of_visits = models.IntegerField()
    time_of_visit = models.DateTimeField(auto_now=True)

    class Meta:
        # db_table = 'ActionStatistic'
        constraints = [models.UniqueConstraint(fields=["session_key", "path", "user"], name="unique visit")]
