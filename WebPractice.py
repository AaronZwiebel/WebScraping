from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.google.com/")
print(result)
print(result.headers)
src = result.content
print(src)
#soup = BeautifulSoup(src,'lxml')
url = "https://en.wikipedia.org/wiki/Wabbit_Twouble#In_popular_culture"
try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")
content = []
for li in content_lis:
    content.append(li.getText().split('/n')[0])