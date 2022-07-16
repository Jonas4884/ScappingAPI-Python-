from fastapi import FastAPI
import asyncio
import uvicorn
from typing import List
from pydantic import Json
from requests_html import HTMLSession;

class Scraper():
    def scrapedata(self,tag ):
        url = f'https://www.portaljob-madagascar.com/emploi/liste/secteur/informatique-web/page/{tag}'
        s = HTMLSession()
        ro = s.get(url)
        quotes = ro.html.find('aside.contenu_annonce')
        qlist = []
        
        for q in quotes:
            item = {
                
            'text':q.find('strong',first = True).text.strip(),
            'title': q.find('h4',first = True).text.strip(),
            'Contrat':q.find('h5',first= True).text.strip(),
            'description':q.find('a.description',first = True).text.strip(),
            'image':q.find('img',first = True)
            }
            
            qlist.append(item)
            print(qlist)
        return qlist
async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())

app = FastAPI()
quotes = Scraper()
@app.get("/{param}")
async def main(param):
    return quotes.scrapedata(param)

