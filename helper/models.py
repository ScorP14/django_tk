from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class AddColumQuerySetForModel:
    objects = models.QuerySet()


class BaseModel(models.Model):
    title = models.CharField('Название', max_length=50, primary_key=True, unique=True)
    slug = models.SlugField('url', blank=True, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.pk}'

    class Meta:
        abstract = True
