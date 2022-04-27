from django.db import models

from accounts.models import User
from .object_abstract import ObjectAbstract


class Routine(ObjectAbstract):
    """ Routine model """

    name = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="routine_creator")

    class Meta:
        unique_together = ["name", "user"]

    def __str__(self):
        return str(self.name)
