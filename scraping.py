from bs4 import BeautifulSoup
import requests
import urllib.request
import re
practice = ("https://en.wikipedia.org/wiki/Wabbit_Twouble#In_popular_culture")
try:
    page = urllib.request.urlopen(practice)
except:
    print("An error occured.")
soup = BeautifulSoup(page, 'html.parser')
regex = re.compile('^tocsection-')
content_lis = soup.find_all('li', attrs={'class': regex})
print(content_lis)
organized = BeautifulSoup(soup, 'html.parser')
print(organized.prettify())