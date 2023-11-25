import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import tldextract

# hiiii! owo (つ✧ω✧)つ let's ask the user for the kawaii url they wanna scrape~ nyaa! (*ฅ́˘ฅ̀*)♡
def get_valid_url():
    while True:
        url = input("uwu~! enter the super cute url you wanna extract links from: ")
        url = url.strip()  # Remove leading and trailing spaces

        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            # If no scheme is provided, add "https://" by default
            url = "https://" + url

        ext = tldextract.extract(url)
        if ext.suffix and ext.domain:
            return url
        else:
            print("aww, that's not a valid domain! (>_<) Please provide a complete URL with a valid top-level domain (TLD), like '.com' or '.net'. Teehee~")

# Keep asking for a valid URL until one is provided (´• ω •`)ﾉ💕
while True:
    # nya~ get a valid url from our adorable user! (^・ω・^ )
    url = get_valid_url()

    try:
        # time to fetch the super kawaii webpage! \(^ヮ^)/
        response = requests.get(url, timeout=10)  # Set a timeout of 10 seconds
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print("aww, it looks like that's an invalid URL or there was an issue fetching the page! (>_<) Please provide a valid URL.")
        # Continue to the next iteration of the while loop to ask for a valid URL again
        continue

    # check if the request was successful! (´∀｀*)ﾉ━☆ﾟ.*･｡ﾟ
    if response.status_code == 200:
        # let's create a super cute beautifulsoup object from the html content of the website. (＾◡＾)
        soup = BeautifulSoup(response.content, 'html.parser')

        # find all the precious links in the html content~! (´• ω •`)ﾉ💕
        links = soup.find_all('a')

        # now, let's sprinkle some magic and print out those links! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
        for link in links:
            # use urljoin to handle any tricky, mischievous relative urls~! (¬‿¬)
            print(urljoin(url, link.get('href')))
        
    else:
        print("aww, it looks like that's an invalid URL or there was an issue fetching the page! (>_<) Please provide a valid URL. Status Code:", response.status_code, "૮( ꒦ິ⍣꒦ິ )ა")
