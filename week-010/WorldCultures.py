"""
By Juan Peralta Web Scrapping Project: The followign script has the porpuse to learn a little bit more about each culture.

On first phase we are scrapping The World Cultures Encyclopedia to realize how many cultures and descritpions. 
"""
import requests
from bs4 import BeautifulSoup

class WorldCulturesScraper():
    # worldcultures = []
    # Urls = []
    # culture_countries = []
    # culture_desc = []
    # lst = []
    # countrs_n_descript = {}

    # def fetch(self, url):
    #     response = requests.get(url)
    #     return response

    # def parse(self, response, lst):
    #     content = BeautifulSoup(response, 'lxml')
    #     lst = content.findAll('h2')[2:]
    #     #return lst

    #     #cont = req.text
    #     # lst = soup.findAll('h2')[2:]
    worldcultures = []
    Urls = []
    culture_countries = []
    culture_desc = []
    lst = []
    countrs_n_descript = {}

    def run(self):
        url = "https://www.everyculture.com/"
        response = requests.get(url)

        content = BeautifulSoup(response, 'lxml')
        self.lst = content.findAll('h2')[2:]

        ### before the run

        #Get first level details and print them
       
        for item in self.lst:
            self.worldcultures.append(item.text)
            self.Urls.append(url+item.a['href'])

        # print(worldcultures)
        # print(Urls)

    #Get second level details from URLs collected in first level
        for u in self.Urls:
            response = requests.get(u)
            content = response.text
            sp = BeautifulSoup(content)
            h2s = sp.find_all('h2')
            descs = sp.find_all('p')
            for idx,h2 in enumerate(h2s):
                self.culture_countries.append(h2.text[1:-1])
                self.culture_desc.append(descs[idx].text)

        self.culture_countries
            #print(self.culture_desc)
        self.countrs_n_descript = {countr:dscript for kc,countr in enumerate(self.culture_countries[1:]) for kd,dscript in enumerate(self.culture_desc[1:]) \
            if kc == kd}
        # return self.countrs_n_descript

    
if __name__ == '__main__':
    webscraper = WorldCulturesScraper()
    webscraper.run()
