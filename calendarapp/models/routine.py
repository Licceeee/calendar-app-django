from django.db import models
from datetime import datetime, date

from accounts.models import User
from .object_abstract import ObjectAbstract


class Routine(ObjectAbstract):
    """ Routine model """

    name = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="routine_creator")

    class Meta:
        unique_together = ["name", "user"]
        ordering = ['-id']

    def __str__(self):
        return str(self.name)


class DailyRoutine(ObjectAbstract):
    """ Daily Routine model """

    date = models.DateField(default=datetime.now, unique=True)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["date", "routine"]
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} - {self.routine.name}"
