from django.db import models
from django.urls import reverse

from pytils.translit import slugify

from city.models import City
from helper.models import AddColumQuerySetForModel, BaseModel
from substation_type.models import SubstationType


class Substation(AddColumQuerySetForModel, models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    view = models.ForeignKey(SubstationType, on_delete=models.CASCADE)
    number = models.CharField('номер', max_length=50)
    slug = models.SlugField('url', blank=True, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.city}-{self.view}-{self.number}')
        tp = Substation.objects.all().filter(city=self.city, view=self.view, number=self.number).first()
        if self.pk is None and tp:
            return tp.get_absolute_url()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('substation:one', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'{self.city}:{self.view}-{self.number}'

    class Meta:
        ordering = ['city', 'view', 'number']
        verbose_name = 'Подстанция'
        verbose_name_plural = 'Подстанции'







