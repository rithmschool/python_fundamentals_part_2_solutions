# Write a Python program that uses BeautifulSoup to go to https://news.google.com 
# and prints out all of the headlines on the page. 

# Then, write a function called find_headline_by_keyword which lets you search 
# through those headlines for keywords, and returns to you a list of all of the 
# headlines that match all the keywords you provide.

import urllib.request
from bs4 import BeautifulSoup

url = 'https://news.google.com'
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "html.parser")

titles = soup.select(".titletext")

headlines = [title.text for title in titles]

def find_headline_by_keyword(hlines, kwds):
	return [headline for headline in hlines if kwds.lower() in headline.lower()]

# Example usage: find_headline_by_keyword(headlines, "california")