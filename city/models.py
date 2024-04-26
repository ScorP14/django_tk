from django.db.models import QuerySet
from django.urls import reverse

from helper.models import AddColumQuerySetForModel, BaseModel


class City(AddColumQuerySetForModel, BaseModel):

    def get_absolute_url(self):
        return reverse('city:one', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class View(AddColumQuerySetForModel, BaseModel):
    class Meta:
        verbose_name = 'Тип подстанции'
        verbose_name_plural = 'Типы подстанций'


class ValidatorCity:
    @staticmethod
    def validator_title(item: str) -> str:
        """Валидация данных Возможно, надо дополнить"""
        valid_item = item.lower()
        return valid_item


class RepositoryCity:

    @staticmethod
    def get(city: City | str) -> City:
        """Получение записи"""
        return City.objects.get(title=city)

    @staticmethod
    def create(city: str) -> City:
        return City.objects.get_or_create(title=ValidatorCity.validator_title(city))[0]

    @staticmethod
    def delete(city: str | City) -> None:
        match city:
            case City():
                city.delete()
            case str():
                RepositoryCity.get(city=ValidatorCity.validator_title(city)).delete()

    @staticmethod
    def get_all() -> QuerySet:
        return City.objects.all()


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