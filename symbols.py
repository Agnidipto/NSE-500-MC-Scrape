import csv
import json

index=open("index.json","r")
data=json.load(index)
index.close()
keys=data.keys()
# print(keys)
count=0

with open("ind_nifty500list.csv", "r") as csv_list:
    source=csv.reader(csv_list)
    header=next(source)
    if header != None:
        for row in source :
            # print(row[0].split(" Ltd.")[0])
            for eachkey in keys:
                if(eachkey==row[0].split(" Ltd.")[0]) :
                    data[eachkey]['symbol'] = row[2]
                    count+=1
            

jsoned = json.dumps(data, indent=4)
f = open("index.json", "w")
f.write(jsoned)
f.close()
