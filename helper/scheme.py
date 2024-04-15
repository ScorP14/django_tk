

import pydantic
from pydantic import field_validator

# from city.models import City


class AdapterCity(pydantic.BaseModel):
    title: str

    @field_validator('title')
    @classmethod
    def validate_title(cls, v: str) -> str:
        print(cls, v)
        return v.lower()

    # def get_from_model(self):
    #     City.objects.get(title=self.title)



c = AdapterCity(title='МосСКВА')
# print(c.get_from_model())