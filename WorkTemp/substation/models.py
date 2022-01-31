from django.db import models
#from django.core.validators import validate_slug
from django.urls import reverse
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField('Город', max_length=250, primary_key=True, unique=True)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.name = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class View(models.Model):
    name = models.CharField('Тип подстанции', max_length=250, primary_key=True, unique=True)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.name = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Substation(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    view = models.ForeignKey(View, on_delete=models.CASCADE)
    number = models.CharField('Номер', max_length=50)
    location = models.CharField('Расположение', max_length=250, null=True)
    
    objects = models.Manager()

    @staticmethod
    def get_sub(city, view, number):
        city = slugify(city, allow_unicode=True)
        view = slugify(view, allow_unicode=True)
        number = slugify(number, allow_unicode=True)
        return Substation.objects.get(city=city, view=view, number=number)


    @staticmethod
    def get_sub_for_city(city):
        city = slugify(city, allow_unicode=True)
        return Substation.objects.all().filter(city=city)


    @staticmethod
    def get_sub_for_view(view):
        view = slugify(view, allow_unicode=True)
        return Substation.objects.all().filter(view=view)

    def get_absolute_url(self):
        return reverse('substation:substation_url', kwargs={'city': self.city, 'view': self.view, 'number': self.number})

    def save(self, *args, **kwargs):
        self.number = slugify(self.number, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.city}:{self.view}-{self.number}'

    class Meta:  
        ordering = ['city', 'view', 'number']   
        verbose_name = 'Подстанция'         
        verbose_name_plural = 'Подстанции'
