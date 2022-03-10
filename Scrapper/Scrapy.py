import requests 
from bs4 import BeautifulSoup

global info_list
global nlp
info_list=[]
nlp=[]

def scrape_info(url): 
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    info_items = soup.find_all('div', class_='listing_content')
    for accommodations in info_items: 
        address = accommodations.find('p', class_='address')
        try: 
            if address is not None: 
                info_list.append([address.text])
                details = address.text
                i, a_phone = details.split('+', 1)
                a_name, a_location = i.split(', ', 1)
                nlp.append([a_name, a_location, a_phone])
        except: 
            pass
    print(nlp)
catgory = input("Enter Category name")
pageNum=["","-2","-3","-4"] 

for i in pageNum:
    scrape_info("https://www.nzdirectory.co.nz/"+str(catgory) +str(i)+".html")