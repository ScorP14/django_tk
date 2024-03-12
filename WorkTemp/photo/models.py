from django.db import models
from django.core.validators import validate_slug
from django.urls import reverse 
from django.utils.text import slugify

from substation.models import Substation


class Photo(models.Model):
    substation = models.ForeignKey(Substation, on_delete=models.PROTECT)
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
