from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/"
#retrieve the data from URL
response = requests.get(url)

#parse the contents of the webpage
soup = BeautifulSoup(response.text, "html.parser")

#filter all the a tags from the parsed document
for link in soup.find_all("a"):
    print(link)