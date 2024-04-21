from django.db import models
from django.db.models import QuerySet
from django.urls import reverse


from pytils.translit import slugify

from city.models import City, View
from helper.models import AddColumQuerySetForModel


class Substation(AddColumQuerySetForModel, models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    view = models.ForeignKey(View, on_delete=models.CASCADE)
    number = models.CharField('номер', max_length=50)
    slug = models.SlugField('url', blank=True, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.city}-{self.view}-{self.number}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('substation:get_one', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'{self.city}:{self.view}-{self.number}'

    class Meta:
        ordering = ['city', 'view', 'number']
        verbose_name = 'Подстанция'
        verbose_name_plural = 'Подстанции'


class RepositorySubstation:
    @staticmethod
    def get_all_substation_from_city(city: str) -> QuerySet:
        """Возвращает QuerySet всех подстанций в городе(city)"""
        city = RepositoryCity.get(city)
        return Substation.objects.all().filter(city=city).order_by('city')

    @staticmethod
    def get_or_none(city: str, view: str, number: str) -> Substation:
        """Возвращает тп"""

        city = RepositoryCity.get(city)
        view = RepositoryView.get(view)
        try:
            tp = Substation.objects.get(city=city, view=view, number=number)
            return tp
        except models.ObjectDoesNotExist as e:
            print(e, 'Ошибка')
            return False
