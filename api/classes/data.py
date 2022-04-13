from dataclasses import dataclass


@dataclass
class Address:
    area: str
    city: str
    country: str
    postal_code: str
    street: str


@dataclass
class Price:
    value: float
    currency: float
