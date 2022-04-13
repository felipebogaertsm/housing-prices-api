from scrapers.viva_real import VivaReal

if __name__ == "__main__":
    viva_real = VivaReal()
    viva_real.get_housing_units()
    average_prices = viva_real.get_average_housing_price()
