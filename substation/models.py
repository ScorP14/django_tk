from django.db import models
from django.db.models import QuerySet
from django.urls import reverse
# from django.core.validators import validate_slug

from pytils.translit import slugify

from city.models import City, View


class AddColumQuerySetForModel:
    objects = models.QuerySet()

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

class RepositoryCity:
    @staticmethod
    def validator(item: str) -> str:
        """Валидация данных"""
        valid_item = item.lower()
        return valid_item

    @staticmethod
    def get_or_create(item: str) -> City:
        """Создание записи или ее получение"""

        return City.objects.get_or_create(title=RepositoryCity.validator(item))[0]

    @staticmethod
    def get(item: str) -> City:
        """Создание записи или ее получение"""
        print(item, RepositoryCity.validator(item))
        return City.objects.get(title=RepositoryCity.validator(item))


class RepositoryView:
    @staticmethod
    def validator(item: str) -> str:
        """Валидация данных"""
        valid_item = item.lower()
        return valid_item

    @staticmethod
    def get_or_create(item: str) -> View:
        """Создание записи или ее получение"""
        return View.objects.get_or_create(title=RepositoryView.validator(item))[0]


class RepositorySubstation:
    @staticmethod
    def get_all_substation_from_city(city: str) -> QuerySet:
        """Возвращает QuerySet всех подстанций в городе(city)"""
        city = RepositoryCity.get(city)
        return Substation.objects.all().filter(city=city)
