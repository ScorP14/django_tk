from django.db import models
from django.core.validators import validate_slug
from django.urls import reverse
from django.utils.text import slugify


class Substation(models.Model):
    view = models.CharField('Тип', max_length=250)
    number = models.CharField('Номер', max_length=50)
    city = models.CharField('Город', max_length=100)
    location = models.CharField('Расположение', max_length=250)

    def get_substation(self, **kwargs):
        tp = Substation.objects.filter(city=kwargs['city'], view=kwargs['substation_inside'], number=kwargs['number'])[0]


        # return render(request, 'tk/work_temp/work_temp.html', {'work_temp': work_temp})
        pass

    @staticmethod
    def filter_substation_for_city_view(**kwargs: str):
        search = Substation.objects.filter(city=kwargs['city'].lower())
        if 'substation_inside' in kwargs:
            search = search.filter(view=kwargs['substation_inside'].lower())
        return search

    def get_absolute_url(self):
        return reverse('tk:substation_url', kwargs={'city': self.city, 'substation_inside': self.view, 'number': self.number})

    def save(self, *args, **kwargs):
        self.view = slugify(self.view.lower(), allow_unicode=True)
        self.number = slugify(self.number.lower(), allow_unicode=True)
        self.city = slugify(self.city.lower(), allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.city.title()}, {self.view.upper()}-{self.number}'

    class Meta:
            ordering = ['city', 'substation_inside', 'number']
            verbose_name = 'Подстанция'
            verbose_name_plural = 'Подстанции'


class Photo(models.Model):
    slug = models.SlugField(max_length=250, validators=[validate_slug], unique=True)
    date = models.DateField('Дата снимка')
    number_photo = models.CharField('Номер снимка', max_length=10)
    view_ru = models.CharField('Тип РУ', max_length=15)
    cell = models.CharField('Узел', max_length=15)
    number_cell = models.CharField('Номер узла', max_length=15)
    element = models.CharField('Элемент', max_length=100, blank=True)
    defect_element = models.CharField('Дефектный элемент', max_length=100, blank=True)
    t0 = models.IntegerField('Темп. OC', default=0)
    ta = models.IntegerField('Темп. фазы - "А"', default=0)
    tb = models.IntegerField('Темп. фазы - "Б"', default=0)
    tc = models.IntegerField('Темп. фазы - "С"', default=0)
    result = models.CharField('Результат', max_length=250, blank=True)
    view_defect = models.CharField('Вид дефекта', max_length=50, blank=True)
    comment = models.TextField('Комментарий', blank=True)
    substation = models.ForeignKey(Substation, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.date}: {self.number_photo}'

    def save(self, *args, **kwargs):
        y, m, d = self.date.year, self.date.month, self.date.day
        self.slug = f'{self.number_photo}-{y}-{m}-{d}'
        print(self.slug)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date', 'number_photo']
        verbose_name = 'Снимок'
        verbose_name_plural = 'Снимки'




