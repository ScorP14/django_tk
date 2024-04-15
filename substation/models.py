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
        return reverse('substation:get_one_url', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'{self.city}:{self.view}-{self.number}'

    class Meta:
        ordering = ['city', 'view', 'number']
        verbose_name = 'Подстанция'
        verbose_name_plural = 'Подстанции'


'''
class Photo(models.Model):
    work_temp = models.ForeignKey(Substation, on_delete=models.PROTECT)
    date = models.DateField('Дата снимка')      
    number_photo = models.CharField('Номер снимка', max_length=10)                              
    view_ru = models.CharField('Тип РУ', max_length=15)
    cell = models.CharField('Узел', max_length=15) 
    number_cell = models.CharField('Номер узла', max_length=15)         
    element = models.CharField('Элемент', max_length=100, blank=True)                               
    defect_element = models.CharField('Дефектный элемент', max_length=100, blank=True)      
    # complete = True/False
    t0 = models.IntegerField('Темп. OC', default=0) 
    ta = models.IntegerField('Темп. фазы - "А"', default=0)                                         
    tb = models.IntegerField('Темп. фазы - "Б"', default=0)                                     
    tc = models.IntegerField('Темп. фазы - "С"', default=0)
    result = models.CharField('Результат', max_length=250, blank=True)  
    view_defect = models.CharField('Вид дефекта', max_length=50, blank=True)        
    comment = models.TextField('Комментарий', blank=True)                           



    def __str__(self):
        return f'{self.date}: {self.number_photo}'

    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)           

    class Meta:                         
        ordering = ['-date', 'number_photo']
        verbose_name = 'Снимок'         
        verbose_name_plural = 'Снимки'
'''

import pydantic
from pydantic import field_validator

class AdapterCity(pydantic.BaseModel):
    title: str


    @field_validator('title')
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()








class RepositoryCity:
    @staticmethod
    def validator(item: str) -> str:
        """Валидация данных
        Возможно, надо дополнить"""
        valid_item = item.lower()
        return valid_item

    @staticmethod
    def get_or_create(item: str) -> City:
        """Создание записи или ее получение"""
        return City.objects.get_or_create(title=RepositoryCity.validator(item))[0]

    @staticmethod
    def get(item: str) -> City:
        """Получение записи"""
        return City.objects.get(title=RepositoryCity.validator(item))


class RepositoryView:
    @staticmethod
    def validator(item: str) -> str:
        """Валидация данных"""
        valid_item = item.lower()
        print(f'{valid_item=})')
        return valid_item

    @staticmethod
    def get_or_create(item: str) -> View:
        """Создание записи или ее получение"""
        return View.objects.get_or_create(title=RepositoryView.validator(item))[0]

    def get(item: str) -> View:
        """Создание записи или ее получение"""
        return View.objects.get(title=RepositoryView.validator(item))


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
