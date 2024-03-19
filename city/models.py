from django.urls import reverse

from helper.models import AddColumQuerySetForModel, BaseModel


class City(AddColumQuerySetForModel, BaseModel):


    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def get_absolute_url(self):
        return reverse('city:get_one_url', kwargs={'slug': self.slug})


class View(AddColumQuerySetForModel, BaseModel):
    class Meta:
        verbose_name = 'Тип подстанции'
        verbose_name_plural = 'Типы подстанций'