#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
# from tkinter import *

url = 'https://pubmed.ncbi.nlm.nih.gov/'
get_url = requests.get(url)
get_text = get_url.text
soup = BeautifulSoup(get_text, 'html5lib')

div1=soup.find("ul", {"class": "items-list"})
div2 = div1.find_all_next()[0]
div3 = list(div2)[1]
print(div3.get_text())

# window = Tk()
# window.title('Top Trending Article On Pubmed')
# window.geometry('960x540')
# window.resizable(width = False, height = False)

# TopArticle = div3.get_text()

# label1 = Label(window, text = TopArticle, font = "TimesNewRoman 12")
# label1.pack()

# window.mainloop()