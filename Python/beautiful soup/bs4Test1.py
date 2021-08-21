from bs4 import BeautifulSoup
import requests

url = "http://www.scottgames.com/"
# url = "https://www.youtube.com"
get_url = requests.get(url)
get_text = get_url.text
soup = BeautifulSoup(get_text, 'html5lib')

# script = soup.find_all("script")
all_stuff = soup.find_all('p')[0]
for link in str(all_stuff):
    print(link.get('src'))
# print(all_stuff)

body = soup.find("body")
p = body.find("p")
image = soup.body.string

# print(image_link)