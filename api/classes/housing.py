from classes.data import Address, Price


class HousingUnit:
    def __init__(self, address: Address, price: Price) -> None:
        self.address = address
        self.price = price

    def __repr__(self):
        return f"{self.price.currency}{self.price.value}"
