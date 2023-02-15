from pprint import pprint
from zapv2 import ZAPv2
import json
import requests


target = 'http://localhost:3000/'
api_key="mypass123"
zap = ZAPv2(apikey=api_key, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})
zap.pscan.set_enabled(False)
"""zap.pscan.disable_all_scanners()
print("______________________________________________one+++++++++++++++++")
for i in zap.pscan.scanners:
     print(i['enabled']+"___"+  i['id'] +"__"+i['name'])"""
#print('Hosts: {}'.format(', '.join(zap.core.hosts)))
#print("zapkamla:",type(zap.core.alerts(baseurl=target)))
#print("gedah kayn:",len(zap.core.alerts(baseurl=target)))
#print("wahda mzap:",type(zap.core.alerts(baseurl=target)[0]))
#print("gedah kayn:",len(zap.core.alerts(baseurl=target)[0]))
#print(zap.core.alerts(baseurl=target)[0])
#print(zap.core.alerts(baseurl=target)[0]['alert'])
zap.ascan.disable_scanners(ids=[6])#Path Traversal
zap.ascan.disable_scanners(ids=[10045])#Source Code Disclosure - /WEB-INF folder
zap.ascan.disable_scanners(ids=[20015])#Heartbleed OpenSSL Vulnerability
zap.ascan.disable_scanners(ids=[20019])#External Redirect
zap.ascan.disable_scanners(ids=[90024])#Generic Padding Oracl
zap.ascan.disable_scanners(ids=[90034])#Cloud Metadata Potentially Exposed
zap.ascan.disable_scanners(ids=[30001])#Buffer Overflow
zap.ascan.disable_scanners(ids=[30002])# Format String Error

zap.ascan.disable_scanners(ids=[40008])#Parameter Tampering
zap.ascan.disable_scanners(ids=[40028])#ELMAH Information Leak
zap.ascan.disable_scanners(ids=[40029])# Trace.axd Information Leak
zap.ascan.disable_scanners(ids=[40032]) #.htaccess Information Leak
zap.ascan.disable_scanners(ids=[40034]) #.env Information Leak
zap.ascan.disable_scanners(ids=[40035]) #Hidden File Finder
zap.ascan.disable_scanners(ids=[90026]) #SOAP Action Spoofing
"""
print("______________________________________________one+++++++++++++++++")
for i in zap.ascan.scanners() :
    print (i['enabled']+"___"+  i['id'] +"__"+i['name'])
""" 
"""list of scanners
"""
"""
with open('myresaults2.json', 'w') as convert_file:
     convert_file.write(json.dumps(zap.core.alerts(baseurl=target)))
"""
