import requests
import csv
from bs4 import BeautifulSoup

#Create a request 
req = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data')
#Create Beautiful soup object
soup = BeautifulSoup(req.text)

#Locate table
table = soup.find('tbody')
#Accumulate all rows to iterate through
rows = table.find_all('tr')

#Method to process data to remove puntuaction and calculate death and recover rate
def process_data(country, cases, deaths, recovered):
	C=-1 #Counter
	death_rate = None
	recover_rate = None
	if 'No data' in cases:
		cases = None
	else:
		cases = cases.replace(',','')
		cases = cases.replace('.','')
		cases = int(cases)
		C = cases
		if C == 0:
			return 0,0,0,0,0
	if 'No data' in deaths:
		deaths = None 
	else:
		deaths = deaths.replace(',','')
		deaths = deaths.replace('.','')
		deaths = int(deaths)
		if C!=0:
			death_rate = deaths/C
	
	if 'No data' in recovered:
		recovered = None 
	else:
		recovered = recovered.replace(',','')
		recovered = recovered.replace('.','')
		recovered = int(recovered)
		if C!=0:
			recover_rate = recovered/C
	return country, cases, deaths, recovered, death_rate, recover_rate

#create Output CSV file
with open('JuanPeralta-covid-report.csv', 'w+', newline = '') as csvfile:
	csvWriter = csv.writer(csvfile, delimiter = ',')
	csvWriter.writerow(['Country','Cases','Deaths', 'Recoveries', 'Death Rate', 'Recovery Rate'])

	#First row
	row = rows[1]
	theads = row.find_all('th')
	country = theads[1].text[:-4]
	cases = theads[2].text[:-1]
	deaths = theads[3].text[:-1]
	recovered = theads[4].text[:-1]

	country, cases, deaths, recovered, death_rate, recover_rate = process_data(country, cases, deaths, recovered)
	print(country, cases, deaths, recovered, death_rate, recover_rate)
	csvWriter.writerow([country, cases, deaths, recovered, death_rate, recover_rate])

#Iterate through table rows
	for row in rows[2:]:
		theader = row.find_all('th')
		tdata = row.find_all('td')
		#Using try/catch block to handle out of index exceptions after table ends
		try:
			country = theader[1].a.text
			cases = tdata[0].text[:-1]
			deaths = tdata[1].text[:-1]
			recovered = tdata[2].text[:-1]

			#handle dta types and missing values
			country, cases, deaths, recovered, death_rate, recover_rate = process_data(country, cases, deaths, recovered)
			print(country, cases, deaths, recovered, death_rate, recover_rate)

			#Write the row to csv file
			csvWriter.writerow([country, cases, deaths, recovered, death_rate, recover_rate])
		except:
			print('End of table reached')