from django.db import models

from helper.models import AddColumQuerySetForModel, BaseModel


class Knot(AddColumQuerySetForModel, BaseModel):
    class Meta:
        verbose_name = 'Узел'
        verbose_name_plural = 'Узлы'
