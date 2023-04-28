import requests
from bs4 import BeautifulSoup

# specify the url of the website you want to extract links from
url = 'https://www.example.com'

# make a GET request to the website
response = requests.get(url)

# create a BeautifulSoup object from the website's HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# find all the links in the HTML content
links = soup.find_all('a')

# print all the links
for link in links:
    print(link.get('href'))
