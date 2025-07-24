'''https://www.langchain.com/langchain

https://www.langchain.com/customers

https://www.langchain.com/about'''

import threading as td
import requests
from bs4 import BeautifulSoup
urls=['https://www.langchain.com/langchain',

'https://www.langchain.com/customers',

'https://www.langchain.com/about']
def fetch(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(soup.text)
x=[]

for i in urls:
    thread=td.Thread(target=fetch,args=(i,))
    x.append(thread)
    thread.start()


for thread in x:

    thread.join()

print("All web pages fetched")
