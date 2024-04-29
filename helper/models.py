from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class AddColumQuerySetForModel:
    objects = models.QuerySet()


class BaseModel(models.Model):
    title = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('url', blank=True, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        import re
        class_name = self.__class__.__name__
        underscore_class_name = '_'.join(re.sub(r'([A-Z])', r' \1', class_name).lower().split())
        return reverse(f'{underscore_class_name}:one', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        abstract = True
