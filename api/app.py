from fastapi import FastAPI

from scrapers.viva_real import VivaReal

app = FastAPI()


@app.get("/viva-real")
async def all():
    scraper = VivaReal()
    units = scraper.get_housing_units()
    return {"message": [unit.asdict() for unit in units]}
