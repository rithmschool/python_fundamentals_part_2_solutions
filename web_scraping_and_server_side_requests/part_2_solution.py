# https://en.wikipedia.org/wiki/United_States_presidential_election
# This Wikipedia page has a table with data on all of the US Presidential elections. 
# Our goal is to use Beautiful Soup to scrape some of this data into a CSV file. 
# The columns of the CSV should be: 
# 	order, 
#	year, 
#	winner,
#	winner electoral votes, 
#	runner-up, and 
#	runner-up electoral votes. 
# Use commas as the delimiter.

import urllib.request
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/United_States_presidential_election'
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "html.parser")

table_rows = soup.select(".wikitable")[0].select("tr")

csv_data = [['order', 'year', 'winner', 'winner electoral votes', 'runner-up', 'runner-up electoral votes']]
for row in table_rows[1:]:
	tds = row.select('td')
	order = tds[0].text
	year = tds[1].select("a")[0].text
	winner = tds[2].select("a")[0].text
	votes = tds[2].text.split("–")[1].strip().split(" ")[0]
	loser = tds[3].select("a")[0].text.split("(")[0].strip()
	loser_votes = tds[3].text.split('\n')[0].split("–")[1].strip().split(" ")[0]
	csv_data.append([order, year, winner, votes, loser, loser_votes])

with open('elections.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data) 	