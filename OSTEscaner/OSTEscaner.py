import os 
import subprocess
import threading
import time
import json
from zapv2 import ZAPv2
from pprint import pprint
from bs4 import BeautifulSoup 
#___________________________________________creat_resaults_folder ______________________
name = "JucyShope2"
url ="http://localhost:3000/rest/product/search?q="
try:
    os.makedirs("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/"+name)
    os.makedirs("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/"+name+"/"+"wapiti")
    os.makedirs("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/"+name+"/"+"nuclei")
    os.makedirs("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/"+name+"/"+"owaspzap")
    os.makedirs("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/"+name+"/"+"skipfish")
    os.makedirs("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/"+name+"/"+"nikto")
except OSError as error:
    print("Error creating The Resault folder foor {}: {}".format(name,error))
    #to do : if this errour messege occured you need make new name because this file already exist wiche means you will have problem in skip fish probebly more.

#__________________________________________Wapiti_________________________________________________________
wapiti_vulnerabilities= {
    "Backup file": 0,
    "Blind SQL Injection": 0,
    "Weak credentials": 0,
    "CRLF Injection": 0,
    "Content Security Policy Configuration": 0,
    "Cross Site Request Forgery": 0,
    "Potentially dangerous file": 0,
    "Command execution": 0,
    "Path Traversal": 0,
    "Htaccess Bypass": 0,
    "HTTP Secure Headers": 0,
    "HttpOnly Flag cookie": 0,
    "Open Redirect": 0,
    "Secure Flag cookie": 0,
    "SQL Injection": 0,
    "Server Side Request Forgery": 0,
    "Cross Site Scripting": 0,
    "XML External Entity": 0  }

def get_wapiti_resaults(name):    # Opening JSON file
    f = open("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/wapiti/{}.json".format(name,name))
    data = json.load(f)
    wapiti_resaults=wapiti_vulnerabilities.copy()
    for vul in data["vulnerabilities"]:
        
    	wapiti_resaults[vul]=len(data["vulnerabilities"][vul])

    f.close()
    return wapiti_resaults

def start_wapiti(url,name):
      print("wapiti scan started:")
      output = subprocess.run("wapiti -u {} -f json -o /home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/wapiti/{}.json -l 2 --flush-session".format(url,name,name), shell=True, capture_output=True)

      print("wapiti Scann Finished ")
def start_wapiti_readReport():
      global wapiti_resaults
      start_wapiti(url,name)
      wapiti_resaults= get_wapiti_resaults(name)
      after_it_finished()
def after_it_finished():
     print("______________________________WApiti Resaults:_________________________")
     print(wapiti_resaults)
starting_wapiti = threading.Thread(target=start_wapiti_readReport)
#starting_wapiti.start() 
#___________________________________________SKIPFISH________________________________________

def start_skipfish(url,name):

        print("skipfish scan started:")
        output = subprocess.run("skipfish -L -W- -e -v -u -o  /home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/skipfish/{} {} ".format(name,name,url), shell=True, capture_output=True)
        print("skipfish scand finished ")
Type_of_issue={

  "10101": ["SSL certificate issuer information",0],
  "10201": ["New HTTP cookie added",0],
  "10202": ["New 'Server' header value seen",0],
  "10203": ["New 'Via' header value seen",0],
  "10204": ["New 'X-*' header value seen",0],
  "10205": ["New 404 signature seen",0],

  "10401": ["Resource not directly accessible",0],
  "10402": ["HTTP authentication required",0],
  "10403": ["Server error triggered",0],
  "10404": ["Directory listing enabled",0],
  "10405": ["Hidden files / directories",0],

  "10501": ["All external links",0],
  "10502": ["External URL redirector",0],
  "10503": ["All e-mail addresses",0],
  "10504": ["Links to unknown protocols",0],
  "10505": ["Unknown form field (can't autocomplete)",0],
  "10601": ["HTML form (not classified otherwise)",0],
  "10602": ["Password entry form - consider brute-force",0],
  "10603": ["File upload form",0],
  "10701": ["User-supplied link rendered on a page",0],
  "10801": ["Incorrect or missing MIME type (low risk)",0],
  "10802": ["Generic MIME used (low risk)",0],
  "10803": ["Incorrect or missing charset (low risk)",0],
  "10804": ["Conflicting MIME / charset info (low risk)",0],
  "10901": ["Numerical filename - consider enumerating",0],
  "10902": ["OGNL-like parameter behavior",0],
  "10909": ["Signature match (informational)",0],

  "20101": ["Resource fetch failed",0],
  "20102": ["Limits exceeded, fetch suppressed",0],
  "20201": ["Directory behavior checks failed (no brute force)",0],
  "20202": ["Parent behavior checks failed (no brute force)",0],
  "20203": ["IPS filtering enabled",0],
  "20204": ["IPS filtering disabled again",0],
  "20205": ["Response varies randomly, skipping checks",0],
  "20301": ["Node should be a directory, detection error?",0],

  "30101": ["HTTP credentials seen in URLs",0],
  "30201": ["SSL certificate expired or not yet valid",0],
  "30202": ["Self-signed SSL certificate",0],
  "30203": ["SSL certificate host name mismatch",0],
  "30204": ["No SSL certificate data found",0],
  "30205": ["Weak SSL cipher negotiated",0],
  "30206": ["Host name length mismatch (name string has null byte)",0],
  "30301": ["Directory listing restrictions bypassed",0],
  "30401": ["Redirection to attacker-supplied URLs",0],
  "30402": ["Attacker-supplied URLs in embedded content (lower risk)",0],
  "30501": ["External content embedded on a page (lower risk)",0],
  "30502": ["Mixed content embedded on a page (lower risk)",0],
  "30503": ["HTTPS form submitting to a HTTP URL",0],
  "30601": ["HTML form with no apparent XSRF protection",0],
  "30602": ["JSON response with no apparent XSSI protection",0],
  "30603": ["Auth form leaks credentials via HTTP GET",0],
  "30701": ["Incorrect caching directives (lower risk)",0],
  "30801": ["User-controlled response prefix (BOM / plugin attacks)",0],
  "30901": ["HTTP header injection vector",0],
  "30909": ["Signature match detected",0],

  "40101": ["XSS vector in document body",0],
  "40102": ["XSS vector via arbitrary URLs",0],
  "40103": ["HTTP response header splitting",0],
  "40104": ["Attacker-supplied URLs in embedded content (higher risk)",0],
  "40105": ["XSS vector via injected HTML tag attribute",0],
  "40201": ["External content embedded on a page (higher risk)",0],
  "40202": ["Mixed content embedded on a page (higher risk)",0],
  "40301": ["Incorrect or missing MIME type (higher risk)",0],
  "40302": ["Generic MIME type (higher risk)",0],
  "40304": ["Incorrect or missing charset (higher risk)",0],
  "40305": ["Conflicting MIME / charset info (higher risk)",0],
  "40401": ["Interesting file",0],
  "40402": ["Interesting server message",0],
  "40501": ["Directory traversal / file inclusion possible",0],
  "40601": ["Incorrect caching directives (higher risk)",0],
  "40701": ["Password form submits from or to non-HTTPS page",0],
  "40909": ["Signature match detected (higher risk)",0],

  "50101": ["Server-side XML injection vector",0],
  "50102": ["Shell injection vector",0],
  "50103": ["Query injection vector",0],
  "50104": ["Format string vector",0],
  "50105": ["Integer overflow vector",0],
  "50106": ["File inclusion",0],
  "50107": ["Remote file inclusion",0],
  "50201": ["SQL query or similar syntax in parameters",0],
  "50301": ["PUT request accepted",0],
  "50909": ["Signature match detected (high risk)",0]

}
list_of_skipfish_issue=Type_of_issue.copy()
list_of_dir=[] 
def Check_all_folders(Dir):
	global list_of_dir
	dir =["{}/{}".format(Dir,name) for name in os.listdir("{}".format(Dir)) if os.path.isdir("{}/{}".format(Dir,name)) and name[0]=="c"]
	list_of_dir.extend(dir)
	for i in range(len(dir)):
		Check_all_folders(dir[i])
def add_issue(path):
	global list_of_skipfish_issue
	with open("{}/issue_index.js".format(path), "r") as f:
		while True:
			line = f.readline()
			if not line:
			    break
			x=line.find("type")
			if x!=-1:
				list_of_skipfish_issue[line[x+7:x+12]][1]=list_of_skipfish_issue[line[x+7:x+12]][1]+1
def get_skipfish_resaults(name):
      Check_all_folders("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/skipfish/{}".format(name,name))	

      for i in range(len(list_of_dir)):
           add_issue(list_of_dir[i])	
      print("____________________________skipfish resaulet :___________________________")
      for i in list_of_skipfish_issue:
         if list_of_skipfish_issue[i][1] >0:
            print(list_of_skipfish_issue[i][0]," : : ",list_of_skipfish_issue[i][1])
def start_skipfish_get_resaults():
      list_of_skipfish_issue=Type_of_issue.copy()
      start_skipfish(url,name)
      
      get_skipfish_resaults(name)
starting_skipfish = threading.Thread(target=start_skipfish_get_resaults)
#starting_skipfish.start() 
#________________________________________________________Owasp_zap cli ____________
zap_vulnerabilities ={
'Directory Browsing':0, 
'Path Traversal':0,
'Remote File Inclusion':0, 
'Source Code Disclosure - /WEB-INF folder':0,
'GET for POST':0,
'User Agent Fuzzer':0,
'Heartbleed OpenSSL Vulnerability':0,
'Source Code Disclosure - CVE-2012-1823':0,
'Remote Code Execution - CVE-2012-1823':0,
'External Redirect':0,
'Buffer Overflow':0,
'Format String Error':0,
'CRLF Injection':0,
'Parameter Tampering':0,
'Server Side Include':0,
'Cross Site Scripting (Reflected)':0,
'Cross Site Scripting (Persistent)':0,
'Cross Site Scripting (Persistent) - Prime':0,
'Cross Site Scripting (Persistent) - Spider':0,
'SQL Injection':0,
'SQL Injection - MySQL':0,
'SQL Injection - Hypersonic SQL':0,
'SQL Injection - Oracle':0,
'SQL Injection - PostgreSQL':0,
'SQL Injection - SQLite':0,
'Cross Site Scripting (DOM Based)':0,
'SQL Injection - MsSQL':0,
'ELMAH Information Leak':0,
'Trace.axd Information Leak':0,
'.htaccess Information Leak':0,
'.env Information Leak':0,
'Hidden File Found':0,
'XSLT Injection':0,
'Server Side Code Injection':0,
'Server Side Code Injection - PHP Code Injection':0,
'Server Side Code Injection - ASP Code Injection':0,
'Remote OS Command Injection':0,
'XML External Entity Attack':0, 
'Generic Padding Oracle':0,
'Cloud Metadata Potentially Exposed':0,
'Server Side Template Injection':0}
#problem eno g3d yannalize mm fel passive attack haw site officel mnin tahna ajoutihem wchouf m3aha :
# https://www.zaproxy.org/docs/alerts/
#this commented part is  using Zap-cli "but it seems that it's no longer supported so we gonna us the new api devolped officiely by owaspZap"
#https://www.zaproxy.org/docs/api/ this is the api provided by the owasapzap officiel site <3 check it for more advance option "maybe in the future you would activate the passive scanners also"
def start_zap():
     print("zap server starting:")
     output = subprocess.run("zap.sh -daemon -config api.key=mypass123 -port 8090 -host 0.0.0.0", shell=True, capture_output=True)
     
def check_for_zap():
    output1= subprocess.run("zap-cli status",shell=True,capture_output=True)
    string=str(output1.stdout)    
    while string[3]=="E":	
       time.sleep(10)
       output1= subprocess.run("zap-cli status",shell=True,capture_output=True)
       string=str(output1.stdout)    
    else :
             apiKey = 'mypass123'
             zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})
             scanID = zap.spider.scan(url)
             """while int(zap.spider.status(scanID)) < 100:
                 # Poll the status until it completes
                 print('Spider progress %: {}'.format(zap.spider.status(scanID)))
                 time.sleep(1)
             """
             while int(zap.spider.status(scanID)) < 100:
                 time.sleep(2)
             # Prints the URLs the spider has crawled
             #print('\n'.join(map(str, zap.spider.results(scanID))))
             # If required post process the spider results
             # TODO: Explore the ajax way 
             scanID = zap.ajaxSpider.scan(url)
             timeout = time.time() + 60*2   # 2 minutes from now
             # Loop until the ajax spider has finished or the timeout has exceeded
             while zap.ajaxSpider.status == 'running':
                 if time.time() > timeout:
                     break
                 time.sleep(2)
             ajaxResults = zap.ajaxSpider.results(start=0, count=10)
             #Disabling the passive scanner since we don't need them for now
             zap.pscan.disable_all_scanners()
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
             scanID = zap.ascan.scan(url)
             while int(zap.ascan.status(scanID)) < 100:
                 # Loop until the scanner has finished
                 #print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
                 time.sleep(5)
             print('Active Scan completed')  
             with open("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/owaspzap/{}.json".format(name,name), 'w') as convert_file:
                  convert_file.write(json.dumps(zap.core.alerts(baseurl=url)))
             global zap_vulnerabilities_new
             zap_vulnerabilities_new=owaspzap_get_resaults(name)
def owaspzap_get_resaults(name):
         zap_vulnerabilities_new=zap_vulnerabilities.copy()
         with open('/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/owaspzap/{}.json'.format(name,name), 'r') as read_file:
              myresault=json.load(read_file)              
              print("length:",len(myresault))
              for i in myresault:
                   zap_vulnerabilities_new[i['alert']]=zap_vulnerabilities_new[i['alert']]+1
         print(zap_vulnerabilities_new)
         return zap_vulnerabilities_new

starting_zap = threading.Thread(target=start_zap)
#starting_zap.start()
checking_zap= threading.Thread(target=check_for_zap)
#checking_zap.start()

#__________________________________________________________zap-cli___________________________________________
"""
def check_for_zap2(): 
    output1= subprocess.run("zap-cli status",shell=True,capture_output=True)
    string=str(output1.stdout)    
    while string[3]=="E":	
       time.sleep(20)
       output1= subprocess.run("zap-cli status",shell=True,capture_output=True)
       string=str(output1.stdout)    
    else :
        print("zap start spidring:")
        output1= subprocess.run("zap-cli --zap-url http://0.0.0.0:8090/ -p 8090 spider {}".format(url),shell=True,capture_output=True)
        print("zap start active scan:")
        output1= subprocess.run("zap-cli --zap-url http://0.0.0.0:8090/ -p 8090 active-scan -r {}".format(url),shell=True,capture_output=True)
        print("zap Start Reporting: ")
        output1= subprocess.run("zap-cli --zap-url http://0.0.0.0:8090/ -p 8090 report -f html -o /home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/owaspzap/{}.html".format(name,name),shell=True,capture_output=True) 
        output1= subprocess.run("zap-cli --zap-url http://0.0.0.0:8090/ -p 8090 report -f xml -o /home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/owaspzap/{}.xml".format(name,name),shell=True,capture_output=True) 
        print("_____________________Zap Resault is in:_____________________________ ")
        print("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/owaspzap/{}.html".format(name,name))
        print("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/owaspzap/{}.xml".format(name,name))

    
starting_zap = threading.Thread(target=start_zap)
#starting_zap.start()
checking_zap= threading.Thread(target=check_for_zap2)
#checking_zap.start()

def  get_zap_resaults(name):
     list_zap_vulnerabilities=zap_vulnerabilities.copy()
# Reading the data inside the xml file to a variable under the name  data
     with open('/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/owaspzap/{}.xml'.format(name,name), 'r') as f:
         data = f.read() 
     bs_data = BeautifulSoup(data, 'xml') 
     b_alerts = bs_data.find_all('alert') 
     for i in b_alerts:
         print(i.text)
#         list_zap_vulnerabilities[i.text]=list_zap_vulnerabilities[i.text]+1
#     print(list_zap_vulnerabilities)
     return list_zap_vulnerabilities

get_zap_resaults(name)
"""
#_______________________________________________________________nikto _______________

import json
with open("/home/ostesayed/Desktop/Scanners/OSTEscaner/nikto_vulnerability_tunning/nikto_tuning.json", 'r') as nikto_file:
         nikto_vulnerability= json.load(nikto_file)     

  
def start_nikto(name,url):
     output = subprocess.run("nikto -h {}  -o /home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/nikto/{}_9.json -F json -Tuning 9".format(url,name,name), shell=True, capture_output=True)
     output = subprocess.run("nikto -h {}  -o /home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/nikto/{}_4.json -F json -Tuning 4".format(url,name,name), shell=True, capture_output=True)
     output = subprocess.run("nikto -h {}  -o /home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/nikto/{}_f.json -F json -Tuning f".format(url,name,name), shell=True, capture_output=True)
     print("the scan did finished")
     get_nikto_vulnerability("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/nikto/{}_9".format(name,name))         
     get_nikto_vulnerability("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/nikto/{}_4".format(name,name))
     get_nikto_vulnerability("/home/ostesayed/Desktop/Scanners/OSTEscaner/Resaults/{}/nikto/{}_f".format(name,name))
     print("________________________________________Nikto Reporte:______________________________________________")
     print("this is the number of sql injection possiiblity:",nikto_vulnerability['nikto_vulnerability']['sql_injection']['number'])
     print("this is the number of XML injection possiiblity:",nikto_vulnerability['nikto_vulnerability']['XML injection']['number'])
     print("this is the number of script_injection possiiblity:",nikto_vulnerability['nikto_vulnerability']['script_injection']['number'])
     print("this is the number of sql information possiiblity:",nikto_vulnerability['nikto_vulnerability']['sql information']['number'])
     print("this is the number of html injection possiiblity:",nikto_vulnerability['nikto_vulnerability']['html injection']['number'])
     print("this is the number of XSLT_Extensible Stylesheet Language Transformations injection possiiblity:",nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'])
     print("this is the number of remote source injection possiiblity:",nikto_vulnerability['nikto_vulnerability']['remote source injection']['number'])
     print("this is the number of XSS injection possiiblity:",nikto_vulnerability['nikto_vulnerability']['XSS injection']['number'])

def get_nikto_vulnerability(name):
    global nikto_vulnerability
    with open("{}.json".format(name), 'r') as nikto_report_file:
         nikto_report_vulnerability= json.load(nikto_report_file)
         
         for i in range(len(nikto_report_vulnerability['vulnerabilities'])):
        #      print(nikto_report_vulnerability['vulnerabilities'][i]['id'])
              if nikto_report_vulnerability['vulnerabilities'][i]['id']  in nikto_vulnerability['nikto_vulnerability']['sql_injection']['ids']:
                        nikto_vulnerability['nikto_vulnerability']['sql_injection']['number']=nikto_vulnerability['nikto_vulnerability']['sql_injection']['number']+1
              elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in nikto_vulnerability['nikto_vulnerability']['XML injection']['ids']:
                        nikto_vulnerability['nikto_vulnerability']['XML injection']['number']=nikto_vulnerability['nikto_vulnerability']['XML injection']['number']+1

              elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in nikto_vulnerability['nikto_vulnerability']['script_injection']['ids']:
                        nikto_vulnerability['nikto_vulnerability']['script_injection']['number']=nikto_vulnerability['nikto_vulnerability']['script_injection']['number']+1
              elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in nikto_vulnerability['nikto_vulnerability']['sql information']['ids']:
                        nikto_vulnerability['nikto_vulnerability']['sql information']['number']=nikto_vulnerability['nikto_vulnerability']['sql information']['number']+1
              elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in nikto_vulnerability['nikto_vulnerability']['html injection']['ids']:
                        nikto_vulnerability['nikto_vulnerability']['html injection']['number']=nikto_vulnerability['nikto_vulnerability']['html injection']['number']+1
              elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['ids']:
                        nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number']=nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number']+1
              elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in nikto_vulnerability['nikto_vulnerability']['remote source injection']['ids']:
                        nikto_vulnerability['nikto_vulnerability']['remote source injection']['number']=nikto_vulnerability['nikto_vulnerability']['remote source injection']['number']+1
              elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in nikto_vulnerability['nikto_vulnerability']['XSS injection']['ids']:
                        nikto_vulnerability['nikto_vulnerability']['XSS injection']['number']=nikto_vulnerability['nikto_vulnerability']['XSS injection']['number']+1
def start_nikto_get_report():
     start_nikto(name,url)
starting_nikto = threading.Thread(target=start_nikto_get_report)
#starting_nikto.start() 

#type_of_vuln_nikto= {"0":["Potentially interesting  file found",0],"1":["Interesting File / Seen in logs",0],"2":[" Misconfiguration / Default File",0],"-1":["File Upload",0],"3":[" Information Disclosure",0],"4":[" Injection (XSS/Script/HTML)",0],"5":["Remote File Retrieval - Inside Web Root",0],"6":["Denial of Service",0],"7":["Remote File Retrieval - Server Wide",0],"8":["Command Execution / Remote Shell",0],"9":["SQL Injection",0]}

#______________________________________________________________nuclei _____________________
"""
import json 
name="Jucyshopex23"
url="http://localhost:3000/"
def start_categorise_nuclei_vuln_cves():
    data = []
    dater={}
    with open("nuclei_cve/cves.json") as f:
        for line in f:
           # print(line)
            data.append(json.loads(line)) 
           
    for i in data :
        dater[i['Info']['Name']]=0
    return dater
dater=start_categorise_nuclei_vuln_cves()

def start_nuclei(name,url):
     output = subprocess.run("nuclei -u {} -tags cve -o nuclei/{}.json -json -duc -ni ".format(url,name), shell=True, capture_output=True)
     print("the scan did finished")
     
#start_nuclei(name,url)
def list_the_Vuln_nuclei(path):
# Opening JSON file
    data = []
    with open("{}.json".format(path)) as f:
        for line in f:
            data.append(json.loads(line)) 
    for i in data :
        dater[i['info']['name']]=dater[i['info']['name']]+1
#        print(i['info']['name'])     
 
#list_the_Vuln_nuclei("nuclei/{}".format(name))     
def my_filtering_function(pair):
    key, value = pair
    if value <= 0:
        return False  # filter pair out of the dictionary
    else:
        return True  # keep pair in the filtered dictionary
 
  
filtered_grades = dict(filter(my_filtering_function, dater.items()))
 
print(filtered_grades)

"""
