from operator import index
from bs4 import BeautifulSoup
import requests 
import json

result = {
}

index = open("index.json")
data = json.load(index)

# print(data)

source=requests.get(data["Wipro"]["link"])
soup = BeautifulSoup(source.text, 'lxml')
price_div= soup.find('div', class_='stickymcont')
price= price_div.find('div', class_='pcstkspr nsestkcp bsestkcp futstkcp optstkcp')

print(price.text)