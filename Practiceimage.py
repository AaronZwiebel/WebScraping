from bs4 import BeautifulSoup
import requests
import urllib.request

search = input("what image would you like to search?")
url = "https://duckduckgo.com/?q=" + search + "&t=ffnt&iar=images&iax=images&ia=images"
print (url)
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
print(soup.prettify())
images = soup.find_all("a", attrs = {"alt": "post image"})
number = 0
while number <= 2:
    for image in images:
        image_src = image["src"]
        urllib.request.urlretrieve(image_src, str(number))
        number +=1