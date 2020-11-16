import requests, csv
from bs4 import BeautifulSoup

site = 'https://ballotpedia.org/Electoral_College'
req = requests.get(site).content

soup = BeautifulSoup(req)

#Locate Table
table = soup.find(class_="marqueetable")

#tables = soup.find("tr", class_="marqueetable").contents[0]

#Accumulate all rows to iterate through
rows = table.find_all("tr")
data = table.find_all("td")

#create Output CSV file
with open('JuanPeralta-ElectorColleges.csv', 'w+', newline = '') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter = ',')
	# csvWriter.writerow(['States','Electors'])
    csvWriter.writerow(['States','Electors'])
    

    #First row
    row = rows[1]
    theads = row.find_all('th')
    # theads = row.find_all('th')
    heads = theads[0].text[:-1]
    states = rows[2].text[:9] #rows[2].text[:-4]
    electors = data[1].text[:9]

    print("States", "Electors")
    #csvWriter.writerow([state, elect])
    
    # #Iterate through table rows
    for row in rows[1:]:
        tdata = row.find_all('td')
        # heads = theads[0].text[:-1]
        # states = rows[2].text[:9] #rows[2].text[:-4]
        # electors = data[1].text[:9]
        data = row
        #headers = theads[1:-1].contents[0]
    
        try:
    # #Using try/catch block to handle out of index exceptions after table ends
            state =  tdata[0].text[:]
            elect =  tdata[1].text[:]
            print(state, elect)


            #Write the row to csv file
            #csvWriter.writerow([state, elect])
            csvWriter.writerow([state, elect])
        except:
            None
    
if __name__ == '__main__':
    print("Elector Colleges completed")