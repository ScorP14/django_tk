from django.db import models


class AddColumQuerySetForModel:
    objects = models.QuerySet()


class BaseModel(models.Model):
    title = models.CharField('Название', max_length=50, primary_key=True, unique=True)

    def __str__(self) -> str:
        return f'{self.pk}'

    class Meta:
        abstract = True


class City(AddColumQuerySetForModel, BaseModel):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class View(AddColumQuerySetForModel, BaseModel):
    class Meta:
        verbose_name = 'Тип подстанции'
        verbose_name_plural = 'Типы подстанций'