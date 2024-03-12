from django.db import models
from django.db.models import QuerySet
# from django.core.validators import validate_slug
from django.urls import reverse
from pytils.translit import slugify


class AddColumQuerySetForModel:
    objects = models.QuerySet()


class BaseModel(AddColumQuerySetForModel, models.Model):
    title = models.CharField('Название', max_length=50, primary_key=True, unique=True)

    def __str__(self) -> str:
        return f'{self.pk}'

    class Meta:
        abstract = True


class City(BaseModel):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class View(BaseModel):
    class Meta:
        verbose_name = 'Тип подстанции'
        verbose_name_plural = 'Типы подстанций'


class Substation(AddColumQuerySetForModel, models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    view = models.ForeignKey(View, on_delete=models.CASCADE)
    number = models.CharField('Номер', max_length=50)
    slug = models.SlugField('Читаймый URL', blank=True, null=False)
    location = models.CharField('Расположение', max_length=250, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.city}-{self.view}-{self.number}')
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('substation:search_url', kwargs={'city': self.city, 'view': self.view, 'number': self.number})

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

        city = City.objects.get(pk=city)
        # print(Substation.objects.all().filter(city=city))
        for i in Substation.objects.all():
            print(i)
        return
