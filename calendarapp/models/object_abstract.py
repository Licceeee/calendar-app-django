from django.db import models


class ObjectAbstract(models.Model):
    """ Object abstract model """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
