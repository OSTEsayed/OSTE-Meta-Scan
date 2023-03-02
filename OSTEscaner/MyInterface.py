import tkinter
import threading

import tkinter.messagebox
import customtkinter
import time
import OSTEscaner
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class start_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x350")
        self.frame_main = customtkinter.CTkFrame(self)
        self.frame_main.pack(pady=20,padx=60,fill ="both",expand=True)
        self.label_main = customtkinter.CTkLabel(self.frame_main, text="Start The New Scan")
        self.label_main.pack(padx=20, pady=20)


        self.target_name=customtkinter.CTkEntry(self.frame_main,placeholder_text="Name of target")
        self.target_name.pack(pady=12,padx=10)

        self.target_url=customtkinter.CTkEntry(self.frame_main,placeholder_text="URL of target: (http://....)")
        self.target_url.pack(pady=12,padx=10)
        self.start_button=customtkinter.CTkButton(self.frame_main, text="Start Scanning",command=self.start_new_scan)
        self.start_button.pack(pady=12,padx=20)
        
        self.label_result = customtkinter.CTkLabel(self.frame_main, text="")
        self.label_result.pack(padx=20, pady=20)

    def start_new_scan(self):
        if self.target_name.get()=="":
            self.label_result.configure(text="Enter the name of target",text_color="red")

        if self.target_url.get()=="":
            self.label_result.configure(text="Enter Valide URL of target",text_color="red")
            print("Enter Valide name!!")
        else:										#scaning
            self.label_result.configure(text="Starting Scaning the target",text_color="green")            
            new_scan= OSTEscaner.scan()
            app.log_textbox.insert(tkinter.END, "\n [INFO] 		Creating Resaults Directory for each scanner", tags=None)
            new_scan.configuiring_new_scan(self.target_name.get(),self.target_url.get())
            new_scan.creat_directory()
            app.log_textbox.insert(tkinter.END, "\n [location]	        /home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/"+self.target_name.get(), tags=None)
            
            app.log_textbox.insert(tkinter.END, "\n [INFO] 		wapiti scan started", tags=None)
            starting_wapiti = threading.Thread(target=new_scan.start_wapiti)
            starting_wapiti.start() 
            app.log_textbox.insert(tkinter.END, "\n [INFO] 		skipfish scan started", tags=None)
            
            starting_skipfish = threading.Thread(target=new_scan.start_skipfish)
            starting_skipfish.start()

            app.log_textbox.insert(tkinter.END, "\n [INFO] 		OWASPZAP server started", tags=None)
            starting_zap_server = threading.Thread(target=new_scan.start_zap)
            starting_zap_server.start()
#            app.log_textbox.insert(tkinter.END, "\n [INFO] 		OWASPZAP Scanning started", tags=None)            
            starting_zap= threading.Thread(target=new_scan.check_for_zap)
            #starting_zap.start()
            app.log_textbox.insert(tkinter.END, "\n [INFO] 		NIKTO Scanning started", tags=None)            
            starting_nikto = threading.Thread(target=new_scan.start_nikto)
            starting_nikto.start() 
#            app.log_textbox.insert(tkinter.END, "\n [INFO] 		Nuclei Scanning started", tags=None)            
            starting_nuclei = threading.Thread(target=new_scan.start_nuclei)
            #starting_nuclei.start() 
            CHECKER = threading.Thread(target=self.check_for_finished,args=(starting_zap,starting_nikto,starting_nuclei,starting_wapiti,starting_skipfish,self.target_name.get()))
            CHECKER.start() 

#            new_scan.starting_all_scanner(self.target_name.get(),self.target_url.get())
    def check_for_finished(self,a,b,c,d,e,name):
                zap_statu,nikto_statu,nuclei_statu,wapiti_statu,skipfish_statu="notscanning","scanning","notscanning","scanning","scanning"
                zaper,nucleir="notyet","notyet"
                number_scaner=3 
                time.sleep(5)
                self.destroy()
                while number_scaner>0:
                  time.sleep(5)
                  if zaper=="lunch":
                      app.log_textbox.insert(tkinter.END, "\n [INFO] 		OWASPZAP Scanning started", tags=None)           
                      a.start()
                      zap_statu="scanning"
                      zaper="yet"
                  if nucleir=="lunch":
                      app.log_textbox.insert(tkinter.END, "\n [INFO] 		Nuclei Scanning started", tags=None)            
                      c.start()
                      nuclei_statu="scanning"
                      nucleir="yet"
                      time.sleep(1)                      
                  if zap_statu=="scanning":
                          if a.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished] 		OWASP ZAP Scanning Finished", tags=None)            
                              zap_statu="finished"
                              number_scaner-=1       	
                  if nikto_statu=="scanning":
                          if b.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished] 		NIKTO Scanning Finished", tags=None)            
                              nikto_statu="finished"
                              number_scaner-=1           
                  if nuclei_statu=="scanning":
                          if c.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished] 		Nuclei Scanning Finished", tags=None)            
                              nuclei_statu="finished"
                              number_scaner-=1 
                  if wapiti_statu=="scanning":
                          if d.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished] 		WAPITI Scanning Finished", tags=None)            
                              wapiti_statu="finished"
                              number_scaner-=1 
                  if skipfish_statu=="scanning":
                          if e.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished] 		SKIPFISH Scanning Finished", tags=None)            
                              skipfish_statu="finished"
                              number_scaner-=1  
                  if number_scaner==0 and zaper=="notyet":
                     number_scaner=2
                     zaper="lunch"
                     nucleir="lunch"
                  

                app.Load_resaults(name)













class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("OSTEscanner Web Vulnerability Scanner")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="OSTE Scanner", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.startnewscan_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_start_Window,text="Start New Scan",state="disabled")
        self.startnewscan_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:self.Load_resaults("skip_wapiti_nikto_zap_nuclei"),text="Load old Results")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.chec_for_scanner_sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.chec_for_scanner,text="check Scanners")
        self.chec_for_scanner_sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        
        self.wapiti = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.wapiti.grid(row=5, column=0, padx=20, pady=3)
        self.zap = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.zap.grid(row=6, column=0, padx=20, pady=3)
        self.nuclei = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.nuclei.grid(row=7, column=0, padx=20, pady=3)
        self.nikto = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.nikto.grid(row=8, column=0, padx=20, pady=3)
        self.skipfish = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.skipfish.grid(row=9, column=0, padx=20, pady=3)
        
        
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[ "System","Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 10))
       
        #loog textbox
        self.log_textbox = customtkinter.CTkTextbox(self, width=250)
        self.log_textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.log_textbox.insert(1.0, "\t here is The log of application:\n[note]to keep track of what's happening)", tags=None)
        self.start_Window = None
        
        
        # create tabview
        self.results_tabview = customtkinter.CTkTabview(self, width=600,height=300)
        self.results_tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.results_tabview.add("Our Resault")
        self.results_tabview.add("skipfish")
        self.results_tabview.add("wapiti")
        self.results_tabview.add("nikto")
        self.results_tabview.add("OWASP zap")
        self.results_tabview.add("Nuclei")
        #our resault tab view:
        self.label_1 = customtkinter.CTkLabel(self.results_tabview.tab("Our Resault"),text="Resault Table:", justify=customtkinter.CENTER)
        self.label_1.pack(pady=0, padx=0)
        
        
        self.my_frame = MyFrame_My_Result(master=self.results_tabview.tab("Our Resault"))
        self.my_frame.pack(fill="both",padx=0,pady=0,expand=True)        
        
        #wapiti Resault Tab View:
        self.label_3 = customtkinter.CTkLabel(self.results_tabview.tab("wapiti"),text="Resault Table:", justify=customtkinter.CENTER)
        self.label_3.pack(pady=0, padx=0)
        self.my_frameWapiti = MyFrame_My_wapiti(master=self.results_tabview.tab("wapiti"))
        self.my_frameWapiti.pack(fill="both",padx=0,pady=0,expand=True)        
        
    def print_wapiti_Result(self,name):
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            number,detaille =new_scaner.get_wapiti_resaults()
            nuumeb=1
            if number['Blind SQL Injection'] > 0:
                   self.my_frame.vul_label[1][1].configure(text_color="red",text=int(self.my_frame.vul_label[1][1].cget("text"))+number['Blind SQL Injection'])
                   if "Wapiti" not in self.my_frame.vul_label[1][2].cget("text"):
                        if self.my_frame.vul_label[1][2].cget("text") =="None": self.my_frame.vul_label[1][2].configure(text="")
                        self.my_frame.vul_label[1][2].configure(text=self.my_frame.vul_label[1][2].cget("text")+" Wapiti \n")
            if number['SQL Injection'] > 0:
                   self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+number['SQL Injection'])
                   if "Wapiti" not in self.my_frame.vul_label[0][2].cget("text"):
                        if self.my_frame.vul_label[0][2].cget("text") =="None": self.my_frame.vul_label[0][2].configure(text="")
                        self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+" Wapiti \n")
            if number['Cross Site Scripting'] > 0:
                   self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+number['Cross Site Scripting'])
                   if "Wapiti" not in self.my_frame.vul_label[2][2].cget("text"):
                        if self.my_frame.vul_label[2][2].cget("text") =="None": self.my_frame.vul_label[2][2].configure(text="")
                        self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+" Wapiti \n")
            if number['XML External Entity'] > 0:
                   self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+number['XML External Entity'])
                   if "Wapiti" not in self.my_frame.vul_label[6][2].cget("text"):
                        if self.my_frame.vul_label[6][2].cget("text") =="None": self.my_frame.vul_label[6][2].configure(text="")
                        self.my_frame.vul_label[6][2].configure(text=self.my_frame.vul_label[6][2].cget("text")+" Wapiti \n")                        
            if number['Command execution'] > 0:
                   self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+number['Command execution'])
                   if "Wapiti" not in self.my_frame.vul_label[7][2].cget("text"):
                        if self.my_frame.vul_label[7][2].cget("text") =="None": self.my_frame.vul_label[7][2].configure(text="")
                        self.my_frame.vul_label[7][2].configure(text=self.my_frame.vul_label[7][2].cget("text")+" Wapiti \n")
            if number['CRLF Injection'] > 0:
                   self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+number['CRLF Injection'])
                   if "Wapiti" not in self.my_frame.vul_label[11][2].cget("text"):
                        if self.my_frame.vul_label[11][2].cget("text") =="None": self.my_frame.vul_label[11][2].configure(text="")
                        self.my_frame.vul_label[11][2].configure(text=self.my_frame.vul_label[11][2].cget("text")+" Wapiti \n")
            
            
            
            #Print the resault in the wapiti tAB view:4
            xer="---------------------------------------------------------------------------------------------"
            for i in detaille: 
               if len(detaille[i])>0:
                  for j in detaille[i]:
                        self.vul=customtkinter.CTkLabel(self.my_frameWapiti,text=xer)
                        self.vul.grid(row=nuumeb, column=0,columnspan=4)
                        nuumeb=nuumeb+1
                        self.vul=customtkinter.CTkLabel(self.my_frameWapiti,text=i,width=150)
                        self.vul.grid(row=nuumeb, column=0)
                        self.http=customtkinter.CTkLabel(self.my_frameWapiti,text=j["http_request"],width=150)
                        self.http.grid(row=nuumeb, column=1)
                        self.info=customtkinter.CTkLabel(self.my_frameWapiti,text=j["info"],width=150)
                        self.info.grid(row=nuumeb, column=2)
                        nuumeb=nuumeb+1

    def print_skipfich_Result(self,name):
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            all_resaults =new_scaner.get_skipfish_resaults()   
            for i in all_resaults:
                 if all_resaults[i][1] >0:
                      if "SQL query or similar syntax in parameters" in all_resaults[i][0] :
                             self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[0][2].cget("text"):
                                 if self.my_frame.vul_label[0][2].cget("text") =="None": self.my_frame.vul_label[0][2].configure(text="")
                                 self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+"SkipFish \n")           
                      elif "XSS vector" in all_resaults[i][0] :
                             self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[2][2].cget("text"):
                                 if self.my_frame.vul_label[2][2].cget("text") =="None": self.my_frame.vul_label[2][2].configure(text="")
                                 self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+"SkipFish \n")           
                      elif "Shell injection" in all_resaults[i][0] :
                             self.my_frame.vul_label[3][1].configure(text_color="red",text=int(self.my_frame.vul_label[3][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[3][2].cget("text"):
                                 if self.my_frame.vul_label[3][2].cget("text") =="None": self.my_frame.vul_label[3][2].configure(text="")
                                 self.my_frame.vul_label[3][2].configure(text=self.my_frame.vul_label[3][2].cget("text")+"SkipFish \n")                   
                      elif "XML injection" in all_resaults[i][0] :
                             self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[5][2].cget("text"):
                                 if self.my_frame.vul_label[5][2].cget("text") =="None": self.my_frame.vul_label[5][2].configure(text="")
                                 self.my_frame.vul_label[5][2].configure(text=self.my_frame.vul_label[5][2].cget("text")+"SkipFish \n")           
                      elif "HTTP response header splitting" in all_resaults[i][0] :
                             self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[11][2].cget("text"):
                                 if self.my_frame.vul_label[11][2].cget("text") =="None": self.my_frame.vul_label[11][2].configure(text="")
                                 self.my_frame.vul_label[11][2].configure(text=self.my_frame.vul_label[11][2].cget("text")+"SkipFish \n")           
                      elif "OGNL-like parameter behavior" in all_resaults[i][0] :
                             self.my_frame.vul_label[12][1].configure(text_color="red",text=int(self.my_frame.vul_label[12][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[12][2].cget("text"):
                                 if self.my_frame.vul_label[12][2].cget("text") =="None": self.my_frame.vul_label[12][2].configure(text="")
                                 self.my_frame.vul_label[12][2].configure(text=self.my_frame.vul_label[12][2].cget("text")+"SkipFish \n")           
                      elif "HTTP header injection" in all_resaults[i][0] :
                             self.my_frame.vul_label[13][1].configure(text_color="red",text=int(self.my_frame.vul_label[13][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[13][2].cget("text"):
                                 if self.my_frame.vul_label[13][2].cget("text") =="None": self.my_frame.vul_label[13][2].configure(text="")
                                 self.my_frame.vul_label[13][2].configure(text=self.my_frame.vul_label[13][2].cget("text")+"SkipFish \n")           
                  
                  
                  #TODOOO ::::: PRINT RESAULT In SKIP FIsh Tab View like wapiti (bring the requast tags from resaults (modifie ostescanner code ,major work needed aghhh))
                  
    def print_Nikto_Result(self,name):
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            Nikto_resaults =new_scaner.get_nikto_report()    
            if Nikto_resaults['nikto_vulnerability']['sql_injection']['number'] >0:
                     self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['sql_injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[0][2].cget("text"):
                         if self.my_frame.vul_label[0][2].cget("text") =="None": self.my_frame.vul_label[0][2].configure(text="")
                         self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+"Nikto \n")                       
            
            if Nikto_resaults['nikto_vulnerability']['XSS injection']['number'] >0:
                     self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XSS injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[2][2].cget("text"):
                         if self.my_frame.vul_label[2][2].cget("text") =="None": self.my_frame.vul_label[2][2].configure(text="")
                         self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+"Nikto \n")                       
                       
            if Nikto_resaults['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'] >0:
                     self.my_frame.vul_label[4][1].configure(text_color="red",text=int(self.my_frame.vul_label[4][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[4][2].cget("text"):
                         if self.my_frame.vul_label[4][2].cget("text") =="None": self.my_frame.vul_label[4][2].configure(text="")
                         self.my_frame.vul_label[4][2].configure(text=self.my_frame.vul_label[4][2].cget("text")+"Nikto \n")                       

            if Nikto_resaults['nikto_vulnerability']['XML injection']['number'] >0:
                     self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XML injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[5][2].cget("text"):
                         if self.my_frame.vul_label[5][2].cget("text") =="None": self.my_frame.vul_label[5][2].configure(text="")
                         self.my_frame.vul_label[5][2].configure(text=self.my_frame.vul_label[5][2].cget("text")+"Nikto \n")                       

            if Nikto_resaults['nikto_vulnerability']['remote source injection']['number'] >0:
                     self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['remote source injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[7][2].cget("text"):
                         if self.my_frame.vul_label[7][2].cget("text") =="None": self.my_frame.vul_label[7][2].configure(text="")
                         self.my_frame.vul_label[7][2].configure(text=self.my_frame.vul_label[7][2].cget("text")+"Nikto \n")                       

            if Nikto_resaults['nikto_vulnerability']['html injection']['number'] >0:
                     self.my_frame.vul_label[9][1].configure(text_color="red",text=int(self.my_frame.vul_label[9][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['html injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[9][2].cget("text"):
                         if self.my_frame.vul_label[9][2].cget("text") =="None": self.my_frame.vul_label[9][2].configure(text="")
                         self.my_frame.vul_label[9][2].configure(text=self.my_frame.vul_label[9][2].cget("text")+"Nikto \n")                       


               #TODO Affichier raport Fel Nikto Tab  view ,(Rouh Lel  La Rapport tjib mno lurl wl method  wl msg )
          
    def print_zap_Result(self,name):                   #todo eglebha condition if >0 bh twli hamra (aaaghhhh) Wzid partye ta tzid esm scaner fki ydetecter
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            zap_resaults =new_scaner.owaspzap_get_resaults()               
#            print(zap_resaults)
            if zap_resaults["SQL Injection"]+zap_resaults["SQL Injection - MySQL"]+zap_resaults["SQL Injection - Hypersonic SQL"]+zap_resaults["SQL Injection - Oracle"]+zap_resaults["SQL Injection - PostgreSQL"]+zap_resaults["SQL Injection - SQLite"]+zap_resaults["SQL Injection - MsSQL"]  > 0 :
                 self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+zap_resaults["SQL Injection"]+zap_resaults["SQL Injection - MySQL"]+zap_resaults["SQL Injection - Hypersonic SQL"]+zap_resaults["SQL Injection - Oracle"]+zap_resaults["SQL Injection - PostgreSQL"]+zap_resaults["SQL Injection - SQLite"]+zap_resaults["SQL Injection - MsSQL"])
            if zap_resaults["Cross Site Scripting (Reflected)"]+zap_resaults["Cross Site Scripting (Persistent)"]+zap_resaults["Cross Site Scripting (Persistent) - Prime"]+zap_resaults["Cross Site Scripting (Persistent) - Spider"]+zap_resaults["Cross Site Scripting (DOM Based)"] > 0 :     
                 self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+zap_resaults["Cross Site Scripting (Reflected)"]+zap_resaults["Cross Site Scripting (Persistent)"]+zap_resaults["Cross Site Scripting (Persistent) - Prime"]+zap_resaults["Cross Site Scripting (Persistent) - Spider"]+zap_resaults["Cross Site Scripting (DOM Based)"])
            if zap_resaults["XSLT Injection"] > 0:
                  self.my_frame.vul_label[4][1].configure(text_color="red",text=int(self.my_frame.vul_label[4][1].cget("text"))+zap_resaults["XSLT Injection"])
            if zap_resaults["SOAP XML Injection"] >0 :
                  self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+zap_resaults["SOAP XML Injection"])
            if zap_resaults["XML External Entity Attack"] >0 :      
                  self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+zap_resaults["XML External Entity Attack"])
            if zap_resaults["Server Side Code Injection"]+zap_resaults["Server Side Code Injection - PHP Code Injection"]+zap_resaults["Server Side Code Injection - ASP Code Injection"]+zap_resaults["Remote Code Execution - CVE-2012-1823"] > 0 :
                  self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+zap_resaults["Server Side Code Injection"]+zap_resaults["Server Side Code Injection - PHP Code Injection"]+zap_resaults["Server Side Code Injection - ASP Code Injection"]+zap_resaults["Remote Code Execution - CVE-2012-1823"])
            if zap_resaults["Remote OS Command Injection"] > 0 :
                  self.my_frame.vul_label[8][1].configure(text_color="red",text=int(self.my_frame.vul_label[8][1].cget("text"))+zap_resaults["Remote OS Command Injection"])
            if zap_resaults["Server Side Template Injection"] > 0 :
                  self.my_frame.vul_label[10][1].configure(text_color="red",text=int(self.my_frame.vul_label[10][1].cget("text"))+zap_resaults["Server Side Template Injection"] )           
            if zap_resaults["CRLF Injection"] > 0:
                  self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+zap_resaults["CRLF Injection"])
            
            #TODO Affichier raport Fel Zap Tab  view ,(Rouh Lel  La Rapport tjib mno des info khlaf )
            
           
    def print_nuclei_Result(self,name):                   #todo eglebha condition if >0 bh twli hamra (aaaghhhh) Wzid partye ta tzid esm scaner fki ydetecter
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            nuclei_resaults =new_scaner.nuclei_report()               
            for i in nuclei_resaults:
                if "sql" in i.lower():
                   self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+1)            
                elif "blind sql" in i.lower():
                   self.my_frame.vul_label[1][1].configure(text_color="red",text=int(self.my_frame.vul_label[1][1].cget("text"))+1)
                elif "cross site scripting" in i.lower() or "xss" in i.lower():
                   self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+1)
                elif "shell" in i.lower():                
                   self.my_frame.vul_label[3][1].configure(text_color="red",text=int(self.my_frame.vul_label[3][1].cget("text"))+1)
                elif "xml external entity" in i.lower():                
                   self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+1)
                elif "xml entity" in i.lower():                
                   self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+1)
                elif "code" in i.lower():                
                   self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+1)
                elif "command" in i.lower():                
                   self.my_frame.vul_label[8][1].configure(text_color="red",text=int(self.my_frame.vul_label[8][1].cget("text"))+1)
                elif "html" in i.lower():                
                   self.my_frame.vul_label[9][1].configure(text_color="red",text=int(self.my_frame.vul_label[9][1].cget("text"))+1)
                elif "crlf" in i.lower():                
                   self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+1)
                elif "ognl" in i.lower():                
                   self.my_frame.vul_label[12][1].configure(text_color="red",text=int(self.my_frame.vul_label[12][1].cget("text"))+1)
                elif "host header" in i.lower():                
                   self.my_frame.vul_label[13][1].configure(text_color="red",text=int(self.my_frame.vul_label[13][1].cget("text"))+1)

    def chec_for_scanner(self):
            new_checker= OSTEscaner.scan_checker()
            Resault=new_checker.check()
            if Resault[0][0] ==True and Resault[1][0] ==True and Resault[2][0]==True and Resault[3][0] ==True and Resault[4][0] ==True :
                   self.chec_for_scanner_sidebar_button_3.configure(fg_color="green")
                   self.startnewscan_button_1.configure (state="normal")
                   self.wapiti.configure(text=Resault[0][1])
                   self.zap.configure(text=Resault[1][1])
                   self.nuclei.configure(text=Resault[2][1])
                   self.nikto.configure(text=Resault[3][1])
                   self.skipfish.configure(text=Resault[4][1])
        
#            print(Resault)
        
    def open_start_Window(self):
        if self.start_Window is None or not self.start_Window.winfo_exists():
            self.start_Window = start_Window(self)  # create window if its None or destroyed
        else:
            self.start_Window.focus()
            
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
#        customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def Load_resaults(self,name):
        for i in self.my_frame.vul_label:
            i[1].configure(text=int(0))
        self.print_wapiti_Result(name)
        self.print_skipfich_Result(name) 
        self.print_Nikto_Result(name)
        self.print_zap_Result(name)
        print("sidebar_button click")

class MyFrame_My_wapiti(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self,text="Vulnerability ",width=150)

        self.label.grid(row=0, column=0,padx=3,pady=3)
        self.label1 = customtkinter.CTkLabel(self,text="http_request",width=150)
        self.label1.grid(row=0, column=1,padx=3,pady=3)
        self.label2 = customtkinter.CTkLabel(self,text="info",width=150)
        self.label2.grid(row=0, column=2,padx=3,pady=3)
#        self.label3 = customtkinter.CTkLabel(self,text="Action",width=80)
#        self.label3.grid(row=0, column=3,padx=3,pady=3,sticky="nsew")    
        
        


class MyFrame_My_Result(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame...borderwidth
        self.label = customtkinter.CTkLabel(self,text="Vulnerability ",width=250)

        self.label.grid(row=0, column=0,padx=3,pady=3)
        self.label1 = customtkinter.CTkLabel(self,text="Exist",width=50)
        self.label1.grid(row=0, column=1,padx=3,pady=3)
        self.label2 = customtkinter.CTkLabel(self,text="Scanners",width=150)
        self.label2.grid(row=0, column=2,padx=3,pady=3)
        self.label3 = customtkinter.CTkLabel(self,text="Action",width=80)
        self.label3.grid(row=0, column=3,padx=3,pady=3,sticky="nsew")    
        self.vul_label=[]
        xer="_______________________________________________________________________________________________"
        for i in range(14):
            temp=[]
            self.labeltemp=customtkinter.CTkLabel(self,text=xer,fg_color="transparent")
            self.labeltemp.grid(row=i+1, column=0,columnspan=4,pady=(40,0))

            self.labeltemp=customtkinter.CTkLabel(self,text=" injection:",width=250,fg_color="transparent")
            self.labeltemp.grid(row=i+1, column=0)
            self.labeltemp1=customtkinter.CTkLabel(self,text=int(0),width=50,fg_color="transparent")
            self.labeltemp1.grid(row=i+1, column=1)
            self.labeltemp2=customtkinter.CTkLabel(self,text="None",width=120,fg_color="transparent")
            self.labeltemp2.grid(row=i+1, column=2)
            self.but=customtkinter.CTkButton(self,text="check" ,state="disabled",width=80 , height=35)
            self.but.grid(row=i+1, column=3,padx=3,pady=(5,30),sticky="nsew")
            self.vul_label.append([self.labeltemp,self.labeltemp1,self.labeltemp2,self.but])

        self.vul_label[0][0].configure(text="SQL injection:")
        self.vul_label[0][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        
        self.vul_label[1][0].configure(text="Blind SQL injection:")
        self.vul_label[1][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[2][0].configure(text="Cross Site Scripting injection:")
        self.vul_label[2][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[3][0].configure(text="Shell injection:")
        self.vul_label[3][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[4][0].configure(text="XSLT injection:")
        self.vul_label[4][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[5][0].configure(text="XML injection:")
        self.vul_label[5][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[6][0].configure(text="XML external entities (XXE) :")
        self.vul_label[6][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[7][0].configure(text="code injection:")
        self.vul_label[7][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[8][0].configure(text="OS command injection:")
        self.vul_label[8][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[9][0].configure(text="html injection:")
        self.vul_label[9][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[10][0].configure(text="Template injection:")
        self.vul_label[10][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[11][0].configure(text="CRLF injection:")
        self.vul_label[11][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[12][0].configure(text="OGNL injection:")
        self.vul_label[12][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))
        self.vul_label[13][0].configure(text="Host Header injection:")
        self.vul_label[13][3].configure(command=lambda:self.getresault(self.vul_label[0][0]))

    def getresault(self,injectiontype):
         print(injectiontype)
                 
if __name__ == "__main__":
    app = App()
    app.mainloop()
