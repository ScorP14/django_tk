from django.db import models

from helper.models import AddColumQuerySetForModel, BaseModel


# Create your models here.
class Switchgear(AddColumQuerySetForModel, BaseModel):
    class Meta:
        verbose_name = 'Распределительное устройство'
        verbose_name_plural = 'Распределительные устройства'
