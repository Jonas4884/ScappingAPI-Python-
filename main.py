from fastapi import FastAPI
from scapper import Scraper
from fastapi import FastAPI
import asyncio
import uvicorn

async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())

app = FastAPI()
quotes = Scraper()
@app.get("/{param}")
async def read_item(param):
    return quotes.scrapedata(param)

