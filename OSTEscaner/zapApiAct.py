from pprint import pprint
from zapv2 import ZAPv2
import json

target = 'http://localhost:3000/'
api_key="mypass123"
zap = ZAPv2(apikey=api_key, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

#zap.pscan.disable_all_scanners()
#for i in zap.pscan.scanners:
    # print(i)
#print('Hosts: {}'.format(', '.join(zap.core.hosts)))
#print("zapkamla:",type(zap.core.alerts(baseurl=target)))
#print("gedah kayn:",len(zap.core.alerts(baseurl=target)))
#print("wahda mzap:",type(zap.core.alerts(baseurl=target)[0]))
#print("gedah kayn:",len(zap.core.alerts(baseurl=target)[0]))
#print(zap.core.alerts(baseurl=target)[0])
#print(zap.core.alerts(baseurl=target)[0]['alert'])
""" list of scanners
for i in zap.ascan.scanners() :
    print (i)
"""
"""
with open('myresaults2.json', 'w') as convert_file:
     convert_file.write(json.dumps(zap.core.alerts(baseurl=target)))
"""
