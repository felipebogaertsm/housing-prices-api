import numpy as np


class SourceWebsite:
    def __init__(self, base_url, country) -> None:
        self.base_url = base_url
        self.country = country

        self.housing_units = []

    def get_average_housing_price(self):
        return np.mean(np.array([unit.price.value for unit in self.housing_units]))
