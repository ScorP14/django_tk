from helper.models import AddColumQuerySetForModel, BaseModel


class City(AddColumQuerySetForModel, BaseModel):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


