from bs4 import BeautifulSoup
import requests

# url = "https://www.le.ac.uk/oerresources/bdra/html/page_09.htm"
# get_url = requests.get(url)
# get_text = get_url.text
# soup = BeautifulSoup(get_text, 'html.parser')

# div = soup.find("div", {"id": "main-content-withtoc"})
# p1 = div.find_all("p", {"class": "bodycopy"})
# p2 = list(p1)[1]
# print(p2.get_text())

url = "https://svue.itsryan.org/dashboard#gradebook"
get_url = requests.get(url)
get_text = get_url.text
soup = BeautifulSoup(get_text, 'html.parser')

print(soup)
# classes = soup.find('div', id_="v-gradeList")
# print(classes)
# for grade in classes:
#     print(grade.text(class_='right lg bw'))

# url = "https://markets.businessinsider.com/indices/world-stock-markets"
# get_url = requests.get(url)
# get_text = get_url.text
# soup = BeautifulSoup(get_text, 'html.parser')
# body = soup.find('tbody')

# print(body.find_all('td'))