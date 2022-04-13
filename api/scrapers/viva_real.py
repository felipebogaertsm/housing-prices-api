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
        results_list = []

        i = 0
        response = requests.get(BASE_URL)
        while int(response.status_code / 100) == 2:  # status code in 200 range
            response = requests.get(BASE_URL, params={"pagina": i + 1})
            doc = BeautifulSoup(response.text, "html.parser")

            try:
                results_list.append(
                    doc.find("div", {"class": "results-list"}).findChildren(
                        "div", recursive=False
                    )
                )
            except AttributeError:  # if page not found error
                break

            i += 1

        self.housing_units = []

        for item in results_list:
            price = item.find("div", {"class": "property-card__price"}).find("p").text
            price_value = float(only_numbers(price, decimal_separator=","))

            address = item.find("span", {"class": "property-card__address"}).text
            address_split = address.split(" - ")
            address_street = address_split[0]
            address_area = address_split[1].split(", ")[0]
            address_city = address_split[1].split(", ")[1]

            self.housing_units.append(
                HousingUnit(
                    address=Address(
                        area=address_area,
                        city=address_city,
                        country=self.country,
                        postal_code="",
                        street=address_street,
                    ),
                    price=Price(value=price_value, currency=self.currency),
                )
            )

        return self.housing_units
