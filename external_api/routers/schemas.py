from pydantic import BaseModel


class Cadastral(BaseModel):
    cadastral_number: str
    latitude: float
    longitude: float
