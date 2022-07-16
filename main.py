from fastapi import FastAPI
from scapper import Scraper
from fastapi import FastAPI

app = FastAPI()
quotes = Scraper()
@app.get("/{param}")
async def read_item(param):
    return quotes.scrapedata(param)

