from bs4 import BeautifulSoup
import requests

url = 'http://papertalks.org/p/e/default.aspx'
get_url = requests.get(url)
get_text = get_url.text
soup = BeautifulSoup(get_text, 'html5lib') #'html.parser')
# div = soup.div['class']
# find_all(soup, class = 'rDMtnd')
# soup1 = soup.find("yt-formatted-string")
# class="style-scope ytd-video-primary-info-renderer"
div1=soup.find('div', id = "LayoutRegion11LYR")
div1.find_all_next()[0]
print(div1.get_text())
# print(soup.title.name)
# print(soup.title.text)

# print(soup.p.text)

# for header in soup.find_all('h'):
#     print(header.text)

# print(soup.get_text())