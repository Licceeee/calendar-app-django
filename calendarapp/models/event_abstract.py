from django.db import models
from .object_abstract import ObjectAbstract


class EventAbstract(ObjectAbstract):
    """ Event abstract model """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
