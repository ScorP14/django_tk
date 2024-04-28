from django.db.models import QuerySet
from django.urls import reverse

from helper.models import AddColumQuerySetForModel, BaseModel


class City(AddColumQuerySetForModel, BaseModel):

    def get_absolute_url(self):
        return reverse('city:one', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


