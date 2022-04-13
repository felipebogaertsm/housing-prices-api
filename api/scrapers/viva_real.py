from bs4 import BeautifulSoup
import requests


from classes.data import Address, Price
from classes.housing import HousingUnit
from classes.source_website import SourceWebsite
from utils.format import only_numbers

BASE_URL = "https://www.vivareal.com.br/aluguel/"


class VivaReal(SourceWebsite):
    def __init__(self):
        super().__init__(BASE_URL, "Brazil")

        self.currency = "BRL"

    def get_housing_units(self):
        response = requests.get(BASE_URL)
        doc = BeautifulSoup(response.text, "html.parser")

        results_list = doc.find("div", {"class": "results-list"}).findChildren(
            "div", recursive=False
        )

        self.housing_units = []

        for item in results_list:
            price = item.find("div", {"class": "property-card__price"}).find("p").text
            price_value = float(only_numbers(price, decimal_separator=","))

            self.housing_units.append(
                HousingUnit(
                    address=Address(
                        area="",
                        city="",
                        country="",
                        postal_code="",
                        street="",
                    ),
                    price=Price(value=price_value, currency=self.currency),
                )
            )

        return self.housing_units
