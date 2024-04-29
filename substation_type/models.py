from django.db import models

from helper.models import AddColumQuerySetForModel, BaseModel


# Create your models here.

class SubstationType(AddColumQuerySetForModel, BaseModel):
    class Meta:
        verbose_name = 'Тип подстанции'
        verbose_name_plural = 'Типы подстанций'
