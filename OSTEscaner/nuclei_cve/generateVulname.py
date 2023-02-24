import json 
tester={}
data =[]
with open("cves.json") as f:
        for line in f:
           # print(line)
            data.append(json.loads(line))

        for i in data : 
           tester[i['Info']['Name']]=0
for i in  tester.keys():
 print(i)
	
