#!/usr/bin/env python
import time
from zapv2 import ZAPv2
from pprint import pprint
import json
import time
url = 'http://localhost:3000/'
url = 'https://elearning.univ-guelma.dz/login/index.php'

apiKey = 'mypass123'
zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

zap.spider.set_option_max_depth(1)
#zap.spider.set_option_max_duration(2)
starter=time.time()
scanID = zap.spider.scan(url)
"""while int(zap.spider.status(scanID)) < 100:
    # Poll the status until it completes
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)
"""
while int(zap.spider.status(scanID)) < 100:
    time.sleep(2)
finished = time.time()

print("time is :{}",finished-starter)
# Prints the URLs the spider has crawled
print('\n'.join(map(str, zap.spider.results(scanID))))
# If required post process the spider results

# TODO: Explore the ajax way 
   #scanID = zap.ajaxSpider.scan(url)

   #timeout = time.time() + 60*2   # 2 minutes from now
# Loop until the ajax spider has finished or the timeout has exceeded
   #while zap.ajaxSpider.status == 'running':
       #if time.time() > timeout:
       #    break
       #time.sleep(2)
   #ajaxResults = zap.ajaxSpider.results(start=0, count=10)
#Disabling the passive scanner since we don't need them for now
   #zap.pscan.disable_all_scanners()

# TODO:
#passive attack
"""
import time
from pprint import pprint


# TODO : explore the app (Spider, etc) before using the Passive Scan API, Refer the explore section for details
while int(zap.pscan.records_to_scan) > 0:
    # Loop until the passive scan has finished
    print('Records to passive scan : ' + zap.pscan.records_to_scan)
    time.sleep(2)

print('Passive Scan completed')

# Print Passive scan results/alerts
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts())
"""
#active scan 
#"""

# TODO : explore the app (Spider, etc) before using the Active Scan API, Refer the explore section
   #scanID = zap.ascan.scan(url)
   #while int(zap.ascan.status(scanID)) < 100:
    # Loop until the scanner has finished
       #print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
       #time.sleep(5)

   #print('Active Scan completed')
# Print vulnerabilities found by the scanning
   #print('Hosts: {}'.format(', '.join(zap.core.hosts)))
   #print('Alerts: ')
#pprint(zap.core.alerts(baseurl=url))
#get the resaults:
  
   #with open('myresaults2.json', 'w') as convert_file:
   #     convert_file.write(json.dumps(zap.core.alerts(baseurl=url)))




