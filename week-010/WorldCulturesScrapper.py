# set up your scraping below
import requests
from bs4 import BeautifulSoup

class WorldCulturesScraper():
    
    def scrape(self):
        worldcultures = []
        Urls = []
        culture_countries = []
        culture_desc = []

        url = "https://www.everyculture.com/"
        req = requests.get(url)
        cont = req.text
        soup = BeautifulSoup(cont, 'lxml')
        lst = soup.findAll('h2')[2:]

        #Get first level details and print them
        for item in lst:
            worldcultures.append(item.text)
            Urls.append(url+item.a['href'])

        #Get second level details from URLs collected in first level
        for u in Urls:
            response = requests.get(u)
            content = response.text
            sp = BeautifulSoup(content,'lxml')
            h2s = sp.find_all('h2')
            descs = sp.find_all('p')
            for idx,h2 in enumerate(h2s):
                culture_countries.append(h2.text[1:-1])
                culture_desc.append(descs[idx].text)

        countrs_n_descript = {countr:dscript for kc,countr in enumerate(culture_countries[1:]) for kd,dscript in enumerate(culture_desc[1:]) \
                    if kc == kd}
        print(countrs_n_descript)

# this `main` function should run your scraping when 
# this script is ran.
        # db.drop_all()
        # db.create_all()
        # for key,val in countrs_n_descript.items():
        #     new_row = DBTable(country=key, description=val)
        #     print(new_row)
        #     db.session.add(new_row)
        #     db.session.commit()    

    #return rows
if __name__ == '__main__':
    webscraper = WorldCulturesScraper()
    webscraper.scrape()