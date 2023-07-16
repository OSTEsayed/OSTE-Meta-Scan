#todo: skipfish ki ykon target makanch maytastish apre ki n7aws 3a resault mnlgach.
import os 
import sys
import subprocess
import threading
import time
import json
from zapv2 import ZAPv2
from pprint import pprint
from bs4 import BeautifulSoup 
#___________________________________________creat_resaults_folder ______________________
#name = "JucyShope3"
#url ="http://localhost:3000/"
class scan_checker():
    def __init__(self):#wapiti --version
    	self.wapiti=True
    	self.zap=True
    	self.nuclei=False
    	self.nikto=False
    	self.skipfish=False
    	self.script_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
    def check(self):
          output = subprocess.run("wapiti --version", shell=True, capture_output=True,text=True).stdout.strip("\n")
          if "Wapiti" in output[343::]:
              self.wapiti=True
          output1 = subprocess.run("nikto -V", shell=True, capture_output=True,text=True).stdout.strip("\n")
          if "Nikto main" in output1:
              self.nikto=True
          output2 = subprocess.run("nuclei -version", shell=True, capture_output=True,text=True).stderr.strip("\n")
          if "Current" in output2:
              self.nuclei=True         
         
          output3 = subprocess.run("skipfish", shell=True, capture_output=True,text=True).stdout.strip("\n")
          if "skipfish web" in output3:
              self.skipfish=True         
          return [[self.wapiti,"Wapiti {}".format(output[len(output)-5::])],[self.zap,"OWASP ZAP V2.10.0"],[self.nuclei,"Nuclei {}".format(output2[212::])],[self.nikto,"Nikto {}".format(output1[318:323])],[self.skipfish,"skipfish {}".format(output3[43:48])]]
   
    	
class scan():
    def __init__(self):
        self.name="OSTE"
        self.url="LOCALHOST"
        self.wapiti_vulnerabilities= {
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
        self.list_of_dir=[]             #skipfish resault dirs 
        self.Type_of_issue={

  "10101": ["SSL certificate issuer information",0,[]],
  "10201": ["New HTTP cookie added",0,[]],
  "10202": ["New 'Server' header value seen",0,[]],
  "10203": ["New 'Via' header value seen",0,[]],
  "10204": ["New 'X-*' header value seen",0,[]],
  "10205": ["New 404 signature seen",0,[]],

  "10401": ["Resource not directly accessible",0,[]],
  "10402": ["HTTP authentication required",0,[]],
  "10403": ["Server error triggered",0,[]],
  "10404": ["Directory listing enabled",0,[]],
  "10405": ["Hidden files / directories",0,[]],

  "10501": ["All external links",0,[]],
  "10502": ["External URL redirector",0,[]],
  "10503": ["All e-mail addresses",0,[]],
  "10504": ["Links to unknown protocols",0,[]],
  "10505": ["Unknown form field (can't autocomplete)",0,[]],
  "10601": ["HTML form (not classified otherwise)",0,[]],
  "10602": ["Password entry form - consider brute-force",0,[]],
  "10603": ["File upload form",0,[]],
  "10701": ["User-supplied link rendered on a page",0,[]],
  "10801": ["Incorrect or missing MIME type (low risk)",0,[]],
  "10802": ["Generic MIME used (low risk)",0,[]],
  "10803": ["Incorrect or missing charset (low risk)",0,[]],
  "10804": ["Conflicting MIME / charset info (low risk)",0,[]],
  "10901": ["Numerical filename - consider enumerating",0,[]],
  "10902": ["OGNL-like parameter behavior",0,[]],
  "10909": ["Signature match (informational)",0,[]],

  "20101": ["Resource fetch failed",0,[]],
  "20102": ["Limits exceeded, fetch suppressed",0,[]],
  "20201": ["Directory behavior checks failed (no brute force)",0,[]],
  "20202": ["Parent behavior checks failed (no brute force)",0,[]],
  "20203": ["IPS filtering enabled",0,[]],
  "20204": ["IPS filtering disabled again",0,[]],
  "20205": ["Response varies randomly, skipping checks",0,[]],
  "20301": ["Node should be a directory, detection error?",0,[]],

  "30101": ["HTTP credentials seen in URLs",0,[]],
  "30201": ["SSL certificate expired or not yet valid",0,[]],
  "30202": ["Self-signed SSL certificate",0,[]],
  "30203": ["SSL certificate host name mismatch",0,[]],
  "30204": ["No SSL certificate data found",0,[]],
  "30205": ["Weak SSL cipher negotiated",0,[]],
  "30206": ["Host name length mismatch (name string has null byte)",0,[]],
  "30301": ["Directory listing restrictions bypassed",0,[]],
  "30401": ["Redirection to attacker-supplied URLs",0,[]],
  "30402": ["Attacker-supplied URLs in embedded content (lower risk)",0,[]],
  "30501": ["External content embedded on a page (lower risk)",0,[]],
  "30502": ["Mixed content embedded on a page (lower risk)",0,[]],
  "30503": ["HTTPS form submitting to a HTTP URL",0,[]],
  "30601": ["HTML form with no apparent XSRF protection",0,[]],
  "30602": ["JSON response with no apparent XSSI protection",0,[]],
  "30603": ["Auth form leaks credentials via HTTP GET",0,[]],
  "30701": ["Incorrect caching directives (lower risk)",0,[]],
  "30801": ["User-controlled response prefix (BOM / plugin attacks)",0,[]],
  "30901": ["HTTP header injection vector",0,[]],
  "30909": ["Signature match detected",0,[]],

  "40101": ["XSS vector in document body",0,[]],
  "40102": ["XSS vector via arbitrary URLs",0,[]],
  "40103": ["HTTP response header splitting",0,[]],
  "40104": ["Attacker-supplied URLs in embedded content (higher risk)",0,[]],
  "40105": ["XSS vector via injected HTML tag attribute",0,[]],
  "40201": ["External content embedded on a page (higher risk)",0,[]],
  "40202": ["Mixed content embedded on a page (higher risk)",0,[]],
  "40301": ["Incorrect or missing MIME type (higher risk)",0,[]],
  "40302": ["Generic MIME type (higher risk)",0,[]],
  "40304": ["Incorrect or missing charset (higher risk)",0,[]],
  "40305": ["Conflicting MIME / charset info (higher risk)",0,[]],
  "40401": ["Interesting file",0,[]],
  "40402": ["Interesting server message",0,[]],
  "40501": ["Directory traversal / file inclusion possible",0,[]],
  "40601": ["Incorrect caching directives (higher risk)",0,[]],
  "40701": ["Password form submits from or to non-HTTPS page",0,[]],
  "40909": ["Signature match detected (higher risk)",0,[]],

  "50101": ["Server-side XML injection vector",0,[]],
  "50102": ["Shell injection vector",0,[]],
  "50103": ["Query injection vector",0,[]],
  "50104": ["Format string vector",0,[]],
  "50105": ["Integer overflow vector",0,[]],
  "50106": ["File inclusion",0,[]],
  "50107": ["Remote file inclusion",0,[]],
  "50201": ["SQL query or similar syntax in parameters",0,[]],
  "50301": ["PUT request accepted",0,[]],
  "50909": ["Signature match detected (high risk)",0,[]]

}
        self.zap_vulnerabilities ={
                                #alert(vulnerability:)  method \n url (Method\nURL)  inputVector(inputVector)  description(description) 

'Directory Browsing':[0,[],[],[],[]], 
'Path Traversal':[0,[],[],[],[]],
'Remote File Inclusion':[0,[],[],[],[]], 
'Source Code Disclosure - /WEB-INF folder':[0,[],[],[],[]],
'GET for POST':[0,[],[],[],[]],
'User Agent Fuzzer':[0,[],[],[],[]],
'Heartbleed OpenSSL Vulnerability':[0,[],[],[],[]],
'Source Code Disclosure - CVE-2012-1823':[0,[],[],[],[]],
'Remote Code Execution - CVE-2012-1823':[0,[],[],[],[]],
'External Redirect':[0,[],[],[],[]],
'Buffer Overflow':[0,[],[],[],[]],
'Format String Error':[0,[],[],[],[]],
'CRLF Injection':[0,[],[],[],[]],
'Parameter Tampering':[0,[],[],[],[]],
'Server Side Include':[0,[],[],[],[]],
'Cross Site Scripting (Reflected)':[0,[],[],[],[]],
'Cross Site Scripting (Persistent)':[0,[],[],[],[]],
'Cross Site Scripting (Persistent) - Prime':[0,[],[],[],[]],
'Cross Site Scripting (Persistent) - Spider':[0,[],[],[],[]],
'SQL Injection':[0,[],[],[],[]],
'SQL Injection - MySQL':[0,[],[],[],[]],
'SQL Injection - Hypersonic SQL':[0,[],[],[],[]],
'SQL Injection - Oracle':[0,[],[],[],[]],
'SQL Injection - PostgreSQL':[0,[],[],[],[]],
'SQL Injection - SQLite':[0,[],[],[],[]],
'Cross Site Scripting (DOM Based)':[0,[],[],[],[]],
'SQL Injection - MsSQL':[0,[],[],[],[]],
'ELMAH Information Leak':[0,[],[],[],[]],
'Trace.axd Information Leak':[0,[],[],[],[]],
'.htaccess Information Leak':[0,[],[],[],[]],
'.env Information Leak':[0,[],[],[],[]],
'Hidden File Found':[0,[],[],[],[]],
'XSLT Injection':[0,[],[],[],[]],
'Server Side Code Injection':[0,[],[],[],[]],
'Server Side Code Injection - PHP Code Injection':[0,[],[],[],[]],
'Server Side Code Injection - ASP Code Injection':[0,[],[],[],[]],
'Remote OS Command Injection':[0,[],[],[],[]],
'XML External Entity Attack':[0,[],[],[],[]], 
'Generic Padding Oracle':[0,[],[],[],[]],
'Cloud Metadata Potentially Exposed':[0,[],[],[],[]],
'SOAP XML Injection':[0,[],[],[],[]],
'Server Side Template Injection':[0,[],[],[],[]]}
        with open("{}/nikto_vulnerability_tunning/nikto_tuning.json".format(self.script_dir), 'r') as nikto_file:
                 self.nikto_vulnerability= json.load(nikto_file)     
        self.list_of_skipfish_issue=self.Type_of_issue.copy()
#Nuclei Vulnerability configureation(1500 Template in nuclei_cve/cves.json)        
        data = []
        self.dater={}
        with open("nuclei_cve/cves.json") as f:
                for line in f:
           # print(line)
                    data.append(json.loads(line)) 
                    
                for i in data : 		#Name(number)         matched-at       (curl-command)   Description
                    self.dater[i['Info']['Name']]=[0,[],[],i['Info']['Description']]
        
    def configuiring_new_scan(self,name,setting,url=None):
        self.setting=setting
        self.name=name
        self.url=url
        #print(f"name:{self.name},url:{self.url},crawl:{self.crawl}")
    def starting_all_scanner(self,name,url):
       # global name ,url
        self.name=name
        self.url=url
        #self.creat_directory(self.name,self.url)
        #self.wapiti_Thread()
#        starting_wapiti.start() 
#        starting_skipfish.start() 
#        starting_zap.start()
#        checking_zap.start()
#        starting_nuclei.start() 

    def creat_directory(self):
        #print("[INFO] 		Creating Resaults Directory for each scanner")
        
        #print("[location]	/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/"+self.name)
        try:
            os.makedirs("{}/Resaults/".format(self.script_dir)+self.name)
            os.makedirs("{}/Resaults/".format(self.script_dir)+self.name+"/"+"wapiti")
            os.makedirs("{}/Resaults/".format(self.script_dir)+self.name+"/"+"nuclei")
            os.makedirs("{}/Resaults/".format(self.script_dir)+self.name+"/"+"owaspzap")
            os.makedirs("{}/Resaults/".format(self.script_dir)+self.name+"/"+"skipfish")
            os.makedirs("{}/Resaults/".format(self.script_dir)+self.name+"/"+"nikto")
        except OSError as error:
            print("Error creating The Resault folder foor {}: {}".format(self.name,error))
    #to do : if this errour messege occured you need make new name because this file already exist wiche means you will have problem in skip fish probebly more.
#__________________________________________Wapiti_________________________________________________________
#""" 
 #  def wapiti_Thread(self):
  #      starting_wapiti = threading.Thread(target=self.start_wapiti)
   #     starting_wapiti.start() """
    def get_wapiti_resaults(self):   
        f = open("{}/Resaults/{}/wapiti/{}.json".format(self.script_dir,self.name,self.name))
        data = json.load(f)
        wapiti_resaults=self.wapiti_vulnerabilities.copy()
        printedtypes={}
        
        for vul in data["vulnerabilities"]:
            printedtypes[vul]=data["vulnerabilities"][vul]
            wapiti_resaults[vul]=len(data["vulnerabilities"][vul])
        f.close()
        return wapiti_resaults,printedtypes
    
    def start_wapiti(self):
        #print("[INFO] 		wapiti scan started:") --max-links-per-page --max-links-per-page
        output = subprocess.run("wapiti --flush-session -u {} -f json -o {}/Resaults/{}/wapiti/{}.json -l 2 -d {}  --max-links-per-page {} --max-files-per-dir {} --max-scan-time {} --max-attack-time 40".format(self.url,self.script_dir ,self.name,self.name,self.setting['wapiti_d'],self.setting['wapiti_lp'],self.setting['wapiti_fd'],self.setting['wapiti_st']), shell=True, capture_output=True)
        #print("[Finished]		wapiti Scan completed. ")    
#	"""
#    def start_wapiti_readReport():
#        start_wapiti(self.url,self.name)
#        wapiti_resaults= get_wapiti_resaults(name)
#        print("[Result]______________________________WApiti Results:_________________________")
#        print(wapiti_resaults)
#		"""
#___________________________________________SKIPFISH________________________________________
#-d max_depth (16), -c max_child (512) -x max_descandent (8192)
#-k duration h:m:s 
    def start_skipfish(self):
            #print("[INFO] 		skipfish scan started:")-d {} #add 
            output = subprocess.run("skipfish -L -Y -e -v -u -d {} -c {} -x {} -p {} -I {} -o {}/Resaults/{}/skipfish/{} {}".format(self.setting['skip_d'],self.setting['skip_dc'],self.setting['skip_dx'],self.setting['skip_cp'],self.url,self.script_dir ,self.name,self.name,self.url), shell=True, capture_output=True)
            #self.crawl+1,print("[finished]	skipfish scand completed. ")

    def Check_all_folders(self,Dir):
            dir =["{}/{}".format(Dir,name) for name in os.listdir("{}".format(Dir)) if os.path.isdir("{}/{}".format(Dir,name)) and name[0]=="c"]
            self.list_of_dir.extend(dir)
            for i in range(len(dir)):
                   self.Check_all_folders(dir[i])
    def add_issue(self,path):
            self.list_of_skipfish_issue=self.Type_of_issue.copy()
            with open("{}/issue_index.js".format(path), "r") as f:
                  while True:
                        line = f.readline()
                        if not line:
                            break
                        x=line.find("type")
                        if x!=-1:
                             self.list_of_skipfish_issue[line[x+7:x+12]][1]=self.list_of_skipfish_issue[line[x+7:x+12]][1]+1
                             with open("{}/request.dat".format(path),"r") as r:
                                r1=r.readline()
                                r2=r.readline()

                                self.list_of_skipfish_issue[line[x+7:x+12]][2].append([r1,r2])
                             
    def get_skipfish_resaults(self):
          self.Check_all_folders("{}/Resaults/{}/skipfish/{}".format(self.script_dir ,self.name,self.name))	

          for i in range(len(self.list_of_dir)):
               self.add_issue(self.list_of_dir[i])	
          #print("____________________________skipfish resaulet :___________________________")
         # for i in self.list_of_skipfish_issue:
          #   if self.list_of_skipfish_issue[i][1] >0:
           #     print(self.list_of_skipfish_issue[i][0]," : : ",self.list_of_skipfish_issue[i][1])
          return self.list_of_skipfish_issue
    def start_skipfish_get_resaults(self):
          self.list_of_skipfish_issue=self.Type_of_issue.copy()
          start_skipfish(url,name)
      
          self.get_skipfish_resaults()
    #starting_skipfish = threading.Thread(target=self.start_skipfish_get_resaults)
    #starting_skipfish.start() 
#________________________________________________________Owasp_zap cli ____________
    def start_zap(self):
             #print("[INFO] 		zap server starting:")
             output = subprocess.run("zap.sh -daemon -config api.key=mypass123 -port 8090 -host 0.0.0.0", shell=True, capture_output=True)

    def check_for_zap(self):
            output1= subprocess.run("zap-cli status",shell=True,capture_output=True)
            string=str(output1.stdout)    
            while string[3]=="E":	
               time.sleep(10)
               output1= subprocess.run("zap-cli status",shell=True,capture_output=True)
               string=str(output1.stdout)    
            else :
                     apiKey = 'mypass123'
                     zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})
             #Disabling the passive scanner since we don't need them for now
#             zap.pscan.set_enabled(False)
                     zap.pscan.disable_all_scanners()
#             # TODO: Disabling feew active scanner i don't need to check for their vilnerability
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
             #raja3 adi
#                    zap.spider.set_option_max_duration(2)zap.spider.scan(url, recurse=False, subtreeonly=True)
                     zap.core.access_url(url=self.url)
                     time.sleep(2)
                     zap.spider.set_option_max_depth(self.setting['zap_d']) 
                     zap.spider.set_option_max_children(self.setting['zap_dc'])
                     time.sleep(1)
                     if self.setting['zap_c']==0:
                          print("ak hna")
                          scanID = zap.spider.scan(self.url, recurse=False, subtreeonly=True)
                          while int(zap.spider.status(scanID)) < 100:
                             print('Spider progress %: {}'.format(zap.spider.status(scanID)))
                             time.sleep(2)
                     
#                     """while int(zap.spider.status(scanID)) < 100:
#                         # Poll the status until it completes
#                         time.sleep(1)
#                     """
                     # Prints the URLs the spider has crawled
                     #print('\n'.join(map(str, zap.spider.results(scanID))))
                     # If required post process the spider results
                     # TODO: Explore the ajax way 
                     
                     #scanID = zap.ajaxSpider.scan(url)
                     #timeout = time.time() + 60*2   # 2 minutes from now
                     # Loop until the ajax spider has finished or the timeout has exceeded
                     #while zap.ajaxSpider.status == 'running':
                     #    if time.time() > timeout:
                     #        break
                     #    time.sleep(2)
                     #ajaxResults = zap.ajaxSpider.results(start=0, count=10)
                     #passive attack check(officel site to integrate...)                   
                     #active scan 
                     #""""""
                     # TODO : explore the app (Spider, etc) before using the Active Scan API, Refer the explore section
                     scanID = zap.ascan.scan(self.url)
                     time.sleep(2)
                     print(zap.ascan.status(scanID))
                     while int(zap.ascan.status(scanID)) < 100:
                         # Loop until the scanner has finished
                         print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
                         time.sleep(4)
                     #print('[finished] 		Zap scan completed')  
                     with open("{}/Resaults/{}/owaspzap/{}.json".format(self.script_dir ,self.name,self.name), 'w') as convert_file:
                          convert_file.write(json.dumps(zap.core.alerts(baseurl=self.url)))
             
    def owaspzap_get_resaults(self):
                 zap_vulnerabilities_new=self.zap_vulnerabilities.copy()
                 with open('{}/Resaults/{}/owaspzap/{}.json'.format(self.script_dir,self.name,self.name), 'r') as read_file:
                      myresault=json.load(read_file)              
                      #print("length:",len(myresault))
                      for i in myresault:
                        #alert(vulnerability:)  method \n url (Method\nURL)  inputVector(inputVector)  description(description) 
                           zap_vulnerabilities_new[i['alert']][0]=zap_vulnerabilities_new[i['alert']][0]+1
                           zap_vulnerabilities_new[i['alert']][1].append([i['method'],i['url']])
                           zap_vulnerabilities_new[i['alert']][2].append(i['param']+":"+i['attack'])#inputVector
                           zap_vulnerabilities_new[i['alert']][3].append(i['description'])

               #  print("[Result]__________________________Zap Results:_____________________________")
                 #print(zap_vulnerabilities_new)
                 return zap_vulnerabilities_new
    def start_get_zap(self):
             #check_for_zap()
             zap_vulnerabilities_new=owaspzap_get_resaults()
     
#starting_zap = threading.Thread(target=start_zap)
#checking_zap= threading.Thread(target=start_get_zap)
#starting_zap.start()
#checking_zap.start()
#_______________________________________________________________nikto ___________________________________________________________________________


  
    def start_nikto(self):
         #print("[INFO] 		Nikto scan Started:") -no404 -nossl -nolookup -nocache "-nolookup  -nossl -no404 -nointeractive
         output = subprocess.run("nikto -h {} -ask no -o {}/Resaults/{}/nikto/{}_9.json -F json -Tuning 9 -nossl -nointeractive".format(self.url,self.script_dir ,self.name,self.name), shell=True, capture_output=True)
         output = subprocess.run("nikto -h {} -ask no -o {}/Resaults/{}/nikto/{}_4.json -F json -Tuning 4 -nossl -nointeractive".format(self.url,self.script_dir ,self.name,self.name), shell=True, capture_output=True)
#         output = subprocess.run("nikto -h {}  -o /home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/{}/nikto/{}_f.json -F json -Tuning f".format(url,name,name), shell=True, capture_output=True)
         #print("[finished] 		Nikto scan  completed")
    
    def get_nikto_vulnerability(self,path):
        
        with open("{}.json".format(path), 'r') as nikto_report_file:
             nikto_report_vulnerability= json.load(nikto_report_file)
             
             for i in range(len(nikto_report_vulnerability['vulnerabilities'])):
            #      print(nikto_report_vulnerability['vulnerabilities'][i]['id'])
            #id(vulnerability:)  method (METHOD) msg(description)  url (URL)  OSVDB(OSBDV Ref:)  
                  if nikto_report_vulnerability['vulnerabilities'][i]['id']  in self.nikto_vulnerability['nikto_vulnerability']['sql_injection']['ids']:
                            self.nikto_vulnerability['nikto_vulnerability']['sql_injection']['number']=self.nikto_vulnerability['nikto_vulnerability']['sql_injection']['number']+1
                            self.nikto_vulnerability['nikto_vulnerability']['sql_injection']["method_msg"].append([nikto_report_vulnerability['vulnerabilities'][i]['method'],nikto_report_vulnerability['vulnerabilities'][i]['msg'],nikto_report_vulnerability['vulnerabilities'][i]['url'],nikto_report_vulnerability['vulnerabilities'][i]['OSVDB']])
                  elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in self.nikto_vulnerability['nikto_vulnerability']['XML injection']['ids']:
                            self.nikto_vulnerability['nikto_vulnerability']['XML injection']['number']=self.nikto_vulnerability['nikto_vulnerability']['XML injection']['number']+1
                            self.nikto_vulnerability['nikto_vulnerability']['XML injection']["method_msg"].append([nikto_report_vulnerability['vulnerabilities'][i]['method'],nikto_report_vulnerability['vulnerabilities'][i]['msg'],nikto_report_vulnerability['vulnerabilities'][i]['url'],nikto_report_vulnerability['vulnerabilities'][i]['OSVDB']])

                  elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in self.nikto_vulnerability['nikto_vulnerability']['script_injection']['ids']:
                            self.nikto_vulnerability['nikto_vulnerability']['script_injection']['number']=self.nikto_vulnerability['nikto_vulnerability']['script_injection']['number']+1
                            self.nikto_vulnerability['nikto_vulnerability']['script_injection']["method_msg"].append([nikto_report_vulnerability['vulnerabilities'][i]['method'],nikto_report_vulnerability['vulnerabilities'][i]['msg'],nikto_report_vulnerability['vulnerabilities'][i]['url'],nikto_report_vulnerability['vulnerabilities'][i]['OSVDB']])
                  elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in self.nikto_vulnerability['nikto_vulnerability']['sql information']['ids']:
                            self.nikto_vulnerability['nikto_vulnerability']['sql information']['number']=self.nikto_vulnerability['nikto_vulnerability']['sql information']['number']+1
                            self.nikto_vulnerability['nikto_vulnerability']['sql information']["method_msg"].append([nikto_report_vulnerability['vulnerabilities'][i]['method'],nikto_report_vulnerability['vulnerabilities'][i]['msg'],nikto_report_vulnerability['vulnerabilities'][i]['url'],nikto_report_vulnerability['vulnerabilities'][i]['OSVDB']])
                  elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in self.nikto_vulnerability['nikto_vulnerability']['html injection']['ids']:
                            self.nikto_vulnerability['nikto_vulnerability']['html injection']['number']=self.nikto_vulnerability['nikto_vulnerability']['html injection']['number']+1
                            self.nikto_vulnerability['nikto_vulnerability']['html injection']["method_msg"].append([nikto_report_vulnerability['vulnerabilities'][i]['method'],nikto_report_vulnerability['vulnerabilities'][i]['msg'],nikto_report_vulnerability['vulnerabilities'][i]['url'],nikto_report_vulnerability['vulnerabilities'][i]['OSVDB']])
                  elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in self.nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['ids']:
                            self.nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number']=self.nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number']+1
                            self.nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']["method_msg"].append([nikto_report_vulnerability['vulnerabilities'][i]['method'],nikto_report_vulnerability['vulnerabilities'][i]['msg'],nikto_report_vulnerability['vulnerabilities'][i]['url'],nikto_report_vulnerability['vulnerabilities'][i]['OSVDB']])
                  elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in self.nikto_vulnerability['nikto_vulnerability']['remote source injection']['ids']:
                            self.nikto_vulnerability['nikto_vulnerability']['remote source injection']['number']=self.nikto_vulnerability['nikto_vulnerability']['remote source injection']['number']+1
                            self.nikto_vulnerability['nikto_vulnerability']['remote source injection']["method_msg"].append([nikto_report_vulnerability['vulnerabilities'][i]['method'],nikto_report_vulnerability['vulnerabilities'][i]['msg'],nikto_report_vulnerability['vulnerabilities'][i]['url'],nikto_report_vulnerability['vulnerabilities'][i]['OSVDB']])
                  elif nikto_report_vulnerability['vulnerabilities'][i]['id']  in self.nikto_vulnerability['nikto_vulnerability']['XSS injection']['ids']:
                            self.nikto_vulnerability['nikto_vulnerability']['XSS injection']['number']=self.nikto_vulnerability['nikto_vulnerability']['XSS injection']['number']+1
                            self.nikto_vulnerability['nikto_vulnerability']['XSS injection']["method_msg"].append([nikto_report_vulnerability['vulnerabilities'][i]['method'],nikto_report_vulnerability['vulnerabilities'][i]['msg'],nikto_report_vulnerability['vulnerabilities'][i]['url'],nikto_report_vulnerability['vulnerabilities'][i]['OSVDB']])


    def get_nikto_report(self):
         self.get_nikto_vulnerability("{}/Resaults/{}/nikto/{}_9".format(self.script_dir ,self.name,self.name))         
         self.get_nikto_vulnerability("{}/Resaults/{}/nikto/{}_4".format(self.script_dir ,self.name,self.name))
#     get_nikto_vulnerability("/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/{}/nikto/{}_f".format(name,name))
         #print("[Results]________________________________________Nikto Reporte:______________________________________________")
         #print("sql injection possiiblity:",self.nikto_vulnerability['nikto_vulnerability']['sql_injection']['number'])
         #print("XML injection possiiblity:",self.nikto_vulnerability['nikto_vulnerability']['XML injection']['number'])
         #print("script_injection possiiblity:",self.nikto_vulnerability['nikto_vulnerability']['script_injection']['number'])
         #print("sql information possiiblity:",self.nikto_vulnerability['nikto_vulnerability']['sql information']['number'])
         #print("html injection possiiblity:",self.nikto_vulnerability['nikto_vulnerability']['html injection']['number'])
         #print("XSLT_Extensible Stylesheet Language Transformations injection possiiblity:",self.nikto_vulnerability['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'])
         #print("remote source injection possiiblity:",self.nikto_vulnerability['nikto_vulnerability']['remote source injection']['number'])
         #print("XSS injection possiiblity:",self.nikto_vulnerability['nikto_vulnerability']['XSS injection']['number']) 
         return self.nikto_vulnerability

#starting_nikto = threading.Thread(target=start_nikto_get_report)
#starting_nikto.start() 

#______________________________________________________________nuclei _____________________________________________________________________________
    def start_nuclei(self):
         #print("[INFO] 		Nuclei Scan started:")
         output = subprocess.run("nuclei -u {} -tags cve -o {}/Resaults/{}/nuclei/{}.json -json -duc -ni ".format(self.url,self.script_dir ,self.name,self.name), shell=True, capture_output=True)
         #print("[finished] 		Nuclei scan finished")
    def list_the_Vuln_nuclei(self):
        data = []
        newdater=self.dater.copy()
        with open("{}/Resaults/{}/nuclei/{}.json".format(self.script_dir ,self.name,self.name)) as f:
            for line in f:
                data.append(json.loads(line)) 
        for i in data :
            newdater[i['info']['name']][0]=newdater[i['info']['name']][0]+1
            newdater[i['info']['name']][1].append(i['matched-at'])
            newdater[i['info']['name']][2].append(i['curl-command'])
            
        return newdater
     
    def my_filtering_function(self,pair):
        key, value = pair
        if value[0] <= 0:
            return False  # filter pair out of the dictionary
        else:
            return True  # keep pair in the filtered dictionary
    def nuclei_report(self):
               #start_nuclei()
               newdater=self.list_the_Vuln_nuclei() 
               filtered_grades = dict(filter(self.my_filtering_function, newdater.items()))
          #    print("[Resault]__________________________________Nuclei Resault:_________________________")
          #     print(filtered_grades)    
               return filtered_grades



"""




# https://www.zaproxy.org/docs/alerts/
#this commented part is  using Zap-cli "but it seems that it's no longer supported so we gonna us the new api devolped officiely by owaspZap"
#https://www.zaproxy.org/docs/api/ this is the api provided by the owasapzap officiel site <3 check it for more advance option "maybe in the future you would activate the passive scanners also"
     

#__________________________________________________________zap-cli___________________________________________
""""""
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
        output1= subprocess.run("zap-cli --zap-url http://0.0.0.0:8090/ -p 8090 report -f html -o /home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/{}/owaspzap/{}.html".format(name,name),shell=True,capture_output=True) 
        output1= subprocess.run("zap-cli --zap-url http://0.0.0.0:8090/ -p 8090 report -f xml -o /home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/{}/owaspzap/{}.xml".format(name,name),shell=True,capture_output=True) 
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
     with open('/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/{}/owaspzap/{}.xml'.format(name,name), 'r') as f:
         data = f.read() 
     bs_data = BeautifulSoup(data, 'xml') 
     b_alerts = bs_data.find_all('alert') 
     for i in b_alerts:
         print(i.text)
#         list_zap_vulnerabilities[i.text]=list_zap_vulnerabilities[i.text]+1
#     print(list_zap_vulnerabilities)
     return list_zap_vulnerabilities

get_zap_resaults(name)
""""""


#______________________________________________________________nuclei _____________________

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



   """
