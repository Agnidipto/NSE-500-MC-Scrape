import requests
from bs4 import BeautifulSoup
import json

result={}

source= open("mc.html", encoding="utf8")
soup=BeautifulSoup(source,'lxml')
# table_data=soup.find_all('div', id='indicesTableData')
# print(table_data[0].prettify())
table_content=soup.find_all('tr')

for r in table_content:
    td=r.find_all('td')
    # print(td.text)
    g=td[0].a['href'].split("/")[6]
    result[td[0].text] = { 'link': td[0].a['href'], 'type':td[1].text, 'id' : g}


jsoned = json.dumps(result, indent=4)
print(jsoned)

f = open("index.json", "w")
f.write(jsoned)
f.close()


