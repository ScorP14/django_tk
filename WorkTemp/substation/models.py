from django.db import models
# from django.core.validators import validate_slug
from django.urls import reverse
from django.utils.text import slugify

from transliterate import translit





class City(models.Model):
    title = models.CharField('Название', max_length=250, primary_key=True, unique=True)

    # def save(self, *args, **kwargs):
    #     self.title = slugify(self.title, allow_unicode=True)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class View(models.Model):
    title = models.CharField('Название', max_length=250, primary_key=True, unique=True)
    #
    # def save(self, *args, **kwargs):
    #     self.title = slugify(self.title, allow_unicode=True)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Тип подстанции'
        verbose_name_plural = 'Типы подстанций'


class Substation(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    view = models.ForeignKey(View, on_delete=models.CASCADE)
    number = models.CharField('Номер', max_length=50)
    location = models.CharField('Расположение', max_length=250, null=True)

    @staticmethod
    def get_sub(city, view, number):
        city = slugify(city, allow_unicode=True)
        view = slugify(view, allow_unicode=True)
        number = slugify(number, allow_unicode=True)
        return Substation.objects.get(city=city, view=view, number=number)

    #
    # def get_absolute_url(self):
    #     return reverse('substation:search_url', kwargs={'city': self.city, 'view': self.view, 'number': self.number})
    #
    # def save(self, *args, **kwargs):
    #     self.number = slugify(self.number, allow_unicode=True)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.city}:{self.view}-{self.number}'

    class Meta:
        ordering = ['city', 'view', 'number']
        verbose_name = 'Подстанция'
        verbose_name_plural = 'Подстанции'



class RepositorySubstation:
    @staticmethod
    def get_sub_for_city(city, transle=None):
        if transle is None:
            city = slugify(city, allow_unicode=True)
            return Substation.objects.all().filter(city=city)

    @staticmethod
    def get_sub_for_view(view):
        view = slugify(view, allow_unicode=True)
        return Substation.objects.all().filter(view=view)