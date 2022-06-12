from bs4 import BeautifulSoup
import requests 
import json


index= open("index.json", "r")
content=json.load(index)
index.close()
# print(content.keys())
for i in content.keys():
    source= requests.get(content[i]['link'])
    soup = BeautifulSoup(source.text, 'lxml')
    price_div= soup.find('div', class_='indimprice')
    symbol=price_div.find('input', id='bseid')['value']
    print(symbol)
    content[i]['symbol']=symbol

jsoned = json.dumps(content, indent=4)

f = open("index.json", "w")
f.write(jsoned)
f.close()
    

