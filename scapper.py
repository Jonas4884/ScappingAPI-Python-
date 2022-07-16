import json
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
            
        return qlist
        

#quotes = Scraper()

# quotes.scrapedata('emploi')





