from bs4 import BeautifulSoup
import requests 
import json

result = {
}

url_file= open("url.txt", "r")
content = url_file.readlines()

for c_url in content:
    source= requests.get('https://www.moneycontrol.com/india/stockpricequote/'+c_url)
    soup = BeautifulSoup(source.text, 'lxml')
    price_div= soup.find('div', class_='stickymcont')
    price= price_div.find('div', class_='pcstkspr nsestkcp bsestkcp futstkcp optstkcp')
    x=c_url.split("\n")[0].split("/")
    result[''+x[1]+"/"+x[2]]=""+price.text
    
jsoned = json.dumps(result, indent=4)
print(jsoned)