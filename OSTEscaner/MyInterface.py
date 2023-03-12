import tkinter
import threading
import webbrowser
import tkinter.messagebox
import customtkinter
import time
import OSTEscaner
import os,shutil
import subprocess
import signal
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class MyResultFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)
        self.mylist=os.listdir("/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/")
        self.radio_var = tkinter.IntVar(value=0)
        for i in range(len(self.mylist)):
                self.radio_button_1 = customtkinter.CTkRadioButton(master=self,text=self.mylist[i], variable=self.radio_var, value=i)
                self.radio_button_1.grid(row=int(i/3), column=int(i%3), pady=10, padx=20, sticky="n")
        print(self.radio_var)     
        
        
class Target_Window(customtkinter.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        xer="_____________________________________________________"
        self.path="/home/ostesayed/Desktop/Scanners/OSTE-Scanner/Targets/"
        self.geometry("600x350")
        self.frame_main = customtkinter.CTkFrame(self)
        self.frame_main.pack(pady=10,padx=10,fill ="both",expand=True)
        self.label_main=customtkinter.CTkLabel(self.frame_main,text="Npm Target List:").pack(pady=10,padx=10)
        self.mylist=os.listdir(self.path)
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_main,text="None", variable=self.radio_var, value=0)
        self.radio_button_1.pack(pady=5,padx=5)
        for i in range(len(self.mylist)):
                self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_main,text=self.mylist[i], variable=self.radio_var, value=i+1)
                self.radio_button_1.pack(pady=5,padx=5)
        print(self.radio_var)     
        self.npmTarget = customtkinter.CTkButton(self, command=self.npmstart ,text="Start Npm Target")
        self.XampTarget = customtkinter.CTkButton(self, command=self.xampstart ,text="Start Xamp")
        self.npmTarget.pack(padx=(40,5),side="left")
        self.XampTarget.pack(padx=(5,40),side="right")
   
    def npmstart(self):
        self.frame_main.pack_forget()
        self.npmTarget.pack_forget()
        self.XampTarget.pack_forget()
        self.log_textbox = customtkinter.CTkTextbox(self, width=200)
        self.log_textbox.pack(padx=10, pady=10,fill ="both",expand=True)
        self.log_textbox.tag_add("red", 0.0, 0.5)
        self.log_textbox.tag_config("red",foreground="red",underline=1)
        self.log_textbox.tag_config("yellow",foreground="yellow")
        self.log_textbox.tag_config("green",foreground="lightgreen")
        
        self.log_textbox.tag_add("yellow", 0.0, 0.5)
        self.log_textbox.tag_add("green", 0.0, 0.5)
        self.log_textbox.insert(1.0, "\t Starting Target.... :\n", tags="red")

        self.process = subprocess.Popen("npm start", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,cwd=f"{self.path}/{self.mylist[self.radio_var.get()-1]}/")       #path li fe cwd mazalt majerbtouch 3les problem:
        pid = int(self.process.pid)
        starting= threading.Thread(target=self.start)
        starting.start() 
        
        self.stop_button = customtkinter.CTkButton(self, text="Stop The Target", command=lambda: os.kill(pid, signal.SIGTERM)) 
        self.stop_button.pack()
        print(f"ok with {self.mylist[self.radio_var.get()-1]}")
        
    def start(self):
   
        line = self.process.stdout.readline()
        if not line:
            time.sleep(10)
            print("no line")
        self.log_textbox.insert(tkinter.END, line.decode())
        self.log_textbox.see(tkinter.END)
        time.sleep(3)
        self.start()       

              
        
    def xampstart(self):
        self.frame_main.pack_forget()
        self.npmTarget.pack_forget()
        self.XampTarget.pack_forget()
        self.log_textbox = customtkinter.CTkTextbox(self, width=200)
        self.log_textbox.pack(padx=10, pady=10,fill ="both",expand=True)

        cmd = "sudo /opt/lampp/lampp start"
#        cmd="sudo ls -l"
        password = tkinter.simpledialog.askstring("Password", "Enter your password:(Required)", show='*')
        process = os.popen('echo {} | {} -S {}'.format(password, "sudo", cmd))

# Insert the output into the text widget
        self.log_textbox.insert(tkinter.END, "Command output:\n")

        for line in process:
           self.log_textbox.insert(tkinter.END, line)
           
        self.stop_button = customtkinter.CTkButton(self, text="Stop The Target", command=self.xampstop) 
        self.stop_button.pack()

        print("ok")
    def xampstop(self):
        cmd = "sudo /opt/lampp/lampp stop"
#        cmd="sudo ls -l"
        password = tkinter.simpledialog.askstring("Password", "Enter your password:(Required)", show='*')
        process = os.popen('echo {} | {} -S {}'.format(password, "sudo", cmd))

# Insert the output into the text widget
        self.log_textbox.insert(tkinter.END, "Command output:\n")

        for line in process:
           self.log_textbox.insert(tkinter.END, line)
           
       







         
class loadResult_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.frame_main = customtkinter.CTkFrame(self)
        self.frame_main.pack(pady=10,padx=10,fill ="both",expand=True)
        self.label =customtkinter.CTkLabel(self.frame_main,text="Chose Result:")
        self.label.pack(padx=20,pady=20)
        
        self.resultf =MyResultFrame (self.frame_main,height=200)
        self.resultf.pack(padx=10,pady=0,fill="x")
        self.check = customtkinter.CTkButton(self.frame_main, command=self.cchek ,text="Check")
        self.delete = customtkinter.CTkButton(self.frame_main, command=self.ddelete ,text="Delete")
        self.check.pack(padx=(40,5),side="left")
        self.delete.pack(padx=(5,40),side="right")
    def cchek(self):
        app.Load_resaults(self.resultf.mylist[self.resultf.radio_var.get()])
        self.destroy()
    def ddelete(self):
        shutil.rmtree("/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/{}".format(self.resultf.mylist[self.resultf.radio_var.get()]))        
        self.destroy()
        
        
        
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
            app.log_textbox.insert(tkinter.END, "\n[Starting]", tags="green") 
            app.log_textbox.insert(tkinter.END, "\t\tCreating Resaults Directory for each scanner", tags=None)
            new_scan.configuiring_new_scan(self.target_name.get(),self.target_url.get())
            new_scan.creat_directory()
            app.log_textbox.insert(tkinter.END, "\n[Location]", tags="green") 
            app.log_textbox.insert(tkinter.END, "\t\t/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/"+self.target_name.get(), tags=None)
            app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")      
            app.log_textbox.insert(tkinter.END, "\t\twapiti scan started", tags=None)
            starting_wapiti = threading.Thread(target=new_scan.start_wapiti)
            starting_wapiti.start() 
            app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")      	
            app.log_textbox.insert(tkinter.END, "\t\tskipfish scan started", tags=None)
            
            starting_skipfish = threading.Thread(target=new_scan.start_skipfish)
            starting_skipfish.start()
            app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="green")      
            app.log_textbox.insert(tkinter.END, "\t\tOWASPZAP server started", tags=None)
            
            starting_zap_server = threading.Thread(target=new_scan.start_zap)
            starting_zap_server.start()
#            app.log_textbox.insert(tkinter.END, "\n [INFO] 		OWASPZAP Scanning started", tags=None)            
            starting_zap= threading.Thread(target=new_scan.check_for_zap)
            #starting_zap.start()
            app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")                  
            app.log_textbox.insert(tkinter.END, "\t\tNIKTO Scanning started", tags=None)            
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
                      app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")            
                      app.log_textbox.insert(tkinter.END, "\t\tOWASPZAP Scanning started", tags=None)           
                      a.start()
                      zap_statu="scanning"
                      zaper="yet"
                  if nucleir=="lunch":
                      app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")            
                      app.log_textbox.insert(tkinter.END, "\t\tNuclei Scanning started", tags=None)            
                      c.start()
                      nuclei_statu="scanning"
                      nucleir="yet"
                      time.sleep(1)                      
                  if zap_statu=="scanning":
                          if a.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")            
                              app.log_textbox.insert(tkinter.END, "\t\tOWASP ZAP Scanning Finished", tags=None)            
                              zap_statu="finished"
                              number_scaner-=1       	
                  if nikto_statu=="scanning":
                          if b.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")            
                              app.log_textbox.insert(tkinter.END, "\t\tNIKTO Scanning Finished", tags=None)            
                              nikto_statu="finished"
                              number_scaner-=1           
                  if nuclei_statu=="scanning":
                          if c.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")            
                              app.log_textbox.insert(tkinter.END, "\t\tNuclei Scanning Finished", tags=None)            
                              nuclei_statu="finished"
                              number_scaner-=1 
                  if wapiti_statu=="scanning":
                          if d.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")            
                              app.log_textbox.insert(tkinter.END, "\t\tWAPITI Scanning Finished", tags=None)            
                              wapiti_statu="finished"
                              number_scaner-=1 
                  if skipfish_statu=="scanning":
                          if e.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")                                      
                              app.log_textbox.insert(tkinter.END, "\t\tSKIPFISH Scanning Finished", tags=None)            
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


        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
 #       self.attributes('-fullscreen',True)
        
        #configure the menu:
        
        self.menubar = tkinter.Menu(self, bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))

        self.config(menu=self.menubar)
        
        self.file_menu = tkinter.Menu(self.menubar ,bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
        self.file_menu.add_command(label='New Scan',command=self.open_start_Window)
        self.file_menu.add_command(label='Load Scan Result',command=self.open_load_Window)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Check Scanners integrity',command=self.chec_for_scanner)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',command=self.destroy)
        self.menubar.add_cascade(label="File", menu=self.file_menu,underline=0)
        
        self.target_menu = tkinter.Menu(self.menubar ,bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
        self.target_menu.add_command(label='lunch target',command=self.open_target_Window)
        self.menubar.add_cascade(label="Target", menu=self.target_menu,underline=0)

        
        self.view_menu=tkinter.Menu(self.menubar,bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
        
        self.modes_menu = tkinter.Menu(self.view_menu, tearoff=0,bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
        self.modes_menu.add_command(label='System ModeThemes',command=lambda:self.change_appearance_mode_event("System"))
        self.modes_menu.add_command(label='light Mode',command=lambda:self.change_appearance_mode_event("Light"))
        self.modes_menu.add_command(label='dark Mode',command=lambda:self.change_appearance_mode_event("Dark"))
        


        self.view_menu.add_cascade(label='Change Appearance',menu=self.modes_menu)
        self.menubar.add_cascade(label="View", menu=self.view_menu,underline=0)
       
        
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
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_load_Window,text="Load old Results")
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
        self.log_textbox = customtkinter.CTkTextbox(self, width=200)
        self.log_textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.log_textbox.insert(1.0, "\t here is The log of application:\n[note]to keep track of what's happening)", tags=None)
        self.log_textbox.tag_add("red", 0.0, 0.5)
        self.log_textbox.tag_config("red",foreground="red",underline=1)
        self.log_textbox.tag_add("yellow", 0.0, 0.5)
        self.log_textbox.tag_config("yellow",foreground="yellow")
        self.log_textbox.tag_add("green", 0.0, 0.5)
        self.log_textbox.tag_config("green",foreground="lightgreen")
        
        self.start_Window = None
        self.loadResult_window =None
        self.Target_Window=None
        # create tabview
        self.results_tabview = customtkinter.CTkTabview(self, width=800,height=300)
        self.results_tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.results_tabview.add("Our Result")
        self.results_tabview.add("Skipfish")
        self.results_tabview.add("wapiti")
        self.results_tabview.add("Nikto")
        self.results_tabview.add("OWASP ZAP")
        self.results_tabview.add("Nuclei")
        #our resault tab view:
        self.label_1 = customtkinter.CTkLabel(self.results_tabview.tab("Our Result"),text="Result Table:", justify=customtkinter.CENTER)
        self.label_1.pack(pady=0, padx=0)
        
        
        
        #wapiti Resault Tab View:
        self.label_3 = customtkinter.CTkLabel(self.results_tabview.tab("wapiti"),text="Result Table:", justify=customtkinter.CENTER)
        self.label_3.pack(pady=0, padx=0)
        
        #zap Resault Tab View:
        self.label_4 = customtkinter.CTkLabel(self.results_tabview.tab("OWASP ZAP"),text="Result Table:", justify=customtkinter.CENTER)
        self.label_4.pack(pady=0, padx=0)
        #Nikto Reslt Tab View:
        self.label_5 = customtkinter.CTkLabel(self.results_tabview.tab("Nikto"),text="Result Table:", justify=customtkinter.CENTER)
        self.label_5.pack(pady=0, padx=0)
        #Nuclei Result Tab Viwe :
        self.label_5 = customtkinter.CTkLabel(self.results_tabview.tab("Nuclei"),text="Result Table:", justify=customtkinter.CENTER)
        self.label_5.pack(pady=0, padx=0)
        
        #skipfish Result Tab Viwe :
        self.label_5 = customtkinter.CTkLabel(self.results_tabview.tab("Skipfish"),text="Result Table:", justify=customtkinter.CENTER)
        self.label_5.pack(pady=0, padx=0)
        
        self.createResaults()
        
        self.Results=[None,None,None,None,None]
        
        
        
    def open_check(self,ID):  
        
        self.CheckVul = customtkinter.CTkFrame(self, width=600)
        self.CheckVul.grid(row=1,rowspan=2, column=1,columnspan=2, padx=(5, 0), pady=(5, 0), sticky="nsew")
        
        self.close =customtkinter.CTkButton(self.CheckVul,text="X",width=20,height=20,fg_color='red',command=self.close_check)
        self.close.pack(pady=0,padx=0,side="right",anchor="ne")          
        self.CheckVul_in = customtkinter.CTkFrame(self.CheckVul)
        self.CheckVul_in.pack(pady=0,padx=0,fill="both",expand=True)
        
        self.CheckVul_in_description=customtkinter.CTkLabel(self.CheckVul_in,text="Description",width=550)
        self.CheckVul_in_Method_http=customtkinter.CTkLabel(self.CheckVul_in,text="Method \n http Request",width=200)        
        self.CheckVul_in_Vector=customtkinter.CTkLabel(self.CheckVul_in,text="Vector | command",width=250)
        self.CheckVul_in_Vulnerability=customtkinter.CTkLabel(self.CheckVul_in,text="Vulnerability",width=150)                
        self.CheckVul_in_Vulnerability.grid(row=0,column=0,padx=0)
        self.CheckVul_in_Method_http.grid(row=0,column=1,padx=0)
        self.CheckVul_in_Vector.grid(row=0,column=2,padx=0)
        self.CheckVul_in_description.grid(row=0,column=3,padx=0)
        xer="_______________________________________________________________________________________________________________________________________________________________________________________________________"
        self.labelll=customtkinter.CTkLabel(self.CheckVul_in,text=xer,height=2).grid(pady=0,row=1,column=0,columnspan=4)
        
        self.name=customtkinter.CTkLabel(self.CheckVul_in,text=ID).grid(pady=(20,20),padx=0,row=2,column=0)     
    
        self.http=customtkinter.CTkTextbox(self.CheckVul_in,width=200,height=280,fg_color="transparent",border_width=1,border_color="white",corner_radius=0)
#        self.http.insert(tkinter.END, "\ntest")
        self.http.grid(row=2, column=1,sticky="w",padx=0)

        self.command=customtkinter.CTkTextbox(self.CheckVul_in,width=250,height=280,fg_color="transparent",border_width=1,border_color="white",corner_radius=0)
        self.command.grid(row=2, column=2,sticky="w",padx=0)
        self.desc=customtkinter.CTkTextbox(self.CheckVul_in,width=500,height=280,fg_color="transparent",border_width=1,border_color="white",corner_radius=0,font=("ariel",15))
        self.desc.tag_add("red", 0.0, 0.5)
        self.desc.tag_config("red",foreground="red",underline=1)       
        self.desc.grid(row=2, column=3,sticky="w",padx=0)
        num=0
        
        
        
        if ("SQL Injection" in ID):        
                self.desc.insert(tkinter.END, "SQL injection vulnerabilities allow an attacker to alter the queries executed on the backend database. An attacker may then be able to extract or modify information stored in the database or even escalate his privileges on the system.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"To protect against SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.")

                for i in range(len(self.Results[0]["SQL Injection"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} ||URL:{}\n".format(num,self.Results[0]["SQL Injection"][i]["method"],self.Results[0]["SQL Injection"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}".format(num,self.Results[0]["SQL Injection"][i]["parameter"]))                     

                            #Skipfish tyhto fl Sql injection.
                if self.Results[2]['nikto_vulnerability']['sql_injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['sql_injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['sql_injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['sql_injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:".format(num) )                     
                 
                if self.Results[3]["SQL Injection"][0]+self.Results[3]["SQL Injection - MySQL"][0]+self.Results[3]["SQL Injection - Hypersonic SQL"][0]+self.Results[3]["SQL Injection - Oracle"][0]+self.Results[3]["SQL Injection - PostgreSQL"][0]+self.Results[3]["SQL Injection - SQLite"][0]+self.Results[3]["SQL Injection - MsSQL"][0]  > 0 :
                       for i in range(self.Results[3]["SQL Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection"][1][i] ,self.Results[3]["SQL Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["SQL Injection"][3][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - MySQL"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - MySQL"][1][i] ,self.Results[3]["SQL Injection - MySQL"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["SQL Injection - MySQL"][3][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - Hypersonic SQL"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - Hypersonic SQL"][1][i] ,self.Results[3]["SQL Injection - Hypersonic SQL"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["SQL Injection - Hypersonic SQL"][3][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - Oracle"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - Oracle"][1][i] ,self.Results[3]["SQL Injection - Oracle"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["SQL Injection - Oracle"][3][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - PostgreSQL"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - PostgreSQL"][1][i] ,self.Results[3]["SQL Injection - PostgreSQL"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["SQL Injection - PostgreSQL"][3][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - SQLite"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - SQLite"][1][i] ,self.Results[3]["SQL Injection - SQLite"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["SQL Injection - SQLite"][3][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - MsSQL"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - MsSQL"][1][i] ,self.Results[3]["SQL Injection - MsSQL"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["SQL Injection - MsSQL"][3][i]) )                     
 
                for i in self.Results[4]:
                    if "sql" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}\n".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     
              
        if ("Blind SQL injection" in ID):     
                self.desc.insert(tkinter.END, "Blind SQL injection is a technique that exploits a vulnerability occurring in the database of an application. This kind of vulnerability is harder to detect than basic SQL injections because no error message will be displayed on the webpage.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Same as Sql injection To protect against blind SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.")

                for i in range(len(self.Results[0]["Blind SQL Injection"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} |\n|URL:{}\n".format(num,self.Results[0]["Blind SQL Injection"][i]["method"],self.Results[0]["Blind SQL Injection"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}".format(num,self.Results[0]["Blind SQL Injection"][i]["parameter"]))                     
                for i in self.Results[4]:
                    if "blind sql" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     

        if ("Cross Site Scripting injection" in ID):     
                self.desc.insert(tkinter.END, "Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications which allow code injection by malicious web users into the web pages viewed by other users. Examples of such code include HTML code and client-side scripts.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"The best way to protect a web application from XSS attacks is ensure that the application performs validation of all headers, cookies, query strings, form fields, and hidden fields. Encoding user supplied output in the server side can also defeat XSS vulnerabilities by preventing inserted scripts from being transmitted to users in an executable form. Applications can gain significant protection from javascript based attacks by converting the following characters in all generated output to the appropriate HTML entity encoding:<, >, &, ', (, ), #, %, ; , +, -")

                for i in range(len(self.Results[0]["Cross Site Scripting"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} |\n|URL:{}\n".format(num,self.Results[0]["Cross Site Scripting"][i]["method"],self.Results[0]["Cross Site Scripting"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}".format(num,self.Results[0]["Cross Site Scripting"][i]["parameter"]))        
                              
                if self.Results[2]['nikto_vulnerability']['XSS injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['XSS injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['XSS injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['XSS injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:".format(num) )       
                           
                                        
                if self.Results[3]["Cross Site Scripting (DOM Based)"][0]+self.Results[3]["Cross Site Scripting (Reflected)"][0]+self.Results[3]["Cross Site Scripting (Persistent)"][0]+self.Results[3]["Cross Site Scripting (Persistent) - Prime"][0]+self.Results[3]["Cross Site Scripting (Persistent) - Spider"][0]  > 0 :
                       for i in range(self.Results[3]["Cross Site Scripting (DOM Based)"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (DOM Based)"][1][i] ,self.Results[3]["Cross Site Scripting (DOM Based)"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Cross Site Scripting (DOM Based)"][3][i]) )
                       for i in range(self.Results[3]["Cross Site Scripting (Reflected)"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (Reflected)"][1][i] ,self.Results[3]["Cross Site Scripting (Reflected)"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Cross Site Scripting (Reflected)"][3][i]) )
                       for i in range(self.Results[3]["Cross Site Scripting (Persistent)"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent)"][1][i] ,self.Results[3]["Cross Site Scripting (Persistent)"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Cross Site Scripting (Persistent)"][3][i]) )
                       for i in range(self.Results[3]["Cross Site Scripting (Persistent) - Prime"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent) - Prime"][1][i] ,self.Results[3]["Cross Site Scripting (Persistent) - Prime"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Cross Site Scripting (Persistent) - Prime"][3][i]) )
                       for i in range(self.Results[3]["Cross Site Scripting (Persistent) - Spider"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent) - Spider"][1][i] ,self.Results[3]["Cross Site Scripting (Persistent) - Spider"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Cross Site Scripting (Persistent) - Spider"][3][i]) )

                for i in self.Results[4]:
                    if "cross"in i.lower() and "site"in i.lower() and "scripting" in i.lower() or "xss" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     

                if self.Results[1]['40101'][1] >0:
                     for i in range(self.Results[1]['40101'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['40101'][2][i][0],self.Results[1]['40101'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None".format(num) )                     
                if self.Results[1]['40105'][1] >0:
                     for i in range(self.Results[1]['40105'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['40105'][2][i][0],self.Results[1]['40105'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None".format(num) )
                if self.Results[1]['40102'][1] >0:
                     for i in range(self.Results[1]['40102'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['40102'][2][i][0],self.Results[1]['40102'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None".format(num) )

        if ("Shell injection" in ID):    
                self.desc.insert(tkinter.END, "Check For it\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Double Check for it")
                if self.Results[1]['50102'][1] >0:
                     for i in range(self.Results[1]['50102'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['50102'][2][i][0],self.Results[1]['50102'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None".format(num) )                             
                for i in self.Results[4]:
                    if "shell" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     
         
        if ("XSLT injection" in ID):         
                self.desc.insert(tkinter.END, "Check For it\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Double Check for it")
                if self.Results[2]['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:".format(num) )       
                                        
                if self.Results[3]["XSLT Injection"][0] > 0 :
                       for i in range(self.Results[3]["XSLT Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["XSLT Injection"][1][i] ,self.Results[3]["XSLT Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["XSLT Injection"][3][i]) )
                            
        if ("XML injection" in ID):         
                self.desc.insert(tkinter.END, "Check For it\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Double Check for it")         
                if self.Results[1]['50101'][1] >0:
                     for i in range(self.Results[1]['50101'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['50101'][2][i][0],self.Results[1]['50101'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None".format(num) )  
                                                      
                if self.Results[2]['nikto_vulnerability']['XML injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['XML injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['XML injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['XML injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:".format(num) )       
                if self.Results[3]["SOAP XML Injection"][0] > 0 :
                       for i in range(self.Results[3]["XSLT Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SOAP XML Injection"][1][i] ,self.Results[3]["SOAP XML Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["SOAP XML Injection"][3][i]) )
         
                for i in self.Results[4]:
                    if "xml"in i.lower() and "external" not in i.lower() and "entity" not in i.lower():                               
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     
         
        if ("XML external entities (XXE)" in ID):    
                self.desc.insert(tkinter.END, "An XML External Entity attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"The safest way to prevent XXE is always to disable DTDs (External Entities) completely.")         

                for i in range(len(self.Results[0]["XML External Entity"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} |\n|URL:{}\n".format(num,self.Results[0]["XML External Entity"][i]["method"],self.Results[0]["XML External Entity"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}".format(num,self.Results[0]["XML External Entity"][i]["parameter"]))                            
                if self.Results[3]["XML External Entity Attack"][0] > 0 :
                       for i in range(self.Results[3]["XSLT Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["XML External Entity Attack"][1][i] ,self.Results[3]["XML External Entity Attack"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["XML External Entity Attack"][3][i]) )
                for i in self.Results[4]:
                    if "xml"in i.lower() and "external"  in i.lower() and "entity" in i.lower():                               
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                               
                  
        if ("code injection" in ID):    
                self.desc.insert(tkinter.END, "check for it (check in my Thesis)\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"search for it")    
                     
                if self.Results[2]['nikto_vulnerability']['remote source injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['remote source injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['remote source injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['remote source injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:".format(num) )                         
                             
         
                if self.Results[3]["Server Side Code Injection"][0]+self.Results[3]["Server Side Code Injection - PHP Code Injection"][0]+self.Results[3]["Server Side Code Injection - ASP Code Injection"][0]+self.Results[3]["Remote Code Execution - CVE-2012-1823"][0] > 0 :
                       for i in range(self.Results[3]["Remote Code Execution - CVE-2012-1823"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Remote Code Execution - CVE-2012-1823"][1][i] ,self.Results[3]["Remote Code Execution - CVE-2012-1823"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Remote Code Execution - CVE-2012-1823"][3][i]) )                     
                       for i in range(self.Results[3]["Server Side Code Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Server Side Code Injection"][1][i] ,self.Results[3]["Server Side Code Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Server Side Code Injection"][3][i]) )                     
                       for i in range(self.Results[3]["Server Side Code Injection - PHP Code Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Server Side Code Injection - PHP Code Injection"][1][i] ,self.Results[3]["Server Side Code Injection - PHP Code Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Server Side Code Injection - PHP Code Injection"][3][i]) )                     
                       for i in range(self.Results[3]["Server Side Code Injection - ASP Code Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Server Side Code Injection - ASP Code Injection"][1][i] ,self.Results[3]["Server Side Code Injection - ASP Code Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Server Side Code Injection - ASP Code Injection"][3][i]) )                     

                for i in self.Results[4]:
                    if "code" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     

        if ("OS command injection" in ID):    
                self.desc.insert(tkinter.END, "This attack consists in executing system commands on the server. The attacker tries to inject this commands in the request parameters.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Prefer working without user input when using file system calls.")  

                for i in range(len(self.Results[0]["Command execution"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} |\n|URL:{}\n".format(num,self.Results[0]["Command execution"][i]["method"],self.Results[0]["Command execution"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}".format(num,self.Results[0]["Command execution"][i]["parameter"]))        
                
                          
                if self.Results[3]["Remote OS Command Injection"][0] > 0 :
                       for i in range(self.Results[3]["Remote OS Command Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Remote OS Command Injection"][1][i] ,self.Results[3]["Remote OS Command Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Remote OS Command Injection"][3][i]) )                     
                for i in self.Results[4]:
                    if "command" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     
        if ("html injection" in ID):        
                self.desc.insert(tkinter.END, "check for it\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"searchh about it")
                if self.Results[2]['nikto_vulnerability']['html injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['html injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['html injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['html injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:".format(num) )       


                for i in self.Results[4]:
                    if "html" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     

        if ("Template injection" in ID):        
                self.desc.insert(tkinter.END, "check for it\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"searchh about it")
                if self.Results[3]["Remote OS Command Injection"][0] > 0 :
                       for i in range(self.Results[3]["Server Side Template Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Server Side Template Injection"][1][i] ,self.Results[3]["Server Side Template Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["Server Side Template Injection"][3][i]))                     
        if ("CRLF injection" in ID):        
                self.desc.insert(tkinter.END, "The term CRLF refers to Carriage Return (ASCII 13, \\r) Line Feed (ASCII 10, \\n). A CRLF Injection attack occurs when a user manages to submit a CRLF into an application. This is most commonly done by modifying an HTTP parameter or URL.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Check the submitted parameters and do not allow CRLF to be injected when it is not expected.")

                for i in range(len(self.Results[0]["CRLF Injection"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} ||URL:{}\n".format(num,self.Results[0]["CRLF Injection"][i]["method"],self.Results[0]["CRLF Injection"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}".format(num,self.Results[0]["CRLF Injection"][i]["parameter"]))                     

                if self.Results[3]["CRLF Injection"][0] > 0 :
                       for i in range(self.Results[3]["CRLF Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["CRLF Injection"][1][i] ,self.Results[3]["CRLF Injection"][2][i]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}".format(num,self.Results[3]["CRLF Injection"][3][i]) )                     
                for i in self.Results[4]:
                    if "crlf" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     
                if self.Results[1]['40103'][1] >0:
                     for i in range(self.Results[1]['50102'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['40103'][2][i][0],self.Results[1]['40103'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None".format(num) )                             




        if ("OGNL injection" in ID):        
                self.desc.insert(tkinter.END, "checkfor it\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"search for")
                if self.Results[1]['10902'][1] >0:
                     for i in range(self.Results[1]['50102'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['10902'][2][i][0],self.Results[1]['10902'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None".format(num) )                             
                for i in self.Results[4]:
                    if "ognl" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     


        if ("Host Header injection" in ID):        
                self.desc.insert(tkinter.END, "check thesis\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"search for it")
                if self.Results[1]['10902'][1] >0:
                     for i in range(self.Results[1]['30901'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['30901'][2][i][0],self.Results[1]['30901'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None".format(num) )                             
                for i in self.Results[4]:
                    if "host header" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}".format(num,self.Results[4][i][2]) )                     









        self.desc.configure(state="disabled")
        self.command.configure(state="disabled")
        self.http.configure(state="disabled")
    def close_check(self):
        self.CheckVul.grid_forget()    
    def createResaults(self):
        self.my_frame = MyFrame_My_Result(master=self.results_tabview.tab("Our Result"))
        self.my_frame.pack(fill="both",padx=0,pady=0,expand=True)        
                
        self.my_frameWapiti = MyFrame_My_wapiti(master=self.results_tabview.tab("wapiti"))
        self.my_frameWapiti.pack(fill="both",padx=0,pady=0,expand=True)        

        self.my_frameZap = MyFrame_My_Zap(master=self.results_tabview.tab("OWASP ZAP"))
        self.my_frameZap.pack(fill="both",padx=0,pady=0,expand=True)        

        self.my_frameNikto = MyFrame_My_Nikto(master=self.results_tabview.tab("Nikto"))
        self.my_frameNikto.pack(fill="both",padx=0,pady=0,expand=True)    

        self.my_frameNuclei = MyFrame_My_Nuclei(master=self.results_tabview.tab("Nuclei"))
        self.my_frameNuclei.pack(fill="both",padx=0,pady=0,expand=True)    


        self.my_frameSkipfish = MyFrame_My_Skipfish(master=self.results_tabview.tab("Skipfish"))
        self.my_frameSkipfish.pack(fill="both",padx=0,pady=0,expand=True)    
                        
    def destroyResaults(self):
        self.my_frame.pack_forget()
        self.my_frameWapiti.pack_forget()
        self.my_frameZap.pack_forget()
        self.my_frameNikto.pack_forget()
        self.my_frameNuclei.pack_forget()
        self.my_frameSkipfish.pack_forget()
        self.createResaults()

    def print_wapiti_Result(self,name):
    
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            number,detaille =new_scaner.get_wapiti_resaults()
            self.Results[0]=detaille
            if number['Blind SQL Injection'] > 0:
                   self.my_frame.vul_label[1][1].configure(text_color="red",text=int(self.my_frame.vul_label[1][1].cget("text"))+number['Blind SQL Injection'])
                   if "Wapiti" not in self.my_frame.vul_label[1][2].cget("text"):
                        if self.my_frame.vul_label[1][2].cget("text") =="None": self.my_frame.vul_label[1][2].configure(text="")
                        self.my_frame.vul_label[1][2].configure(text=self.my_frame.vul_label[1][2].cget("text")+" Wapiti,")
            if number['SQL Injection'] > 0:
                   self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+number['SQL Injection'])
                   if "Wapiti" not in self.my_frame.vul_label[0][2].cget("text"):
                        if self.my_frame.vul_label[0][2].cget("text") =="None": self.my_frame.vul_label[0][2].configure(text="")
                        self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+" Wapiti,")
            if number['Cross Site Scripting'] > 0:
                   self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+number['Cross Site Scripting'])
                   if "Wapiti" not in self.my_frame.vul_label[2][2].cget("text"):
                        if self.my_frame.vul_label[2][2].cget("text") =="None": self.my_frame.vul_label[2][2].configure(text="")
                        self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+" Wapiti,")
            if number['XML External Entity'] > 0:
                   self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+number['XML External Entity'])
                   if "Wapiti" not in self.my_frame.vul_label[6][2].cget("text"):
                        if self.my_frame.vul_label[6][2].cget("text") =="None": self.my_frame.vul_label[6][2].configure(text="")
                        self.my_frame.vul_label[6][2].configure(text=self.my_frame.vul_label[6][2].cget("text")+" Wapiti,")                        
            if number['Command execution'] > 0:
                   self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+number['Command execution'])
                   if "Wapiti" not in self.my_frame.vul_label[7][2].cget("text"):
                        if self.my_frame.vul_label[7][2].cget("text") =="None": self.my_frame.vul_label[7][2].configure(text="")
                        self.my_frame.vul_label[7][2].configure(text=self.my_frame.vul_label[7][2].cget("text")+" Wapiti,")
            if number['CRLF Injection'] > 0:
                   self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+number['CRLF Injection'])
                   if "Wapiti" not in self.my_frame.vul_label[11][2].cget("text"):
                        if self.my_frame.vul_label[11][2].cget("text") =="None": self.my_frame.vul_label[11][2].configure(text="")
                        self.my_frame.vul_label[11][2].configure(text=self.my_frame.vul_label[11][2].cget("text")+" Wapiti,")
            
            #TODO: Switch to textbox instead of label
            
            #Print the resault in the wapiti tAB view:4
            print_wapiti_Result11 = threading.Thread(target=self.print_wapiti_Result1,args=([detaille]))
            print_wapiti_Result11.start()
    def print_wapiti_Result1(self,detaille):    
            nuumeb=1      
            xer="---------------------------------------------------------------------------------------------"
            for i in detaille: 
               if len(detaille[i])>0:
                  for j in detaille[i]:
                        self.vul=customtkinter.CTkLabel(self.my_frameWapiti,text=xer)
                        self.vul.grid(row=nuumeb, column=0,columnspan=4)
                        nuumeb=nuumeb+1
                        self.vul=customtkinter.CTkLabel(self.my_frameWapiti,text=i,width=150)
                        self.vul.grid(row=nuumeb, column=0)
                        
                        self.http=customtkinter.CTkTextbox(self.my_frameWapiti,width=150,height=50,fg_color="transparent")
                        self.http.insert("0.0",j["http_request"])
                        self.http.grid(row=nuumeb, column=1,sticky="w")
                        self.http.configure(state="disabled")
                        
                        self.http=customtkinter.CTkTextbox(self.my_frameWapiti,width=150,height=50,fg_color="transparent")
                        self.http.insert("0.0",j["parameter"])
                        self.http.grid(row=nuumeb, column=2,sticky="w")
                        self.http.configure(state="disabled")
                        

                        self.info=customtkinter.CTkTextbox(self.my_frameWapiti,width=250,height=50,fg_color="transparent")
                        self.info.insert("0.0",j["info"])
                        self.info.grid(row=nuumeb, column=3,sticky="w")
                        self.info.configure(state="disabled")
                        
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
                                 self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+" SkipFish,")           
                      elif "XSS vector" in all_resaults[i][0] :
                             self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[2][2].cget("text"):
                                 if self.my_frame.vul_label[2][2].cget("text") =="None": self.my_frame.vul_label[2][2].configure(text="")
                                 self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+" SkipFish,")           
                      elif "Shell injection" in all_resaults[i][0] :
                             self.my_frame.vul_label[3][1].configure(text_color="red",text=int(self.my_frame.vul_label[3][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[3][2].cget("text"):
                                 if self.my_frame.vul_label[3][2].cget("text") =="None": self.my_frame.vul_label[3][2].configure(text="")
                                 self.my_frame.vul_label[3][2].configure(text=self.my_frame.vul_label[3][2].cget("text")+" SkipFish,")                   
                      elif "XML injection" in all_resaults[i][0] :
                             self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[5][2].cget("text"):
                                 if self.my_frame.vul_label[5][2].cget("text") =="None": self.my_frame.vul_label[5][2].configure(text="")
                                 self.my_frame.vul_label[5][2].configure(text=self.my_frame.vul_label[5][2].cget("text")+" SkipFish,")           
                      elif "HTTP response header splitting" in all_resaults[i][0] :
                             self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[11][2].cget("text"):
                                 if self.my_frame.vul_label[11][2].cget("text") =="None": self.my_frame.vul_label[11][2].configure(text="")
                                 self.my_frame.vul_label[11][2].configure(text=self.my_frame.vul_label[11][2].cget("text")+" SkipFish,")           
                      elif "OGNL-like parameter behavior" in all_resaults[i][0] :
                             self.my_frame.vul_label[12][1].configure(text_color="red",text=int(self.my_frame.vul_label[12][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[12][2].cget("text"):
                                 if self.my_frame.vul_label[12][2].cget("text") =="None": self.my_frame.vul_label[12][2].configure(text="")
                                 self.my_frame.vul_label[12][2].configure(text=self.my_frame.vul_label[12][2].cget("text")+" SkipFish,")           
                      elif "HTTP header injection" in all_resaults[i][0] :
                             self.my_frame.vul_label[13][1].configure(text_color="red",text=int(self.my_frame.vul_label[13][1].cget("text"))+all_resaults[i][1])
                             if "SkipFish" not in self.my_frame.vul_label[13][2].cget("text"):
                                 if self.my_frame.vul_label[13][2].cget("text") =="None": self.my_frame.vul_label[13][2].configure(text="")
                                 self.my_frame.vul_label[13][2].configure(text=self.my_frame.vul_label[13][2].cget("text")+" SkipFish,")           
                  
                  
                  #TODOOO ::::: PRINT RESAULT In SKIP FIsh Tab View like wapiti (bring the requast tags from resaults (modifie ostescanner code ,major work needed aghhh))
            self.my_frameSkipfish.label3.configure(state="normal",command=lambda: self.Open_skipfish_site(name) )
            
            print_skipfich_Result11 = threading.Thread(target=self.print_skipfich_Result1,args=([all_resaults]))
            print_skipfich_Result11.start()
            self.Results[1]=all_resaults
                  
    def print_skipfich_Result1(self,all_resaults):                  
                   #Print the resault in the skipfish tAB view:4
            xer="---------------------------------------------------------------------------------------------"
            nuumeb=1
            for i in all_resaults:
                 if "SQL query or similar syntax in parameters" in all_resaults[i][0] or "XSS vector"in all_resaults[i][0] or "Shell injection" in all_resaults[i][0] or"XML injection" in all_resaults[i][0] or"HTTP response header splitting"in all_resaults[i][0] or "OGNL-like parameter behavior" in all_resaults[i][0] or "HTTP header injection" in all_resaults[i][0]:
                    if all_resaults[i][1] >0:
                      for j in range(all_resaults[i][1]):
                        self.vul=customtkinter.CTkLabel(self.my_frameSkipfish,text=xer)
                        self.vul.grid(row=nuumeb, column=0,columnspan=4)
                        nuumeb=nuumeb+1
                     
                        self.vul=customtkinter.CTkLabel(self.my_frameSkipfish,text=all_resaults[i][0],width=150)
                        self.vul.grid(row=nuumeb, column=0)
                        
                        self.info=customtkinter.CTkTextbox(self.my_frameSkipfish,width=200,height=50,fg_color="transparent")
                        self.info.insert("0.0", all_resaults[i][2][j][1])
                        self.info.grid(row=nuumeb, column=1,sticky="w")
                        self.info.configure(state="disabled")

                        self.info=customtkinter.CTkTextbox(self.my_frameSkipfish,width=200,height=50,fg_color="transparent")
                        self.info.insert("0.0", all_resaults[i][2][j][0])
                        self.info.grid(row=nuumeb, column=2,sticky="w")
                        self.info.configure(state="disabled")

                        nuumeb=nuumeb+1
                 
                 
                 
                 
                  
    def print_Nikto_Result(self,name):
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            Nikto_resaults =new_scaner.get_nikto_report() 
            self.Results[2]=Nikto_resaults   
            if Nikto_resaults['nikto_vulnerability']['sql_injection']['number'] >0:
                     self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['sql_injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[0][2].cget("text"):
                         if self.my_frame.vul_label[0][2].cget("text") =="None": self.my_frame.vul_label[0][2].configure(text="")
                         self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+" Nikto,")                       
            
            if Nikto_resaults['nikto_vulnerability']['XSS injection']['number'] >0:
                     self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XSS injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[2][2].cget("text"):
                         if self.my_frame.vul_label[2][2].cget("text") =="None": self.my_frame.vul_label[2][2].configure(text="")
                         self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+" Nikto,")                       
                       
            if Nikto_resaults['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'] >0:
                     self.my_frame.vul_label[4][1].configure(text_color="red",text=int(self.my_frame.vul_label[4][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[4][2].cget("text"):
                         if self.my_frame.vul_label[4][2].cget("text") =="None": self.my_frame.vul_label[4][2].configure(text="")
                         self.my_frame.vul_label[4][2].configure(text=self.my_frame.vul_label[4][2].cget("text")+" Nikto,")                       

            if Nikto_resaults['nikto_vulnerability']['XML injection']['number'] >0:
                     self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XML injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[5][2].cget("text"):
                         if self.my_frame.vul_label[5][2].cget("text") =="None": self.my_frame.vul_label[5][2].configure(text="")
                         self.my_frame.vul_label[5][2].configure(text=self.my_frame.vul_label[5][2].cget("text")+" Nikto,")                       

            if Nikto_resaults['nikto_vulnerability']['remote source injection']['number'] >0:
                     self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['remote source injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[7][2].cget("text"):
                         if self.my_frame.vul_label[7][2].cget("text") =="None": self.my_frame.vul_label[7][2].configure(text="")
                         self.my_frame.vul_label[7][2].configure(text=self.my_frame.vul_label[7][2].cget("text")+" Nikto,")                       

            if Nikto_resaults['nikto_vulnerability']['html injection']['number'] >0:
                     self.my_frame.vul_label[9][1].configure(text_color="red",text=int(self.my_frame.vul_label[9][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['html injection']['number'])
                     if "Nikto" not in self.my_frame.vul_label[9][2].cget("text"):
                         if self.my_frame.vul_label[9][2].cget("text") =="None": self.my_frame.vul_label[9][2].configure(text="")
                         self.my_frame.vul_label[9][2].configure(text=self.my_frame.vul_label[9][2].cget("text")+" Nikto,")                       


            print_Nikto_Result11 = threading.Thread(target=self.print_Nikto_Result1,args=([Nikto_resaults]))
            print_Nikto_Result11.start()

    def print_Nikto_Result1(self,Nikto_resaults):
               #TODO Affichier raport Fel Nikto Tab  view ,(Rouh Lel  La Rapport tjib mno lurl wl method  wl msg )
           #            #id(vulnerability:)  method (METHOD) msg(description)  url (URL)  OSVDB(OSBDV Ref:)  
            xer="---------------------------------------------------------------------------------------------"
            nuumeb=1
            for i in Nikto_resaults['nikto_vulnerability']: 
               if Nikto_resaults['nikto_vulnerability'][i]['number']>0 :
                  for j in range(Nikto_resaults['nikto_vulnerability'][i]['number']):
                        self.vul=customtkinter.CTkLabel(self.my_frameNikto,text=xer)
                        self.vul.grid(row=nuumeb, column=0,columnspan=4)
                        nuumeb=nuumeb+1
                        
                        self.vul=customtkinter.CTkLabel(self.my_frameNikto,text=i,width=150)
                        self.vul.grid(row=nuumeb, column=0)
                        
                        self.http=customtkinter.CTkTextbox(self.my_frameNikto,width=180,height=100,fg_color="transparent")
                        self.http.insert("0.0","{} \n {}".format(Nikto_resaults['nikto_vulnerability'][i]['method_msg'][j][0],Nikto_resaults['nikto_vulnerability'][i]['method_msg'][j][2]))
                        self.http.grid(row=nuumeb, column=1)
                        self.http.configure(state="disabled")
                        
                        self.info=customtkinter.CTkLabel(self.my_frameNikto,text=Nikto_resaults['nikto_vulnerability'][i]['method_msg'][j][3],width=50)
                        self.info.grid(row=nuumeb, column=2)
                        
                        
                        self.info=customtkinter.CTkTextbox(self.my_frameNikto,width=280,height=100,fg_color="transparent")
                        self.info.insert("0.0", Nikto_resaults['nikto_vulnerability'][i]['method_msg'][j][1])
                        self.info.grid(row=nuumeb, column=3,sticky="w")
                        self.info.configure(state="disabled")
                        
                        nuumeb=nuumeb+1
          
      
          
    def print_zap_Result(self,name):                   #todo eglebha condition if >0 bh twli hamra (aaaghhhh) Wzid partye ta tzid esm scaner fki ydetecter
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            zap_resaults =new_scaner.owaspzap_get_resaults()   
            self.Results[3]=zap_resaults            
#            print(zap_resaults)
            if zap_resaults["SQL Injection"][0]+zap_resaults["SQL Injection - MySQL"][0]+zap_resaults["SQL Injection - Hypersonic SQL"][0]+zap_resaults["SQL Injection - Oracle"][0]+zap_resaults["SQL Injection - PostgreSQL"][0]+zap_resaults["SQL Injection - SQLite"][0]+zap_resaults["SQL Injection - MsSQL"][0]  > 0 :
                 self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+zap_resaults["SQL Injection"][0]+zap_resaults["SQL Injection - MySQL"][0]+zap_resaults["SQL Injection - Hypersonic SQL"][0]+zap_resaults["SQL Injection - Oracle"][0]+zap_resaults["SQL Injection - PostgreSQL"][0]+zap_resaults["SQL Injection - SQLite"][0]+zap_resaults["SQL Injection - MsSQL"][0])
                 if self.my_frame.vul_label[0][2].cget("text") =="None": self.my_frame.vul_label[0][2].configure(text="")
                 self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+" Owasp Zap,")

            if zap_resaults["Cross Site Scripting (Reflected)"][0]+zap_resaults["Cross Site Scripting (Persistent)"][0]+zap_resaults["Cross Site Scripting (Persistent) - Prime"][0]+zap_resaults["Cross Site Scripting (Persistent) - Spider"][0]+zap_resaults["Cross Site Scripting (DOM Based)"][0] > 0 :     
                 self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+zap_resaults["Cross Site Scripting (Reflected)"][0]+zap_resaults["Cross Site Scripting (Persistent)"][0]+zap_resaults["Cross Site Scripting (Persistent) - Prime"][0]+zap_resaults["Cross Site Scripting (Persistent) - Spider"][0]+zap_resaults["Cross Site Scripting (DOM Based)"][0])
                 if self.my_frame.vul_label[2][2].cget("text") =="None": self.my_frame.vul_label[2][2].configure(text="")
                 self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+" Owasp Zap,")

            if zap_resaults["XSLT Injection"][0] > 0:
                  self.my_frame.vul_label[4][1].configure(text_color="red",text=int(self.my_frame.vul_label[4][1].cget("text"))+zap_resaults["XSLT Injection"][0])
                  if self.my_frame.vul_label[4][2].cget("text") =="None": self.my_frame.vul_label[4][2].configure(text="")
                  self.my_frame.vul_label[4][2].configure(text=self.my_frame.vul_label[4][2].cget("text")+" Owasp Zap,")

                  
            if zap_resaults["SOAP XML Injection"][0] >0 :
                  self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+zap_resaults["SOAP XML Injection"][0])
                  if self.my_frame.vul_label[5][2].cget("text") =="None": self.my_frame.vul_label[5][2].configure(text="")
                  self.my_frame.vul_label[5][2].configure(text=self.my_frame.vul_label[5][2].cget("text")+" Owasp Zap,")
                  
            if zap_resaults["XML External Entity Attack"][0] >0 :      
                  self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+zap_resaults["XML External Entity Attack"][0])
                  if self.my_frame.vul_label[6][2].cget("text") =="None": self.my_frame.vul_label[6][2].configure(text="")
                  self.my_frame.vul_label[6][2].configure(text=self.my_frame.vul_label[6][2].cget("text")+" Owasp Zap,")
                  
            if zap_resaults["Server Side Code Injection"][0]+zap_resaults["Server Side Code Injection - PHP Code Injection"][0]+zap_resaults["Server Side Code Injection - ASP Code Injection"][0]+zap_resaults["Remote Code Execution - CVE-2012-1823"][0] > 0 :
                  self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+zap_resaults["Server Side Code Injection"][0]+zap_resaults["Server Side Code Injection - PHP Code Injection"][0]+zap_resaults["Server Side Code Injection - ASP Code Injection"][0]+zap_resaults["Remote Code Execution - CVE-2012-1823"][0])
                  if self.my_frame.vul_label[7][2].cget("text") =="None": self.my_frame.vul_label[7][2].configure(text="")
                  self.my_frame.vul_label[7][2].configure(text=self.my_frame.vul_label[7][2].cget("text")+" Owasp Zap,")

            if zap_resaults["Remote OS Command Injection"][0] > 0 :
                  self.my_frame.vul_label[8][1].configure(text_color="red",text=int(self.my_frame.vul_label[8][1].cget("text"))+zap_resaults["Remote OS Command Injection"][0])
                  if self.my_frame.vul_label[8][2].cget("text") =="None": self.my_frame.vul_label[8][2].configure(text="")
                  self.my_frame.vul_label[8][2].configure(text=self.my_frame.vul_label[8][2].cget("text")+" Owasp Zap,")
            if zap_resaults["Server Side Template Injection"][0] > 0 :
                  self.my_frame.vul_label[10][1].configure(text_color="red",text=int(self.my_frame.vul_label[10][1].cget("text"))+zap_resaults["Server Side Template Injection"][0] )      
                  if self.my_frame.vul_label[10][2].cget("text") =="None": self.my_frame.vul_label[10][2].configure(text="")
                  self.my_frame.vul_label[10][2].configure(text=self.my_frame.vul_label[10][2].cget("text")+" Owasp Zap,")
                       
            if zap_resaults["CRLF Injection"][0] > 0:
                  self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+zap_resaults["CRLF Injection"][0])
                  if self.my_frame.vul_label[11][2].cget("text") =="None": self.my_frame.vul_label[11][2].configure(text="")
                  self.my_frame.vul_label[11][2].configure(text=self.my_frame.vul_label[11][2].cget("text")+" Owasp Zap,")
                  
            print_zap_Result1 = threading.Thread(target=self.print_zap_Result1,args=([zap_resaults]))
            print_zap_Result1.start()
            
    def print_zap_Result1(self,zap_resaults):                            
                        #Print the resault in the Zap tAB view:4
                        #alert(vulnerability:)  method \n url (Method\nURL)  inputVector(inputVector)  description(description) 
            xer="---------------------------------------------------------------------------------------------"
            nuumeb=1
            for i in zap_resaults: 
               if zap_resaults[i][0]>0 and i!="User Agent Fuzzer" and i!="GET for POST":
                  for j in range(zap_resaults[i][0]):
                        self.vul=customtkinter.CTkLabel(self.my_frameZap,text=xer)
                        self.vul.grid(row=nuumeb, column=0,columnspan=4)
                        nuumeb=nuumeb+1
                        
                        self.vul=customtkinter.CTkLabel(self.my_frameZap,text=i,width=150)
                        self.vul.grid(row=nuumeb, column=0)
                        
                        self.http=customtkinter.CTkLabel(self.my_frameZap,text="{} \n {}".format(zap_resaults[i][1][j][0],zap_resaults[i][1][j][1]),width=150)
                        self.http.grid(row=nuumeb, column=1)
                        self.info=customtkinter.CTkLabel(self.my_frameZap,text=zap_resaults[i][2][j],width=150)
                        self.info.grid(row=nuumeb, column=2)
                        self.info=customtkinter.CTkTextbox(self.my_frameZap,width=250,height=100,fg_color="transparent")
                        self.info.insert("0.0", zap_resaults[i][3][j])
                        self.info.grid(row=nuumeb, column=3,sticky="w")
                        self.info.configure(state="disabled")
                        
                        nuumeb=nuumeb+1
            
            
           
    def print_nuclei_Result(self,name):                   #todo eglebha condition if >0 bh twli hamra (aaaghhhh) Wzid partye ta tzid esm scaner fki ydetecter
            new_scaner=OSTEscaner.scan()
            new_scaner.configuiring_new_scan(name)
            nuclei_resaults =new_scaner.nuclei_report()   
            self.Results[4]=nuclei_resaults            
            for i in nuclei_resaults:
                if "sql" in i.lower():
                   self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+nuclei_resaults[i][0])    
                   if self.my_frame.vul_label[0][2].cget("text") =="None": self.my_frame.vul_label[0][2].configure(text="")        
                   self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+" Nuclei,")

                elif "blind sql" in i.lower():
                   self.my_frame.vul_label[1][1].configure(text_color="red",text=int(self.my_frame.vul_label[1][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[1][2].cget("text") =="None": self.my_frame.vul_label[1][2].configure(text="")
                   self.my_frame.vul_label[1][2].configure(text=self.my_frame.vul_label[1][2].cget("text")+" Nuclei,")
                elif "cross"in i.lower() and "site"in i.lower() and "scripting" in i.lower() or "xss" in i.lower():
                   self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[2][2].cget("text") =="None": self.my_frame.vul_label[2][2].configure(text="")                  
                   self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+" Nuclei,")                
                elif "shell" in i.lower():                
                   self.my_frame.vul_label[3][1].configure(text_color="red",text=int(self.my_frame.vul_label[3][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[3][2].cget("text") =="None": self.my_frame.vul_label[3][2].configure(text="")
                   self.my_frame.vul_label[3][2].configure(text=self.my_frame.vul_label[3][2].cget("text")+" Nuclei,")
                elif "xml"in i.lower() and "external"in i.lower() and "entity" in i.lower():                
                   self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[6][2].cget("text") =="None": self.my_frame.vul_label[6][2].configure(text="") 
                   self.my_frame.vul_label[6][2].configure(text=self.my_frame.vul_label[6][2].cget("text")+" Nuclei,")
                elif "xml"in i.lower() and "entity" in i.lower():                
                   self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[5][2].cget("text") =="None": self.my_frame.vul_label[5][2].configure(text="")
                   self.my_frame.vul_label[5][2].configure(text=self.my_frame.vul_label[5][2].cget("text")+" Nuclei,")
                elif "code" in i.lower():                
                   self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[7][2].cget("text") =="None": self.my_frame.vul_label[7][2].configure(text="")
                   self.my_frame.vul_label[7][2].configure(text=self.my_frame.vul_label[7][2].cget("text")+" Nuclei,")
                elif "command" in i.lower():                
                   self.my_frame.vul_label[8][1].configure(text_color="red",text=int(self.my_frame.vul_label[8][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[8][2].cget("text") =="None": self.my_frame.vul_label[8][2].configure(text="")
                   self.my_frame.vul_label[8][2].configure(text=self.my_frame.vul_label[8][2].cget("text")+" Nuclei,")
                elif "html" in i.lower():                
                   self.my_frame.vul_label[9][1].configure(text_color="red",text=int(self.my_frame.vul_label[9][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[9][2].cget("text") =="None": self.my_frame.vul_label[9][2].configure(text="")
                   self.my_frame.vul_label[9][2].configure(text=self.my_frame.vul_label[9][2].cget("text")+" Nuclei,")
                elif "crlf" in i.lower():                
                   self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[11][2].cget("text") =="None": self.my_frame.vul_label[11][2].configure(text="")
                   self.my_frame.vul_label[11][2].configure(text=self.my_frame.vul_label[11][2].cget("text")+" Nuclei,")
                elif "ognl" in i.lower():                
                   self.my_frame.vul_label[12][1].configure(text_color="red",text=int(self.my_frame.vul_label[12][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[12][2].cget("text") =="None": self.my_frame.vul_label[12][2].configure(text="")
                   self.my_frame.vul_label[12][2].configure(text=self.my_frame.vul_label[12][2].cget("text")+" Nuclei,")
                elif "host header" in i.lower():                
                   self.my_frame.vul_label[13][1].configure(text_color="red",text=int(self.my_frame.vul_label[13][1].cget("text"))+nuclei_resaults[i][0])
                   if self.my_frame.vul_label[13][2].cget("text") =="None": self.my_frame.vul_label[13][2].configure(text="")
                   self.my_frame.vul_label[13][2].configure(text=self.my_frame.vul_label[4][2].cget("text")+" Nuclei,")

            print_nuclei_Result1 = threading.Thread(target=self.print_nuclei_Result1,args=([nuclei_resaults]))
            print_nuclei_Result1.start()
            
            
            
    def print_nuclei_Result1(self,nuclei_resaults):               
					#Name(number)         matched-at       (curl-command)   Description
            xer="---------------------------------------------------------------------------------------------"
            nuumeb=1
            for i in nuclei_resaults:

                  for j in range(nuclei_resaults[i][0]):
                        self.vul=customtkinter.CTkLabel(self.my_frameNuclei,text=xer)
                        self.vul.grid(row=nuumeb, column=0,columnspan=4)
                        nuumeb=nuumeb+1
                        
                        self.info=customtkinter.CTkTextbox(self.my_frameNuclei,width=180,height=100,fg_color="transparent")
                        self.info.insert("0.0",i)
                        self.info.grid(row=nuumeb, column=0,sticky="w")
                        self.info.configure(state="disabled")
                        
                        self.info=customtkinter.CTkTextbox(self.my_frameNuclei,width=150,height=100,fg_color="transparent")
                        self.info.insert("0.0", nuclei_resaults[i][1][j])
                        self.info.grid(row=nuumeb, column=1,sticky="w")
                        self.info.configure(state="disabled")

                        self.info=customtkinter.CTkTextbox(self.my_frameNuclei,width=150,height=100,fg_color="transparent")
                        self.info.insert("0.0", nuclei_resaults[i][2][j])
                        self.info.grid(row=nuumeb, column=2,sticky="w")
                        self.info.configure(state="disabled")

                        
                        self.info=customtkinter.CTkTextbox(self.my_frameNuclei,width=250,height=100,fg_color="transparent")
                        self.info.insert("0.0", nuclei_resaults[i][3])
                        self.info.grid(row=nuumeb, column=3,sticky="w")
                        self.info.configure(state="disabled")
                        
                        nuumeb=nuumeb+1


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

    def open_target_Window(self):
       if self.Target_Window is None or not self.Target_Window.winfo_exists():
            self.Target_Window=Target_Window(self)
       else:
            self.Target_Window.focus()

    def open_load_Window(self):
        if self.loadResult_window is None or not self.loadResult_window.winfo_exists():
                 self.loadResult_window =loadResult_Window(self)
        else:
             self.loadResult_window.focus()
                      
    def open_start_Window(self):
        if self.start_Window is None or not self.start_Window.winfo_exists():
            self.start_Window = start_Window(self)  # create window if its None or destroyed
        else:
            self.start_Window.focus()
            
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        if new_appearance_mode=="Light":
                self.menubar.config(bg='#4d4d4d', fg='white', activebackground='white', activeforeground='#2d2d2d', borderwidth=0, relief='flat', font=('Arial', 12))
                self.file_menu.config(bg='#4d4d4d', fg='white', activebackground='white', activeforeground='#2d2d2d', borderwidth=0, relief='flat', font=('Arial', 12))
                self.view_menu.config(bg='#4d4d4d', fg='white', activebackground='white', activeforeground='#2d2d2d', borderwidth=0, relief='flat', font=('Arial', 12))
                self.modes_menu.config(bg='#4d4d4d', fg='white', activebackground='white', activeforeground='#2d2d2d', borderwidth=0, relief='flat', font=('Arial', 12))
        else:
                self.menubar.config(bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
                self.file_menu.config(bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
                self.view_menu.config(bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
                self.modes_menu.config(bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))

        
        customtkinter.set_appearance_mode(new_appearance_mode)
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def Load_resaults(self,name):
#        for i in self.my_frame.vul_label:
#            i[1].configure(text=int(0))

        self.log_textbox.insert(tkinter.END, "\n[Results]:", tags="yellow")            
        self.log_textbox.insert(tkinter.END, "\t\tCheck The Results of :", tags=None) 
        self.log_textbox.insert(tkinter.END, "\n---------------- ", tags="red")            
        self.log_textbox.insert(tkinter.END, "{}".format(name), tags=None) 
        self.log_textbox.insert(tkinter.END, "  ----------------", tags="red")            

        self.destroyResaults()
       
        self.print_wapiti_Result(name)
        self.print_skipfich_Result(name) 
        self.print_Nikto_Result(name)
        self.print_zap_Result(name)
        self.print_nuclei_Result(name)
    def Open_skipfish_site(self,name):
        webbrowser.open('/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/{}/skipfish/{}/index.html'.format(name,name), new=2)
        
        
        
class MyFrame_My_wapiti(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self,text="Vulnerability ",width=150)

        self.label.grid(row=0, column=0,padx=3,pady=3)
        self.label1 = customtkinter.CTkLabel(self,text="http_request",width=150)
        self.label1.grid(row=0, column=1,padx=3,pady=3)
        self.label2 = customtkinter.CTkLabel(self,text="parameter",width=80)
        self.label2.grid(row=0, column=2,padx=3,pady=3,sticky="nsew")    
        self.label3 = customtkinter.CTkLabel(self,text="Discription",width=150)
        self.label3.grid(row=0, column=3,padx=3,pady=3)
        
class MyFrame_My_Zap(customtkinter.CTkScrollableFrame):  #alert(vulnerability:)  method \n url (Method\nURL)  inputVector(inputVector)  description(description) 
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self,text="Vulnerability",width=150)

        self.label.grid(row=0, column=0,padx=3,pady=3)
        self.label1 = customtkinter.CTkLabel(self,text="Method\nURL",width=150)
        self.label1.grid(row=0, column=1,padx=3,pady=3)
        self.label2 = customtkinter.CTkLabel(self,text="inputVector",width=150)
        self.label2.grid(row=0, column=2,padx=3,pady=3)        
        self.label3 = customtkinter.CTkLabel(self,text="Description",width=300)
        self.label3.grid(row=0, column=3,padx=3,pady=3,sticky="e")
        
class MyFrame_My_Nikto(customtkinter.CTkScrollableFrame):  #            #id(vulnerability:)  method (METHOD) msg(description)  url (URL)  OSVDB(OSBDV Ref:)  
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self,text="Vulnerability",width=150)

        self.label.grid(row=0, column=0,padx=3,pady=3)
        self.label1 = customtkinter.CTkLabel(self,text="Method\nURL",width=150)
        self.label1.grid(row=0, column=1,padx=3,pady=3)
        self.label2 = customtkinter.CTkLabel(self,text="OSVDB Ref:",width=150)
        self.label2.grid(row=0, column=2,padx=3,pady=3)        
        self.label3 = customtkinter.CTkLabel(self,text="Description",width=300)
        self.label3.grid(row=0, column=3,padx=3,pady=3,sticky="e")

class MyFrame_My_Nuclei(customtkinter.CTkScrollableFrame):  #           #Name(number)         matched-at       (curl-command)   Description
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self,text="Vulnerability",width=180)

        self.label.grid(row=0, column=0,padx=3,pady=3)
        self.label1 = customtkinter.CTkLabel(self,text="URL",width=150)
        self.label1.grid(row=0, column=1,padx=3,pady=3)
        self.label2 = customtkinter.CTkLabel(self,text="curl-command",width=150)
        self.label2.grid(row=0, column=2,padx=3,pady=3)        
        self.label3 = customtkinter.CTkLabel(self,text="Description",width=300)
        self.label3.grid(row=0, column=3,padx=3,pady=3,sticky="e")

class MyFrame_My_Skipfish(customtkinter.CTkScrollableFrame):  #           #Name(number)         Host  Request          more info
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self,text="Vulnerability",width=180)
        self.label.grid(row=0, column=0,padx=3,pady=3)
        
        self.label1 = customtkinter.CTkLabel(self,text="host",width=150)
        self.label1.grid(row=0, column=1,padx=3,pady=3)
        
        self.label2 = customtkinter.CTkLabel(self,text="Request",width=150)
        self.label2.grid(row=0, column=2,padx=3,pady=3)        

        self.label3=customtkinter.CTkButton(self,text="check for more information" ,width=120 , height=35,command=None,state="disabled")
        self.label3.grid(row=0, column=3,padx=3,pady=3,sticky="e")

class MyFrame_My_Result(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame...borderwidth
        self.label = customtkinter.CTkLabel(self,text="Vulnerability ",width=250)

        self.label.grid(row=0, column=0,padx=3,pady=3)
        self.label1 = customtkinter.CTkLabel(self,text="Exist",width=50)
        self.label1.grid(row=0, column=1,padx=3,pady=3)
        self.label2 = customtkinter.CTkLabel(self,text="Scanners",width=350)
        self.label2.grid(row=0, column=2,padx=3,pady=3)
        self.label3 = customtkinter.CTkLabel(self,text="Action")
        self.label3.grid(row=0, column=3,padx=3,pady=3,sticky="e")    
        self.vul_label=[]
        xer="_____________________________________________________________________________________________________________________________"
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
            self.but=customtkinter.CTkButton(self,text="check",width=80 , height=35)#,state="disabled"  ki tkml raj3ha
            self.but.grid(row=i+1, column=3,padx=3,pady=(5,30),sticky="e")
            self.vul_label.append([self.labeltemp,self.labeltemp1,self.labeltemp2,self.but])

        self.vul_label[0][0].configure(text="SQL injection:")
        self.vul_label[0][3].configure(command=lambda:app.open_check("SQL Injection"))
        
        self.vul_label[1][0].configure(text="Blind SQL injection:")
        self.vul_label[1][3].configure(command=lambda:app.open_check("Blind SQL injection"))
        self.vul_label[2][0].configure(text="Cross Site Scripting injection:")
        self.vul_label[2][3].configure(command=lambda:app.open_check("Cross Site Scripting injection"))
        self.vul_label[3][0].configure(text="Shell injection:")
        self.vul_label[3][3].configure(command=lambda:app.open_check("Shell injection"))
        self.vul_label[4][0].configure(text="XSLT injection:")
        self.vul_label[4][3].configure(command=lambda:app.open_check("XSLT injection"))
        self.vul_label[5][0].configure(text="XML injection:")
        self.vul_label[5][3].configure(command=lambda:app.open_check("XML injection"))
        self.vul_label[6][0].configure(text="XML external entities (XXE):")
        self.vul_label[6][3].configure(command=lambda:app.open_check("XML external entities (XXE)"))
        self.vul_label[7][0].configure(text="code injection:")
        self.vul_label[7][3].configure(command=lambda:app.open_check("code injection"))
        self.vul_label[8][0].configure(text="OS command injection:")
        self.vul_label[8][3].configure(command=lambda:app.open_check("OS command injection"))
        self.vul_label[9][0].configure(text="html injection:")
        self.vul_label[9][3].configure(command=lambda:app.open_check("html injection"))
        self.vul_label[10][0].configure(text="Template injection:")
        self.vul_label[10][3].configure(command=lambda:app.open_check("Template injection"))
        self.vul_label[11][0].configure(text="CRLF injection:")
        self.vul_label[11][3].configure(command=lambda:app.open_check("CRLF injection"))
        self.vul_label[12][0].configure(text="OGNL injection:")
        self.vul_label[12][3].configure(command=lambda:app.open_check("OGNL injection"))
        self.vul_label[13][0].configure(text="Host Header injection:")
        self.vul_label[13][3].configure(command=lambda:app.open_check("Host Header injection"))

    def getresault(self,injectiontype):
         print(injectiontype)
                 
if __name__ == "__main__":
    app = App()
    app.mainloop()
