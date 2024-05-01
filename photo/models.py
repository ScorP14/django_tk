from django.db import models
from django.urls import reverse
from django.utils import timezone

from knot.models import Knot
from substation.models import Substation
from switchgear.models import Switchgear


class Photo(models.Model):
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE, verbose_name='Подстанция')
    date = models.DateField('Дата снимка', default=timezone.now)
    number_photo = models.CharField('Номер снимка', max_length=10)

    switchgear = models.ForeignKey(Switchgear, on_delete=models.CASCADE, verbose_name='Распределительное устройство')

    knot = models.ForeignKey(Knot, on_delete=models.CASCADE, verbose_name='Узел')
    number_cell = models.CharField('Номер узла', max_length=15)

    complete = models.BooleanField(default=False, verbose_name='Статус выполнения')
    t_env = models.IntegerField('Темп. OC', default=0)
    t_a = models.IntegerField('Темп. фазы - "А"', default=0)
    t_b = models.IntegerField('Темп. фазы - "Б"', default=0)
    t_c = models.IntegerField('Темп. фазы - "С"', default=0)

    comment = models.TextField('Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.date}: {self.number_photo}'

    def get_absolute_url(self):
        return reverse('photo:one', kwargs={'pk': self.pk})


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date', 'number_photo']
        verbose_name = 'Снимок'
        verbose_name_plural = 'Снимки'
