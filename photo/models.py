from django.db import models

from substation.models import Substation


class Photo(models.Model):
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE)
    date = models.DateField('Дата снимка', auto_now_add=True)     
    number_photo = models.CharField('Номер снимка', max_length=10)     
    
    substation_type = models.CharField('Тип РУ', max_length=15)
    
    knot = models.CharField('Узел', max_length=15)
    number_cell = models.CharField('Номер узла', max_length=15)         

    complete = models.BooleanField(default=False)
    t_env = models.IntegerField('Темп. OC', default=0) 
    t_a = models.IntegerField('Темп. фазы - "А"', default=0)                                         
    t_b = models.IntegerField('Темп. фазы - "Б"', default=0)                                     
    t_c = models.IntegerField('Темп. фазы - "С"', default=0)
 
    comment = models.TextField('Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.date}: {self.number_photo}'

    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)           

    class Meta:                         
        ordering = ['-date', 'number_photo']
        verbose_name = 'Снимок'         
        verbose_name_plural = 'Снимки'
