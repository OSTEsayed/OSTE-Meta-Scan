import tkinter
from tkinter import filedialog
import threading
import webbrowser
import tkinter.messagebox
import customtkinter
import time
import OSTEscaner
import os,shutil
import subprocess
import signal
import json
from PIL import Image
from jinja2 import Environment, FileSystemLoader
from matplotlib.pyplot import bar, show,title,ylim

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
                self.radio_button_1.grid(row=int(i/2), column=int(i%2), pady=10, padx=20, sticky="nw")
        #print(self.radio_var)     
        
        
class Target_Window(customtkinter.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Web Vulnerability META-Scanner  -servers-")
        self.directory="no"
        xer="_____________________________________________________"
        self.path="/home/ostesayed/Desktop/Scanners/OSTE-Scanner/Targets/"
        self.geometry("400x350")
        self.frame_main = customtkinter.CTkFrame(self)
        self.frame_main.pack(pady=10,padx=10,fill="both",expand=True)

        self.optionmenu_var = customtkinter.StringVar(value="XAMP server")  # set initial value
        self.choselabel = customtkinter.CTkLabel(self.frame_main,text="Chose your desired server:").grid(padx=(30,0),pady=10,row=0,column=0)
        self.chose = customtkinter.CTkOptionMenu(self.frame_main, values=["XAMP server", "NPM server"],command=self.optionmenu_callback,variable=self.optionmenu_var,width=100).grid(padx=(10,30),pady=10,row=0,column=1)
#        self.npmTarget = customtkinter.CTkButton(self, command=self.npmstart ,text="Start Npm Target")
#        self.XampTarget = customtkinter.CTkButton(self, command=self.xampstart ,text="Start Xamp",fg_color="green")
        self.starter =  customtkinter.CTkButton(self, command=self.startchoise ,text="Start",fg_color="green")
        self.starter.pack()
#       self.npmTarget.pack(padx=(40,5),side="left")
#        self.XampTarget.pack(padx=(5,40),side="right")
    def optionmenu_callback(self,choice):
#        self.geometry("600x350")
#        print(self.optionmenu_var.get())
        if choice=="NPM server":
         self.label_main=customtkinter.CTkLabel(self.frame_main,text="or from Target List:").grid(row=1,column=1)
         self.mylist=os.listdir(self.path)
         self.radio_var = tkinter.IntVar(value=0)
         self.radio_button_1 = customtkinter.CTkButton(master=self.frame_main,text="chose directory", command=self.chosedirect)
         self.radio_button_1.grid(row=1,column=0)
        

         for i in range(len(self.mylist)):
                 self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_main,text=self.mylist[i], variable=self.radio_var, value=i+1)
                 self.radio_button_1.grid(row=i+3,column=0,columnspan=2,padx=(20,0),pady=(15,0),sticky="sw")
        else:
         self.frame_main.pack_forget()
         self.starter.pack_forget()
         self.frame_main = customtkinter.CTkFrame(self)
         self.frame_main.pack(pady=10,padx=10,fill="both",expand=True)

         self.optionmenu_var = customtkinter.StringVar(value="XAMP server")  # set initial value
         self.choselabel = customtkinter.CTkLabel(self.frame_main,text="Chose your desired server:").grid(padx=(30,0),pady=10,row=0,column=0)
         self.chose = customtkinter.CTkOptionMenu(self.frame_main, values=["XAMP server", "NPM server"],command=self.optionmenu_callback,variable=self.optionmenu_var,width=100).grid(padx=(10,30),pady=10,row=0,column=1)
         self.starter =  customtkinter.CTkButton(self, command=self.startchoise ,text="Start",fg_color="green")
         self.starter.pack()


    def chosedirect(self):
        self.directory = filedialog.askdirectory()    
        self.npmstart()
    def startchoise(self):
        if self.optionmenu_var.get()=="XAMP server":
              self.xampstart()
        else:
              self.npmstart()
#        print('you started')    
    def npmstart(self):
        self.frame_main.pack_forget()
#        self.npmTarget.pack_forget()
#        self.XampTarget.pack_forget()
        self.starter.pack_forget()

        self.log_textbox = customtkinter.CTkTextbox(self, width=200)
        self.log_textbox.pack(padx=10, pady=10,fill ="both",expand=True)
        self.log_textbox.tag_add("red", 0.0, 0.5)
        self.log_textbox.tag_config("red",foreground="red",underline=1)
        self.log_textbox.tag_config("yellow",foreground="yellow")
        self.log_textbox.tag_config("green",foreground="lightgreen")
        
        self.log_textbox.tag_add("yellow", 0.0, 0.5)
        self.log_textbox.tag_add("green", 0.0, 0.5)
        self.log_textbox.insert(1.0, "\t Starting Target.... :\n", tags="red")
        if self.directory!="no":
           self.process = subprocess.Popen("npm start", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,cwd=self.directory)       #path li fe cwd mazalt majerbtouch 3les problem:
        else:
           self.process = subprocess.Popen("npm start", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,cwd=f"{self.path}/{self.mylist[self.radio_var.get()-1]}/")       #path li fe cwd mazalt majerbtouch 3les problem:
        
        pid = int(self.process.pid)
        starting= threading.Thread(target=self.start)
        starting.start() 
        
        self.stop_button = customtkinter.CTkButton(self, text="Stop The Target", command=lambda: os.kill(pid, signal.SIGTERM),fg_color="red") 
        self.stop_button.pack()
        #print(f"ok with {self.mylist[self.radio_var.get()-1]}")
        
    def start(self):
   
        line = self.process.stdout.readline()
        if not line:
            time.sleep(10)
            #print("no line")
        self.log_textbox.insert(tkinter.END, line.decode())
        self.log_textbox.see(tkinter.END)
        self.start()       

              
        
    def xampstart(self):
        self.frame_main.pack_forget()
#        self.npmTarget.pack_forget()
#        self.XampTarget.pack_forget()
        self.starter.pack_forget()
        self.log_textbox = customtkinter.CTkTextbox(self, width=200)
        self.log_textbox.pack(padx=10, pady=10,fill ="both",expand=True)

        cmd = "sudo /opt/lampp/lampp start"
#        cmd="sudo ls -l"
        password = tkinter.simpledialog.askstring("Password", "Enter your password:(Required)", show='*')
        process = os.popen('echo {} | {} -S {}'.format(password, "sudo", cmd))
        self.log_textbox.insert(tkinter.END, "Command output:\n")

        for line in process:
           self.log_textbox.insert(tkinter.END, line)
           
        self.stop_button = customtkinter.CTkButton(self, text="Stop The Target", command=self.xampstop,fg_color="red") 
        self.stop_button.pack()

        #print("ok")
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
        self.title("Web Vulnerability META-Scanner  -Resault-")
        self.geometry("500x400")
        self.frame_main = customtkinter.CTkFrame(self)
        self.frame_main.pack(pady=10,padx=10,fill ="both",expand=True)
        self.label =customtkinter.CTkLabel(self.frame_main,text="Chose Result:")
        self.label.pack(padx=20,pady=20)
        
        self.resultf =MyResultFrame (self.frame_main,height=200)
        self.resultf.pack(padx=10,pady=0,fill="x")
        self.check = customtkinter.CTkButton(self.frame_main, command=self.cchek ,text="Check")
        self.delete = customtkinter.CTkButton(self.frame_main, command=self.ddelete ,text="Delete",fg_color="red")
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
        self.title("Web Vulnerability META-Scanner  -Starting Scan-")
        self.geometry("500x350")
        self.frame_main = customtkinter.CTkFrame(self)
        self.frame_main.pack(pady=20,padx=60,fill ="both",expand=True)
        self.label_main = customtkinter.CTkLabel(self.frame_main, text="Start The New Scan")
        self.label_main.pack(padx=20, pady=20)


        self.slider_1 = customtkinter.CTkSlider(self.frame_main, from_=0, to=1, number_of_steps=16,orientation="vertical")
        self.slider_1.pack(padx=(20, 10), pady=(10, 10),side="right")
        self.label_craw=customtkinter.CTkLabel(self.frame_main,text="Crawling Depth:").pack(side="right")
        
#        but = customtkinter.CTkButton(self.frame_main,text="val" , command =lambda: print(int(self.slider_1.get()*16)))
#       but.pack()
        self.target_name=customtkinter.CTkEntry(self.frame_main,placeholder_text="Name of target")
        self.target_name.pack(pady=12,padx=10)

        self.target_url=customtkinter.CTkEntry(self.frame_main,placeholder_text="URL of target: (http://....)")
        self.target_url.pack(pady=12,padx=10)
        self.start_button=customtkinter.CTkButton(self.frame_main, text="Start Scanning",command=self.start_new_scan)
        self.start_button.pack(pady=12,padx=20)
        
        self.label_result = customtkinter.CTkLabel(self.frame_main, text="")
        self.label_result.pack(padx=20, pady=20)




    def start_new_scan(self):
        crowling_depth= int(self.slider_1.get()*16)
        if crowling_depth==0:crowling_depth=1
        if crowling_depth==16:crowling_depth=15
        #print(crowling_depth)
        if self.target_name.get()=="":
            self.label_result.configure(text="Enter the name of target",text_color="red")

        if self.target_url.get()=="":
            self.label_result.configure(text="Enter Valide URL of target",text_color="red")
            #print("Enter Valide name!!")
        else:										#scaning
            self.label_result.configure(text="Starting Scaning the target",text_color="green")            
            new_scan= OSTEscaner.scan()
            app.log_textbox.insert(tkinter.END, "\n[Starting]", tags="green") 
            app.log_textbox.insert(tkinter.END, " Creating Resaults Directory for each scanner", tags=None)
            new_scan.configuiring_new_scan(self.target_name.get(),self.target_url.get(),crowling_depth)
            new_scan.creat_directory()
            app.log_textbox.insert(tkinter.END, "\n[Location]", tags="green") 
            app.log_textbox.insert(tkinter.END, " /home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/"+self.target_name.get(), tags=None)
            app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")      
            app.log_textbox.insert(tkinter.END, " wapiti scan started", tags=None)
            starting_wapiti = threading.Thread(target=new_scan.start_wapiti)
            starting_wapiti.start() 
            app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")      	
            app.log_textbox.insert(tkinter.END, " skipfish scan started", tags=None)
            
            starting_skipfish = threading.Thread(target=new_scan.start_skipfish)
            starting_skipfish.start()
            app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="green")      
            app.log_textbox.insert(tkinter.END, " OWASPZAP server started", tags=None)
            
            starting_zap_server = threading.Thread(target=new_scan.start_zap)
            starting_zap_server.start()
#            app.log_textbox.insert(tkinter.END, "\n [INFO] 		OWASPZAP Scanning started", tags=None)            
            starting_zap= threading.Thread(target=new_scan.check_for_zap)
            #starting_zap.start()
            app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")                  
            app.log_textbox.insert(tkinter.END, " NIKTO Scanning started", tags=None)            
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
                      app.log_textbox.insert(tkinter.END, " OWASPZAP Scanning started", tags=None)           
                      a.start()
                      zap_statu="scanning"
                      zaper="yet"
                  if nucleir=="lunch":
                      app.log_textbox.insert(tkinter.END, "\n[INFO]", tags="yellow")            
                      app.log_textbox.insert(tkinter.END, " Nuclei Scanning started", tags=None)            
                      c.start()
                      nuclei_statu="scanning"
                      nucleir="yet"
                      time.sleep(1)                      
                  if zap_statu=="scanning":
                          if a.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")            
                              app.log_textbox.insert(tkinter.END, " OWASP ZAP Scanning Finished", tags=None)            
                              zap_statu="finished"
                              number_scaner-=1       	
                  if nikto_statu=="scanning":
                          if b.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")            
                              app.log_textbox.insert(tkinter.END, " NIKTO Scanning Finished", tags=None)            
                              nikto_statu="finished"
                              number_scaner-=1           
                  if nuclei_statu=="scanning":
                          if c.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")            
                              app.log_textbox.insert(tkinter.END, " Nuclei Scanning Finished", tags=None)            
                              nuclei_statu="finished"
                              number_scaner-=1 
                  if wapiti_statu=="scanning":
                          if d.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")            
                              app.log_textbox.insert(tkinter.END, " WAPITI Scanning Finished", tags=None)            
                              wapiti_statu="finished"
                              number_scaner-=1 
                  if skipfish_statu=="scanning":
                          if e.is_alive()==False:
                              app.log_textbox.insert(tkinter.END, "\n [finished]", tags="red")                                      
                              app.log_textbox.insert(tkinter.END, " SKIPFISH Scanning Finished", tags=None)            
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
        self.title("Web Vulnerability META-Scanner")		#OSTEscanner

        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
 #       self.attributes('-fullscreen',True)
#        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join("images/meta.ico")), size=(20, 20)) 
#        self.iconbitmap(default="images/meta.ico")        #configure the menu:
        
        self.menubar = tkinter.Menu(self, bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))

        self.config(menu=self.menubar)
        
        self.file_menu = tkinter.Menu(self.menubar ,bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
        self.file_menu.add_command(label='Start Scan',command=self.open_start_Window)
        self.file_menu.add_command(label='Load Result',command=self.open_load_Window)
        self.file_menu.add_command(label='Save As HTML',command=self.save_as_html)
#        self.file_menu.add_separator()
#        self.file_menu.add_command(label='About',command=print("about not yet finished"))
#        self.file_menu.add_command(label='Verify Scanners',command=self.chec_for_scanner)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',command=self.destroy)
        self.menubar.add_cascade(label="File", menu=self.file_menu,underline=0)
        
#        self.target_menu = tkinter.Menu(self.menubar ,bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
#        self.target_menu.add_command(label='Local host servers',command=self.open_target_Window)
#        self.target_menu.add_separator()
#        self.target_menu.add_command(label='Verify Scanners',command=self.chec_for_scanner)
#        self.target_menu.add_separator()
#        self.menubar.add_cascade(label="Others", menu=self.target_menu,underline=0)

        
        self.modes_menu = tkinter.Menu(self.menubar, tearoff=0,bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
        self.modes_menu.add_command(label='System ModeThemes',command=lambda:self.change_appearance_mode_event("System"))
        self.modes_menu.add_command(label='light Mode',command=lambda:self.change_appearance_mode_event("Light"))
        self.modes_menu.add_command(label='dark Mode',command=lambda:self.change_appearance_mode_event("Dark"))
        
        
        self.menubar.add_command(label="Local-host servers",command=self.open_target_Window,underline=0)
        self.menubar.add_command(label="Verify Scanners",command=self.chec_for_scanner,underline=0)
        self.menubar.add_cascade(label='Appearance',menu=self.modes_menu,underline=0)
        self.menubar.add_command(label="About",command=print("about not yet finished"),underline=0)

        
        
        

        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        #Start stat (slide bar minized)
        self.slidd=0

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=30, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        maximize=customtkinter.CTkImage(light_image=Image.open("images/maximize.png"),dark_image=Image.open("images/maximize.png"),size=(20, 20))
        self.maxi =customtkinter.CTkButton(self.sidebar_frame,text="",image=maximize,width=20,height=20,fg_color='transparent',command=self.maximize)#,command=
        self.maxi.grid(row=0,column=0,sticky="ne")                  

        #loog textbox
        self.log_textbox = customtkinter.CTkTextbox(self, width=350)
        self.log_textbox.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.log_textbox.tag_add("red", 0.0, 0.5)
        self.log_textbox.tag_config("red",foreground="red",underline=1)
        self.log_textbox.tag_add("yellow", 0.0, 0.5)
        self.log_textbox.tag_config("yellow",foreground="yellow")
        self.log_textbox.tag_add("green", 0.0, 0.5)
        self.log_textbox.tag_config("green",foreground="lightgreen")
        self.log_textbox.tag_add("console", 0.0, 0.5)
        self.log_textbox.tag_config("console",foreground="red",underline=1) #,font=('Helvetica',36,'bold')
        self.log_textbox.insert(1.0, "\tConsole:", tags="console")
        self.log_textbox.configure(font=("Terminal",15,"normal"))
        self.start_Window = None
        self.loadResult_window =None
        self.Target_Window=None
        # create tabview
        self.results_tabview = customtkinter.CTkTabview(self, width=1450,height=600)
        self.results_tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.results_tabview.add("Results")
        self.results_tabview.add("Skipfish")
        self.results_tabview.add("wapiti")
        self.results_tabview.add("Nikto")
        self.results_tabview.add("OWASP ZAP")
        self.results_tabview.add("Nuclei")
        #our resault tab view:
        self.label_1 = customtkinter.CTkLabel(self.results_tabview.tab("Results"),text="Result Table:", justify=customtkinter.CENTER)
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

        self.templateresult={
	"target_name":"name",        
        "sql_meta":"null",
        "blind_meta":"null",
        "xss_meta":"null",
        "shell_meta":"null",
        "xslt_meta":"null",
        "xml_meta":"null",
        "xxe_meta":"null",
        "code_meta":"null",
        "os_meta":"null",
        "html_meta":"null",
        "template_meta":"null",
        "crlf_meta":"null",
        "ognl_meta":"null",
        "host_meta":"null",
        "sql1":"null",
        "sql2":"null",
        "sql3":"null",
        "sql4":"null",
        "sql5":"null",
        "blind3":"null",
        "blind5":"null",
        "xss1":"null",
        "xss2":"null",
        "xss3":"null",
        "xss4":"null",
        "xss5":"null",
        "shell2":"null",
        "shell5":"null",
        "xslt1":"null",
        "xslt4":"null",
        "xml1":"null",
        "xml2":"null",
        "xml4":"null",
        "xml5":"null",
        "xxe1":"null",
        "xxe3":"null",
        "xxe5":"null",
        "code1":"null",
        "code4":"null",
        "code5":"null",
        "os1":"null",
        "os3":"null",
        "os5":"null",
        "html4":"null",
        "html5":"null",
        "template1":"null",
        "crlf1":"null",
        "crlf2":"null",
        "crlf3":"null",
        "crlf5":"null",
        "ognl2":"null",
        "ognl5":"null",
        "host2":"null",
        "host5":"null"}
        fileObject = open("weights/weights.json", "r")
        jsonContent = fileObject.read()
        self.weights = json.loads(jsonContent)
        fileObject.close()

    
    def minimize(self):
        self.log_textbox.configure(width=350)
        self.slidd=0    
        self.sidebar_frame.grid_forget()
        self.sidebar_frame = customtkinter.CTkFrame(self, width=30, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        maximize=customtkinter.CTkImage(light_image=Image.open("images/maximize.png"),dark_image=Image.open("images/maximize.png"),size=(20, 20))
        self.maxi =customtkinter.CTkButton(self.sidebar_frame,text="",image=maximize,width=20,height=20,fg_color='transparent',command=self.maximize)#,command=
        self.maxi.grid(row=0,column=0,sticky="ne")                  
    def maximize(self):
        self.log_textbox.configure(width=170)    
        self.slidd=1
        self.sidebar_frame.grid_forget()
        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        minimize=customtkinter.CTkImage(light_image=Image.open("images/close.png"),dark_image=Image.open("images/close.png"),size=(20, 20))
        self.close =customtkinter.CTkButton(self.sidebar_frame,text="",image=minimize,width=20,height=20,fg_color='transparent',command=self.minimize)#,command=
        self.close.grid(row=0,column=5,sticky="ne")       
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="META-Scanner", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=0, pady=(20, 10))
        self.startnewscan_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_start_Window,text="start Scan")
        self.startnewscan_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_load_Window,text="Load Result")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.chec_for_scanner_sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.save_as_html,text="Save As HTML")
        self.chec_for_scanner_sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join("images/meta.png")), size=(190, 150))   
        self.navigation_frame_label = customtkinter.CTkLabel(self.sidebar_frame, text="", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=5, column=0,columnspan=3, padx=0, pady=20)
        
        
        
        self.wapiti = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.wapiti.grid(row=6, column=0, padx=20, pady=3)
        self.zap = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.zap.grid(row=7, column=0, padx=20, pady=3)
        self.nuclei = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.nuclei.grid(row=8, column=0, padx=20, pady=3)
        self.nikto = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.nikto.grid(row=9, column=0, padx=20, pady=3)
        self.skipfish = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.skipfish.grid(row=10, column=0, padx=20, pady=3)
        
        
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[ "System","Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 10))


        
    def open_check(self,ID):  
        self.results_tabview.configure(height=10)
        self.CheckVul = customtkinter.CTkFrame(self, width=600,height=800)
        self.CheckVul.grid(row=1,rowspan=2, column=1,columnspan=2, padx=(5, 0), pady=(5, 0), sticky="nsew")
        
        self.CheckVul_in = customtkinter.CTkFrame(self.CheckVul)
        self.CheckVul_in.pack(pady=0,padx=0,side="top",fill="x",expand=True)
        self.CheckVul_out = customtkinter.CTkFrame(self.CheckVul)
        self.CheckVul_out.pack(pady=0,padx=0,side="top",fill="x",expand=True)
        
        closs=customtkinter.CTkImage(light_image=Image.open("images/cancel2.png"),dark_image=Image.open("images/cancel2.png"),size=(20, 20))
        self.close =customtkinter.CTkButton(self.CheckVul_in,text="",image=closs,width=20,height=20,fg_color='transparent',command=self.close_check)
        self.close.pack(pady=0,padx=0,side="right",anchor="ne")          
        self.CheckVul_in_description=customtkinter.CTkLabel(self.CheckVul_in,text="Description",width=550)
        self.CheckVul_in_Method_http=customtkinter.CTkLabel(self.CheckVul_in,text="Method \n http Request",width=200)        
        self.CheckVul_in_Vector=customtkinter.CTkLabel(self.CheckVul_in,text="Vector | command",width=250)
        self.CheckVul_in_Vulnerability=customtkinter.CTkLabel(self.CheckVul_in,text="Vulnerability",width=150)                
        self.CheckVul_in_Vulnerability.pack(pady=0,padx=5,side="left",anchor="nw")
        self.CheckVul_in_Method_http.pack(pady=0,padx=5,side="left",anchor="nw")
        self.CheckVul_in_Vector.pack(pady=0,padx=5,side="left",anchor="nw")
        self.CheckVul_in_description.pack(pady=0,padx=5,side="left",anchor="nw")
        xer="_______________________________________________________________________________________________________________________________________________________________________________________________________"
#        self.labelll=customtkinter.CTkLabel(self.CheckVul_in,text=xer,height=2).pack(pady=0,padx=0,anchor="center")
        
        self.name=customtkinter.CTkLabel(self.CheckVul_out,text=ID,width=150).pack(pady=100,padx=5,side="left",anchor="se")     
    
        self.http=customtkinter.CTkTextbox(self.CheckVul_out,width=200,height=280,fg_color="transparent",border_width=1,border_color="white",corner_radius=0)
#        self.http.insert(tkinter.END, "\ntest")
        self.http.pack(side="left",anchor="se",padx=5)

        self.command=customtkinter.CTkTextbox(self.CheckVul_out,width=250,height=280,fg_color="transparent",border_width=1,border_color="white",corner_radius=0)
        self.command.pack(side="left",anchor="se",padx=5)
        self.desc=customtkinter.CTkTextbox(self.CheckVul_out,width=700,height=280,fg_color="transparent",border_width=1,border_color="white",corner_radius=0,font=("ariel",15))
        self.desc.tag_add("red", 0.0, 0.5)
        self.desc.tag_config("red",foreground="red",underline=1)       
        self.desc.pack(side="left",anchor="se",padx=5)
        num=0
        
        
        
        if ("SQL Injection" in ID):        
                self.desc.insert(tkinter.END, "SQL injection vulnerabilities allow an attacker to alter the queries executed on the backend database. An attacker may then be able to extract or modify information stored in the database or even escalate his privileges on the system.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"To protect against SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.")

                for i in range(len(self.Results[0]["SQL Injection"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} ||URL:{}\n".format(num,self.Results[0]["SQL Injection"][i]["method"],self.Results[0]["SQL Injection"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}\n".format(num,self.Results[0]["SQL Injection"][i]["parameter"]))                     

                            #Skipfish tyhto fl Sql injection.
                if self.Results[2]['nikto_vulnerability']['sql_injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['sql_injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['sql_injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['sql_injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:\n".format(num) )                     
                 
                if self.Results[3]["SQL Injection"][0]+self.Results[3]["SQL Injection - MySQL"][0]+self.Results[3]["SQL Injection - Hypersonic SQL"][0]+self.Results[3]["SQL Injection - Oracle"][0]+self.Results[3]["SQL Injection - PostgreSQL"][0]+self.Results[3]["SQL Injection - SQLite"][0]+self.Results[3]["SQL Injection - MsSQL"][0]  > 0 :
                       for i in range(self.Results[3]["SQL Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection"][1][i][0] ,self.Results[3]["SQL Injection"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["SQL Injection"][2][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - MySQL"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - MySQL"][1][i][0] ,self.Results[3]["SQL Injection - MySQL"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["SQL Injection - MySQL"][2][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - Hypersonic SQL"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - Hypersonic SQL"][1][i][0] ,self.Results[3]["SQL Injection - Hypersonic SQL"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["SQL Injection - Hypersonic SQL"][2][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - Oracle"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - Oracle"][1][i][0] ,self.Results[3]["SQL Injection - Oracle"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["SQL Injection - Oracle"][2][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - PostgreSQL"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - PostgreSQL"][1][i][0] ,self.Results[3]["SQL Injection - PostgreSQL"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["SQL Injection - PostgreSQL"][2][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - SQLite"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - SQLite"][1][i][0] ,self.Results[3]["SQL Injection - SQLite"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["SQL Injection - SQLite"][2][i]) )                     
                       for i in range(self.Results[3]["SQL Injection - MsSQL"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SQL Injection - MsSQL"][1][i][0] ,self.Results[3]["SQL Injection - MsSQL"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["SQL Injection - MsSQL"][2][i]) )                     
 
                for i in self.Results[4]:
                    if "sql" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}\n".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     
              
        if ("Blind SQL injection" in ID):     
                self.desc.insert(tkinter.END, "Blind SQL injection is a technique that exploits a vulnerability occurring in the database of an application. This kind of vulnerability is harder to detect than basic SQL injections because no error message will be displayed on the webpage.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Same as Sql injection To protect against blind SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.")

                for i in range(len(self.Results[0]["Blind SQL Injection"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} |\n|URL:{}\n".format(num,self.Results[0]["Blind SQL Injection"][i]["method"],self.Results[0]["Blind SQL Injection"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}\n".format(num,self.Results[0]["Blind SQL Injection"][i]["parameter"]))                     
                for i in self.Results[4]:
                    if "blind sql" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     

        if ("Cross Site Scripting injection" in ID):     
                self.desc.insert(tkinter.END, "Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications which allow code injection by malicious web users into the web pages viewed by other users. Examples of such code include HTML code and client-side scripts.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"The best way to protect a web application from XSS attacks is ensure that the application performs validation of all headers, cookies, query strings, form fields, and hidden fields. Encoding user supplied output in the server side can also defeat XSS vulnerabilities by preventing inserted scripts from being transmitted to users in an executable form. Applications can gain significant protection from javascript based attacks by converting the following characters in all generated output to the appropriate HTML entity encoding:<, >, &, ', (, ), #, %, ; , +, -")

                for i in range(len(self.Results[0]["Cross Site Scripting"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} |\n|URL:{}\n".format(num,self.Results[0]["Cross Site Scripting"][i]["method"],self.Results[0]["Cross Site Scripting"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}\n".format(num,self.Results[0]["Cross Site Scripting"][i]["parameter"]))        
                              
                if self.Results[2]['nikto_vulnerability']['XSS injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['XSS injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['XSS injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['XSS injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:\n".format(num) )       
                           
                                        
                if self.Results[3]["Cross Site Scripting (DOM Based)"][0]+self.Results[3]["Cross Site Scripting (Reflected)"][0]+self.Results[3]["Cross Site Scripting (Persistent)"][0]+self.Results[3]["Cross Site Scripting (Persistent) - Prime"][0]+self.Results[3]["Cross Site Scripting (Persistent) - Spider"][0]  > 0 :
                       for i in range(self.Results[3]["Cross Site Scripting (DOM Based)"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (DOM Based)"][1][i][0] ,self.Results[3]["Cross Site Scripting (DOM Based)"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Cross Site Scripting (DOM Based)"][2][i]) )
                       for i in range(self.Results[3]["Cross Site Scripting (Reflected)"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (Reflected)"][1][i][0] ,self.Results[3]["Cross Site Scripting (Reflected)"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Cross Site Scripting (Reflected)"][2][i]) )
                       for i in range(self.Results[3]["Cross Site Scripting (Persistent)"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent)"][1][i][0] ,self.Results[3]["Cross Site Scripting (Persistent)"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent)"][2][i]) )
                       for i in range(self.Results[3]["Cross Site Scripting (Persistent) - Prime"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent) - Prime"][1][i][0] ,self.Results[3]["Cross Site Scripting (Persistent) - Prime"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent) - Prime"][2][i]) )
                       for i in range(self.Results[3]["Cross Site Scripting (Persistent) - Spider"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent) - Spider"][1][i][0] ,self.Results[3]["Cross Site Scripting (Persistent) - Spider"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Cross Site Scripting (Persistent) - Spider"][2][i]) )

                for i in self.Results[4]:
                    if "cross"in i.lower() and "site"in i.lower() and "scripting" in i.lower() or "xss" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     

                if self.Results[1]['40101'][1] >0:
                     for i in range(self.Results[1]['40101'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['40101'][2][i][0],self.Results[1]['40101'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None\n".format(num) )                     
                if self.Results[1]['40105'][1] >0:
                     for i in range(self.Results[1]['40105'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['40105'][2][i][0],self.Results[1]['40105'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None\n".format(num) )
                if self.Results[1]['40102'][1] >0:
                     for i in range(self.Results[1]['40102'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['40102'][2][i][0],self.Results[1]['40102'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None\n".format(num) )

        if ("Shell injection" in ID):    
                self.desc.insert(tkinter.END, "Shell injection is a type of web vulnerability that occurs when an attacker is able to inject malicious shell commands into a web application. This can occur through user input fields, system calls, or other points of input that allow the attacker to execute arbitrary shell commands on the server.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Validate input: Validate all user input, including form data, URL parameters, and cookies, \nSanitize input: Sanitize all input data to remove any potentially malicious shell commands or special characters.\nUse parameterized queries\nUse a whitelist of allowed commands: Use a whitelist of allowed shell commands to ensure that only trusted commands are executed\nUse restricted permissions: Use restricted permissions to limit the access that web applications have to the underlying operating system")
                if self.Results[1]['50102'][1] >0:
                     for i in range(self.Results[1]['50102'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['50102'][2][i][0],self.Results[1]['50102'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None\n".format(num) )                             
                for i in self.Results[4]:
                    if "shell" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     
         
        if ("XSLT injection" in ID):         
                self.desc.insert(tkinter.END, "XSLT web injection is a type of security vulnerability that occurs when an attacker injects malicious code into an XSL stylesheet, which is used to transform XML data into HTML for display on a web page. The injected code can be used to steal sensitive information, manipulate the appearance of the page, or launch further attacks\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Input validation: Validate all user input, including XML data and XSL stylesheets, to ensure that they meet expected formats and do not contain any malicious code.\nUse parameterized XSLT stylesheets: Avoid embedding user input directly into XSLT stylesheets. Instead, use parameters to pass user input into the stylesheet.\nUse Content Security Policy (CSP): Implement a content security policy that restricts the use of inline scripts and styles, and only allows trusted sources for external resources.")
                if self.Results[2]['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:\n".format(num) )       
                                        
                if self.Results[3]["XSLT Injection"][0] > 0 :
                       for i in range(self.Results[3]["XSLT Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["XSLT Injection"][1][i][0] ,self.Results[3]["XSLT Injection"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["XSLT Injection"][2][i]) )
                            
        if ("XML injection" in ID):         
                self.desc.insert(tkinter.END, "XML web injection is a type of security vulnerability that occurs when an attacker injects malicious code into an XML file, which is used to store and transfer data between applications. The injected code can be used to steal sensitive information, manipulate the data, or launch further attacks.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Input validation: Validate all user input, including XML data, to ensure that it meets expected formats and does not contain any malicious code.\nUse parameterized XML: Avoid embedding user input directly into XML files. Instead, use parameters to pass user input into the XML file.\nUse XML digital signatures: Implement XML digital signatures to ensure the integrity and authenticity of the XML data. This will prevent attackers from tampering with the XML file.\nUse XML encryption: Implement XML encryption to protect sensitive data in the XML file from being accessed by unauthorized parties.")         
                if self.Results[1]['50101'][1] >0:
                     for i in range(self.Results[1]['50101'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['50101'][2][i][0],self.Results[1]['50101'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None\n".format(num) )  
                                                      
                if self.Results[2]['nikto_vulnerability']['XML injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['XML injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['XML injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['XML injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:\n".format(num) )       
                if self.Results[3]["SOAP XML Injection"][0] > 0 :
                       for i in range(self.Results[3]["XSLT Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["SOAP XML Injection"][1][i][0] ,self.Results[3]["SOAP XML Injection"][1][i][0]) )
                           self.command.insert(tkinter.END, "\n{}-)InputVectore:{}\n".format(num,self.Results[3]["SOAP XML Injection"][2][i]) )
         
                for i in self.Results[4]:
                    if "xml"in i.lower() and "external" not in i.lower() and "entity" not in i.lower():                               
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     
         
        if ("XML external entities (XXE)" in ID):    
                self.desc.insert(tkinter.END, "An XML External Entity attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"The safest way to prevent XXE is always to disable DTDs (External Entities) completely.\nDisable External Entities: The simplest solution to prevent XXE attacks is to disable the use of external entities altogether. This can be done by setting the parser's external-general-entities and external-parameter-entities properties to false.")         

                for i in range(len(self.Results[0]["XML External Entity"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} |\n|URL:{}\n".format(num,self.Results[0]["XML External Entity"][i]["method"],self.Results[0]["XML External Entity"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}\n".format(num,self.Results[0]["XML External Entity"][i]["parameter"]))                            
                if self.Results[3]["XML External Entity Attack"][0] > 0 :
                       for i in range(self.Results[3]["XSLT Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["XML External Entity Attack"][1][i][0] ,self.Results[3]["XML External Entity Attack"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["XML External Entity Attack"][2][i]) )
                for i in self.Results[4]:
                    if "xml"in i.lower() and "external"  in i.lower() and "entity" in i.lower():                               
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                               
                  
        if ("code injection" in ID):    
                self.desc.insert(tkinter.END, "web code injection attack where an attacker can inject and execute arbitrary code on a remote server or application. This can lead to complete compromise of the system and data theft.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Input validation: Validate all user input, including form data, URL parameters, and cookies,\nUse a web application firewall: Implement a web application firewall (WAF) to block common code injection attacks")    

                     
                     
                if self.Results[2]['nikto_vulnerability']['remote source injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['remote source injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['remote source injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['remote source injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:\n".format(num) )                         
                             
         
                if self.Results[3]["Server Side Code Injection"][0]+self.Results[3]["Server Side Code Injection - PHP Code Injection"][0]+self.Results[3]["Server Side Code Injection - ASP Code Injection"][0]+self.Results[3]["Remote Code Execution - CVE-2012-1823"][0] > 0 :
                       for i in range(self.Results[3]["Remote Code Execution - CVE-2012-1823"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Remote Code Execution - CVE-2012-1823"][1][i][0] ,self.Results[3]["Remote Code Execution - CVE-2012-1823"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Remote Code Execution - CVE-2012-1823"][2][i]) )                     
                       for i in range(self.Results[3]["Server Side Code Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Server Side Code Injection"][1][i][0] ,self.Results[3]["Server Side Code Injection"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Server Side Code Injection"][2][i]) )                     
                       for i in range(self.Results[3]["Server Side Code Injection - PHP Code Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Server Side Code Injection - PHP Code Injection"][1][i][0] ,self.Results[3]["Server Side Code Injection - PHP Code Injection"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Server Side Code Injection - PHP Code Injection"][2][i]) )                     
                       for i in range(self.Results[3]["Server Side Code Injection - ASP Code Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Server Side Code Injection - ASP Code Injection"][1][i][0] ,self.Results[3]["Server Side Code Injection - ASP Code Injection"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Server Side Code Injection - ASP Code Injection"][2][i]) )                     

                for i in self.Results[4]:
                    if "code" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     

        if ("OS command injection" in ID):    
                self.desc.insert(tkinter.END, "This attack consists in executing system commands on the server. The attacker tries to inject this commands in the request parameters.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Prefer working without user input when using file system calls.")                  

                for i in range(len(self.Results[0]["Command execution"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} |\n|URL:{}\n".format(num,self.Results[0]["Command execution"][i]["method"],self.Results[0]["Command execution"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}\n".format(num,self.Results[0]["Command execution"][i]["parameter"]))        

                          
                if self.Results[3]["Remote OS Command Injection"][0] > 0 :
                       for i in range(self.Results[3]["Remote OS Command Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Remote OS Command Injection"][1][i][0] ,self.Results[3]["Remote OS Command Injection"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Remote OS Command Injection"][2][i]) )                     
                for i in self.Results[4]:
                    if "command" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     
        if ("html injection" in ID):        
                self.desc.insert(tkinter.END, "HTML injection is a type of web vulnerability that occurs when an attacker is able to inject malicious HTML code into a web page. This can be used to perform a variety of attacks, including cross-site scripting (XSS) attacks, phishing attacks, and data theft.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Validate input: Validate all user input, including form data, URL parameters, and cookies\n Use input filtering to prevent user input that could be used in an HTML injection attack.\nSanitize input: Sanitize all input data to remove any potentially malicious HTML tags or attributes. \nUse a content security policy (CSP): Use a CSP to restrict the types of content that can be loaded on a web page.\nUse context-aware escaping: Use context-aware escaping to properly encode output data for the context in which it will be displayed")
                if self.Results[2]['nikto_vulnerability']['html injection']['number'] >0:
                      for i in range(self.Results[2]['nikto_vulnerability']['html injection']['number']):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[2]['nikto_vulnerability']['html injection']['method_msg'][i][0] ,self.Results[2]['nikto_vulnerability']['html injection']['method_msg'][i][2]) )
                           self.command.insert(tkinter.END, "\n{}-)None:\n".format(num) )       


                for i in self.Results[4]:
                    if "html" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     

        if ("Template injection" in ID):        
                self.desc.insert(tkinter.END, "Template Injection is a type of web vulnerability that occurs when an attacker is able to inject malicious code into a template file used by a web application, typically in a template engine. This can lead to a variety of attacks, such as data theft, remote code execution, and denial of service.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"input validation: Validate all user input, including form data, URL parameters, and cookies,\nUse safe templates: Use templates that have built-in safety mechanisms and do not allow code execution. For example, using Handlebars.js instead of EJS\nUse a secure template engine: Use a template engine that has built-in security features, such as automatic escaping and input validation.\nEnforce strict separation of concerns: Make sure that templates do not contain any business logic or sensitive data, and keep them separate from application code.")
                if self.Results[3]["Server Side Template Injection"][0] > 0 :
                       for i in range(self.Results[3]["Server Side Template Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["Server Side Template Injection"][1][i][0] ,self.Results[3]["Server Side Template Injection"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["Server Side Template Injection"][2][i]))                     
        if ("CRLF injection" in ID):        
                self.desc.insert(tkinter.END, "The term CRLF refers to Carriage Return (ASCII 13, \\r) Line Feed (ASCII 10, \\n). A CRLF Injection attack occurs when a user manages to submit a CRLF into an application. This is most commonly done by modifying an HTTP parameter or URL.\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Check the submitted parameters and do not allow CRLF to be injected when it is not expected.")

                for i in range(len(self.Results[0]["CRLF Injection"])):    #wapiti Result Sqlinjection fl check (Riglo)
                     num+=1
                     self.http.insert(tkinter.END, "\n{}-)Method:{} ||URL:{}\n".format(num,self.Results[0]["CRLF Injection"][i]["method"],self.Results[0]["CRLF Injection"][i]["path"] ) )
                     self.command.insert(tkinter.END, "\n{}-)Parammeter:{}\n".format(num,self.Results[0]["CRLF Injection"][i]["parameter"]))                     

                if self.Results[3]["CRLF Injection"][0] > 0 :
                       for i in range(self.Results[3]["CRLF Injection"][0]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)Method:{} |\n| URL:{}\n".format(num,self.Results[3]["CRLF Injection"][1][i][0] ,self.Results[3]["CRLF Injection"][1][i][1]) )
                           self.command.insert(tkinter.END, "\n{}-){}\n".format(num,self.Results[3]["CRLF Injection"][2][i]) )                     
                for i in self.Results[4]:
                    if "crlf" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     
                if self.Results[1]['40103'][1] >0:
                     for i in range(self.Results[1]['50102'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['40103'][2][i][0],self.Results[1]['40103'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None\n".format(num) )                             




        if ("OGNL injection" in ID):        
                self.desc.insert(tkinter.END, "OGNL (Object-Graph Navigation Language) injection is a type of web vulnerability that occurs when an attacker is able to inject malicious code into an application that uses OGNL expressions to evaluate and execute user input\n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Avoid using OGNL expressions in user input: Avoid using OGNL expressions that are based on user input. Instead, use OGNL expressions that are based on fixed, predefined values.\nUse safe OGNL expressions: Use OGNL expressions that have built-in safety mechanisms and do not allow code execution")
                if self.Results[1]['10902'][1] >0:
                     for i in range(self.Results[1]['50102'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['10902'][2][i][0],self.Results[1]['10902'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None\n".format(num) )                             
                for i in self.Results[4]:
                    if "ognl" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     


        if ("Host Header injection" in ID):        
                self.desc.insert(tkinter.END, "Host header injection happens more often in Location ad set-cookies in the HTTP header request, when a web application allows an attacker to inject and manipulate its own HTTP header request inside the application server response. and that would allow for other attacks like HTTP response splitting, Fixation session, invalid redirect,and more... \n ")
                self.desc.insert(tkinter.END,"Solution:\n",tags="red")
                self.desc.insert(tkinter.END,"Use a whitelist of allowed hostnames: Use a whitelist of allowed hostnames to ensure that only trusted hostnames are accepted.\nUse HTTPS: Use HTTPS to encrypt all web traffic, including the host header.\nSet a strict SameSite policy: Set a strict SameSite policy on cookies to prevent session hijacking attacks")
                if self.Results[1]['10902'][1] >0:
                     for i in range(self.Results[1]['30901'][1]):
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-Method:{}  || URL:{}".format(num,self.Results[1]['30901'][2][i][0],self.Results[1]['30901'][2][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)None\n".format(num) )                             
                for i in self.Results[4]:
                    if "host header" in i.lower():                           
                           num+=1
                           self.http.insert(tkinter.END, "\n{}-)URL:{}".format(num,self.Results[4][i][1] ) )
                           self.command.insert(tkinter.END, "\n{}-)Curl Command:{}\n".format(num,self.Results[4][i][2]) )                     









        self.desc.configure(state="disabled")
        self.command.configure(state="disabled")
        self.http.configure(state="disabled")
    def close_check(self):
        self.results_tabview.configure(height=600)
        self.CheckVul.grid_forget()    
    def createResaults(self):
        self.my_frame = MyFrame_My_Result(master=self.results_tabview.tab("Results"))
        self.my_frame.bind_all("<Button-4>", lambda e: self.my_frame._parent_canvas.yview("scroll", -1, "units"))
        self.my_frame.bind_all("<Button-5>", lambda e: self.my_frame._parent_canvas.yview("scroll", 1, "units"))
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
                   #self.my_frame.vul_label[1][1].configure(text_color="red",text=int(self.my_frame.vul_label[1][1].cget("text"))+number['Blind SQL Injection'])
                   self.my_frame.vul_label[1][5].configure(text=self.my_frame.vul_label[1][5].cget("text")+number['Blind SQL Injection'],text_color="red")
                        
            if number['SQL Injection'] > 0:
                   #self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+number['SQL Injection'])
                   self.my_frame.vul_label[0][5].configure(text=self.my_frame.vul_label[0][5].cget("text")+number['SQL Injection'],text_color="red")
            if number['Cross Site Scripting'] > 0:
                   #self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+number['Cross Site Scripting'])
                   self.my_frame.vul_label[2][5].configure(text=self.my_frame.vul_label[2][5].cget("text")+number['Cross Site Scripting'],text_color="red")
            if number['XML External Entity'] > 0:
                   #self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+number['XML External Entity'])
                   self.my_frame.vul_label[6][5].configure(text=self.my_frame.vul_label[6][5].cget("text")+number['XML External Entity'],text_color="red")
            if number['Command execution'] > 0:
                   #self.my_frame.vul_label[8][1].configure(text_color="red",text=int(self.my_frame.vul_label[8][1].cget("text"))+number['Command execution'])
                   self.my_frame.vul_label[8][5].configure(text=self.my_frame.vul_label[8][5].cget("text")+number['Command execution'],text_color="red")
            if number['CRLF Injection'] > 0:
                   #self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+number['CRLF Injection'])
                   self.my_frame.vul_label[11][5].configure(text=self.my_frame.vul_label[11][5].cget("text")+number['CRLF Injection'],text_color="red") 
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
                             #self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+all_resaults[i][1])
                             self.my_frame.vul_label[0][4].configure(text=self.my_frame.vul_label[0][4].cget("text")+all_resaults[i][1],text_color="red")
                      elif "XSS vector" in all_resaults[i][0] :
                             #self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+all_resaults[i][1])
                             self.my_frame.vul_label[2][4].configure(text=self.my_frame.vul_label[2][4].cget("text")+all_resaults[i][1],text_color="red")
                      elif "Shell injection" in all_resaults[i][0] :
                             #self.my_frame.vul_label[3][1].configure(text_color="red",text=int(self.my_frame.vul_label[3][1].cget("text"))+all_resaults[i][1])
                             self.my_frame.vul_label[3][4].configure(text=self.my_frame.vul_label[3][4].cget("text")+all_resaults[i][1],text_color="red")
                      elif "XML injection" in all_resaults[i][0] :
                             #self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+all_resaults[i][1])
                             self.my_frame.vul_label[5][4].configure(text=self.my_frame.vul_label[5][4].cget("text")+all_resaults[i][1],text_color="red")
                      elif "HTTP response header splitting" in all_resaults[i][0] :
                             #self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+all_resaults[i][1])
                             self.my_frame.vul_label[11][4].configure(text=self.my_frame.vul_label[11][4].cget("text")+all_resaults[i][1],text_color="red")
                      elif "OGNL-like parameter behavior" in all_resaults[i][0] :
                             #self.my_frame.vul_label[12][1].configure(text_color="red",text=int(self.my_frame.vul_label[12][1].cget("text"))+all_resaults[i][1])
                             self.my_frame.vul_label[12][4].configure(text=self.my_frame.vul_label[12][4].cget("text")+all_resaults[i][1],text_color="red")
                      elif "HTTP header injection" in all_resaults[i][0] :
                             #self.my_frame.vul_label[13][1].configure(text_color="red",text=int(self.my_frame.vul_label[13][1].cget("text"))+all_resaults[i][1])
                             self.my_frame.vul_label[13][4].configure(text=self.my_frame.vul_label[13][4].cget("text")+all_resaults[i][1],text_color="red")     
                  
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
                     #self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['sql_injection']['number'])
                     self.my_frame.vul_label[0][6].configure(text=self.my_frame.vul_label[0][6].cget("text")+Nikto_resaults['nikto_vulnerability']['sql_injection']['number'],text_color="red")
            
            if Nikto_resaults['nikto_vulnerability']['XSS injection']['number'] >0:
                     #self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XSS injection']['number'])
                     self.my_frame.vul_label[2][6].configure(text=self.my_frame.vul_label[2][6].cget("text")+Nikto_resaults['nikto_vulnerability']['XSS injection']['number'],text_color="red")
                                            
            if Nikto_resaults['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'] >0:
                     #self.my_frame.vul_label[4][1].configure(text_color="red",text=int(self.my_frame.vul_label[4][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'])
                     self.my_frame.vul_label[4][6].configure(text=self.my_frame.vul_label[4][6].cget("text")+Nikto_resaults['nikto_vulnerability']['XSLT_Extensible Stylesheet Language Transformations injection']['number'],text_color="red")

            if Nikto_resaults['nikto_vulnerability']['XML injection']['number'] >0:
                     #self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['XML injection']['number'])
                     self.my_frame.vul_label[5][6].configure(text=self.my_frame.vul_label[5][6].cget("text")+Nikto_resaults['nikto_vulnerability']['XML injection']['number'],text_color="red")

            if Nikto_resaults['nikto_vulnerability']['remote source injection']['number'] >0:
                     #self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['remote source injection']['number'])
                     self.my_frame.vul_label[7][6].configure(text=self.my_frame.vul_label[7][6].cget("text")+Nikto_resaults['nikto_vulnerability']['remote source injection']['number'],text_color="red")

            if Nikto_resaults['nikto_vulnerability']['html injection']['number'] >0:
                     #self.my_frame.vul_label[9][1].configure(text_color="red",text=int(self.my_frame.vul_label[9][1].cget("text"))+Nikto_resaults['nikto_vulnerability']['html injection']['number'])
                     self.my_frame.vul_label[9][6].configure(text=self.my_frame.vul_label[9][6].cget("text")+Nikto_resaults['nikto_vulnerability']['html injection']['number'],text_color="red")


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
#                 self.my_frame.vul_label[13][4].configure(text=self.my_frame.vul_label[13][4].cget("text")+,text_color="red")

            if zap_resaults["SQL Injection"][0]+zap_resaults["SQL Injection - MySQL"][0]+zap_resaults["SQL Injection - Hypersonic SQL"][0]+zap_resaults["SQL Injection - Oracle"][0]+zap_resaults["SQL Injection - PostgreSQL"][0]+zap_resaults["SQL Injection - SQLite"][0]+zap_resaults["SQL Injection - MsSQL"][0]  > 0 :
                 #self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+zap_resaults["SQL Injection"][0]+zap_resaults["SQL Injection - MySQL"][0]+zap_resaults["SQL Injection - Hypersonic SQL"][0]+zap_resaults["SQL Injection - Oracle"][0]+zap_resaults["SQL Injection - PostgreSQL"][0]+zap_resaults["SQL Injection - SQLite"][0]+zap_resaults["SQL Injection - MsSQL"][0])
                 
                 self.my_frame.vul_label[0][2].configure(text=self.my_frame.vul_label[0][2].cget("text")+zap_resaults["SQL Injection"][0]+zap_resaults["SQL Injection - MySQL"][0]+zap_resaults["SQL Injection - Hypersonic SQL"][0]+zap_resaults["SQL Injection - Oracle"][0]+zap_resaults["SQL Injection - PostgreSQL"][0]+zap_resaults["SQL Injection - SQLite"][0]+zap_resaults["SQL Injection - MsSQL"][0],text_color="red")

            if zap_resaults["Cross Site Scripting (Reflected)"][0]+zap_resaults["Cross Site Scripting (Persistent)"][0]+zap_resaults["Cross Site Scripting (Persistent) - Prime"][0]+zap_resaults["Cross Site Scripting (Persistent) - Spider"][0]+zap_resaults["Cross Site Scripting (DOM Based)"][0] > 0 :     
                 #self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+zap_resaults["Cross Site Scripting (Reflected)"][0]+zap_resaults["Cross Site Scripting (Persistent)"][0]+zap_resaults["Cross Site Scripting (Persistent) - Prime"][0]+zap_resaults["Cross Site Scripting (Persistent) - Spider"][0]+zap_resaults["Cross Site Scripting (DOM Based)"][0])
                 self.my_frame.vul_label[2][2].configure(text=self.my_frame.vul_label[2][2].cget("text")+zap_resaults["Cross Site Scripting (Reflected)"][0]+zap_resaults["Cross Site Scripting (Persistent)"][0]+zap_resaults["Cross Site Scripting (Persistent) - Prime"][0]+zap_resaults["Cross Site Scripting (Persistent) - Spider"][0]+zap_resaults["Cross Site Scripting (DOM Based)"][0],text_color="red")

            if zap_resaults["XSLT Injection"][0] > 0:
                  #self.my_frame.vul_label[4][1].configure(text_color="red",text=int(self.my_frame.vul_label[4][1].cget("text"))+zap_resaults["XSLT Injection"][0])
                  self.my_frame.vul_label[4][2].configure(text=self.my_frame.vul_label[4][2].cget("text")+zap_resaults["XSLT Injection"][0],text_color="red")
                  
            if zap_resaults["SOAP XML Injection"][0] >0 :
                  #self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+zap_resaults["SOAP XML Injection"][0])
                  self.my_frame.vul_label[5][2].configure(text=self.my_frame.vul_label[5][2].cget("text")+zap_resaults["SOAP XML Injection"][0],text_color="red")                  
            if zap_resaults["XML External Entity Attack"][0] >0 :      
                  #self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+zap_resaults["XML External Entity Attack"][0])
                  self.my_frame.vul_label[6][2].configure(text=self.my_frame.vul_label[6][2].cget("text")+zap_resaults["XML External Entity Attack"][0],text_color="red")                  
                                   
            if zap_resaults["Server Side Code Injection"][0]+zap_resaults["Server Side Code Injection - PHP Code Injection"][0]+zap_resaults["Server Side Code Injection - ASP Code Injection"][0]+zap_resaults["Remote Code Execution - CVE-2012-1823"][0] > 0 :
                  #self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+zap_resaults["Server Side Code Injection"][0]+zap_resaults["Server Side Code Injection - PHP Code Injection"][0]+zap_resaults["Server Side Code Injection - ASP Code Injection"][0]+zap_resaults["Remote Code Execution - CVE-2012-1823"][0])
                  self.my_frame.vul_label[7][2].configure(text=self.my_frame.vul_label[7][2].cget("text")+zap_resaults["Server Side Code Injection"][0]+zap_resaults["Server Side Code Injection - PHP Code Injection"][0]+zap_resaults["Server Side Code Injection - ASP Code Injection"][0]+zap_resaults["Remote Code Execution - CVE-2012-1823"][0],text_color="red")
                 
                 
            if zap_resaults["Remote OS Command Injection"][0] > 0 :
                  #self.my_frame.vul_label[8][1].configure(text_color="red",text=int(self.my_frame.vul_label[8][1].cget("text"))+zap_resaults["Remote OS Command Injection"][0])
                  self.my_frame.vul_label[8][2].configure(text=self.my_frame.vul_label[8][2].cget("text")+zap_resaults["Remote OS Command Injection"][0],text_color="red")


            if zap_resaults["Server Side Template Injection"][0] > 0 :
                  #self.my_frame.vul_label[10][1].configure(text_color="red",text=int(self.my_frame.vul_label[10][1].cget("text"))+zap_resaults["Server Side Template Injection"][0] )      
                  self.my_frame.vul_label[10][2].configure(text=self.my_frame.vul_label[10][2].cget("text")+zap_resaults["Server Side Template Injection"][0],text_color="red")
                                        
            if zap_resaults["CRLF Injection"][0] > 0:
                  #self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+zap_resaults["CRLF Injection"][0])
                  self.my_frame.vul_label[11][2].configure(text=self.my_frame.vul_label[11][2].cget("text")+zap_resaults["CRLF Injection"][0],text_color="red")
                                    
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
                        
 #                       self.http=customtkinter.CTkLabel(self.my_frameZap,text="{} \n {}".format(zap_resaults[i][1][j][0],zap_resaults[i][1][j][1]),width=150)

#                        self.http.grid(row=nuumeb, column=1)
                        self.info=customtkinter.CTkTextbox(self.my_frameZap,width=250,height=100,fg_color="transparent")
                        self.info.insert("0.0", "{} \n {}".format(zap_resaults[i][1][j][0],zap_resaults[i][1][j][1]))
                        self.info.grid(row=nuumeb, column=1)
                        self.info.configure(state="disabled")
#                        self.info=customtkinter.CTkLabel(self.my_frameZap,text=zap_resaults[i][2][j],width=150)
                        self.info=customtkinter.CTkTextbox(self.my_frameZap,width=250,height=100,fg_color="transparent")
                        self.info.insert("0.0", zap_resaults[i][2][j])
                        self.info.grid(row=nuumeb, column=2)
                        self.info.configure(state="disabled")

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
                   #self.my_frame.vul_label[0][1].configure(text_color="red",text=int(self.my_frame.vul_label[0][1].cget("text"))+nuclei_resaults[i][0])    
                   self.my_frame.vul_label[0][7].configure(text=self.my_frame.vul_label[0][7].cget("text")+1,text_color="red")
                elif "blind sql" in i.lower():
                   #self.my_frame.vul_label[1][1].configure(text_color="red",text=int(self.my_frame.vul_label[1][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[1][7].configure(text=self.my_frame.vul_label[1][7].cget("text")+1,text_color="red")
                elif "cross"in i.lower() and "site"in i.lower() and "scripting" in i.lower() or "xss" in i.lower():
                   #self.my_frame.vul_label[2][1].configure(text_color="red",text=int(self.my_frame.vul_label[2][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[2][7].configure(text=self.my_frame.vul_label[2][7].cget("text")+1,text_color="red")
                elif "shell" in i.lower():                
                   #self.my_frame.vul_label[3][1].configure(text_color="red",text=int(self.my_frame.vul_label[3][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[3][7].configure(text=self.my_frame.vul_label[3][7].cget("text")+1,text_color="red")
                elif "xml"in i.lower() and "external"in i.lower() and "entity" in i.lower():                
                   #self.my_frame.vul_label[6][1].configure(text_color="red",text=int(self.my_frame.vul_label[6][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[6][7].configure(text=self.my_frame.vul_label[6][7].cget("text")+1,text_color="red")
                elif "xml"in i.lower() and "entity" in i.lower():                
                   #self.my_frame.vul_label[5][1].configure(text_color="red",text=int(self.my_frame.vul_label[5][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[5][7].configure(text=self.my_frame.vul_label[5][7].cget("text")+1,text_color="red")
                elif "code" in i.lower():                
                   #self.my_frame.vul_label[7][1].configure(text_color="red",text=int(self.my_frame.vul_label[7][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[7][7].configure(text=self.my_frame.vul_label[7][7].cget("text")+1,text_color="red")
                elif "command" in i.lower():                
                   #self.my_frame.vul_label[8][1].configure(text_color="red",text=int(self.my_frame.vul_label[8][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[8][7].configure(text=self.my_frame.vul_label[8][7].cget("text")+1,text_color="red")
                elif "html" in i.lower():                
                   #self.my_frame.vul_label[9][1].configure(text_color="red",text=int(self.my_frame.vul_label[9][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[9][7].configure(text=self.my_frame.vul_label[9][7].cget("text")+1,text_color="red")
                elif "crlf" in i.lower():                
                   #self.my_frame.vul_label[11][1].configure(text_color="red",text=int(self.my_frame.vul_label[11][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[11][7].configure(text=self.my_frame.vul_label[11][7].cget("text")+1,text_color="red")
                elif "ognl" in i.lower():                
                   #self.my_frame.vul_label[12][1].configure(text_color="red",text=int(self.my_frame.vul_label[12][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[12][7].configure(text=self.my_frame.vul_label[12][7].cget("text")+1,text_color="red")
                elif "host header" in i.lower():                
                   #self.my_frame.vul_label[13][1].configure(text_color="red",text=int(self.my_frame.vul_label[13][1].cget("text"))+nuclei_resaults[i][0])
                   self.my_frame.vul_label[13][7].configure(text=self.my_frame.vul_label[13][7].cget("text")+1,text_color="red")

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

    def print_meta_Result(self):  
    
#           self.my_frame.vul_label[0][1].configure(text="haho")
           #sqlinjection 0 self.my_frame.vul_label[0][1].cget("text") 
           fileObject = open("weights/weights.json", "r")
           jsonContent = fileObject.read()
           self.weights = json.loads(jsonContent)
           weights = json.loads(jsonContent)
           
           fileObject.close()



           zap,self.templateresult['sql1']=(1,1) if int(self.my_frame.vul_label[0][2].cget("text")) > 0   else (0,0)
           skip,self.templateresult['sql2']=(1,1) if int(self.my_frame.vul_label[0][4].cget("text")) > 0  else (0,0)
           wapiti ,self.templateresult['sql3']=(1,1) if int(self.my_frame.vul_label[0][5].cget("text")) > 0  else (0,0)
           nikto,self.templateresult['sql4']=(1,1) if int(self.my_frame.vul_label[0][6].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['sql5']=(1,1) if int(self.my_frame.vul_label[0][7].cget("text")) > 0 else (0,0)
           formule = ((zap*weights["zap1"])+(skip*weights["skip1"])+(wapiti*weights["wapiti1"])+(nikto*weights["nikto1"])+(nuclei*weights["nuclei1"]) )/2
           if formule >= 0.2 : 
                 self.my_frame.vul_label[0][1].configure(text="Positive",text_color='red')
                 self.templateresult['sql_meta']="Positive"
                 weights["zap1"]=weights["zap1"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
                 weights["skip1"]=weights["skip1"] + ( (skip*(0.01)) + ((skip-1)*(0.002)) )
                 weights["wapiti1"]=weights["wapiti1"] + ( (wapiti*(0.01)) + ((wapiti-1)*(0.002)) )
                 weights["nikto1"]=weights["nikto1"] + ( (nikto*(0.01)) + ((nikto-1)*(0.002)) )
                 weights["nuclei1"]=weights["nuclei1"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )
                 
           else : 
                 self.my_frame.vul_label[0][1].configure(text="Negative",text_color='blue')
                 self.templateresult['sql_meta']="Negative"
           #blindsqlinjection 1 self.my_frame.vul_label[0][1].cget("text") 
           wapiti,self.templateresult['blind3'] =(1,1) if int(self.my_frame.vul_label[1][5].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['blind5']=(1,1) if int(self.my_frame.vul_label[1][7].cget("text")) > 0 else (0,0)
           formule = ((wapiti*weights["wapiti2"])+(nuclei*weights["nuclei2"]) )/1
           if formule >= 0.35 : 
               self.my_frame.vul_label[1][1].configure(text="Positive",text_color='red')
               self.templateresult['blind_meta']="Positive"           
               weights["wapiti2"]=weights["wapiti2"] + ( (wapiti*(0.01)) + ((wapiti-1)*(0.002)) )
               weights["nuclei2"]=weights["nuclei2"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )

           else : 
               self.my_frame.vul_label[1][1].configure(text="Negative",text_color='blue')
               self.templateresult['blind_meta']="Negative"
           #cross site screapt 2 self.my_frame.vul_label[0][1].cget("text") 
           zap,self.templateresult['xss1']=(1,1) if int(self.my_frame.vul_label[2][2].cget("text")) > 0   else (0,0)
           skip,self.templateresult['xss2']=(1,1) if int(self.my_frame.vul_label[2][4].cget("text")) > 0  else (0,0)
           wapiti ,self.templateresult['xss3']=(1,1) if int(self.my_frame.vul_label[2][5].cget("text")) > 0  else (0,0)
           nikto,self.templateresult['xss4']=(1,1) if int(self.my_frame.vul_label[2][6].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['xss5']=(1,1) if int(self.my_frame.vul_label[2][7].cget("text")) > 0 else (0,0)
           formule = ((zap*weights["zap3"])+(skip*weights["skip3"])+(wapiti*weights["wapiti3"])+(nikto*weights["nikto3"])+(nuclei*weights["nuclei3"]) )/2
           if formule >= 0.2 : 
               self.my_frame.vul_label[2][1].configure(text="Positive",text_color='red')
               self.templateresult['xss_meta']="Positive"
               weights["zap3"]=weights["zap3"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
               weights["skip3"]=weights["skip3"] + ( (skip*(0.01)) + ((skip-1)*(0.002)) )
               weights["wapiti3"]=weights["wapiti3"] + ( (wapiti*(0.01)) + ((wapiti-1)*(0.002)) )
               weights["nikto3"]=weights["nikto3"] + ( (nikto*(0.01)) + ((nikto-1)*(0.002)) )
               weights["nuclei3"]=weights["nuclei3"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )

           else : 
               self.my_frame.vul_label[2][1].configure(text="Negative",text_color='blue')
               self.templateresult['xss_meta']="Negative"
           #shell injection 3 self.my_frame.vul_label[0][1].cget("text") 
           skip,self.templateresult['shell2']=(1,1) if int(self.my_frame.vul_label[3][4].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['shell5']=(1,1) if int(self.my_frame.vul_label[3][7].cget("text")) > 0 else (0,0)
           formule = ((skip*weights["skip4"])+(nuclei*weights["nuclei4"]) )/1
           if formule >= 0.5: 
               self.my_frame.vul_label[3][1].configure(text="Positive",text_color='red')
               self.templateresult['shell_meta']="Positive"
               weights["skip4"]=weights["skip4"] + ( (skip*(0.01)) + ((skip-1)*(0.002)) )
               weights["nuclei4"]=weights["nuclei4"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )


           
           else : 
               self.my_frame.vul_label[3][1].configure(text="Negative",text_color='blue')
               self.templateresult['shell_meta']="Negative"

           #XSLT 4 self.my_frame.vul_label[0][1].cget("text") 
           zap,self.templateresult['xslt1']=(1,1) if int(self.my_frame.vul_label[4][2].cget("text")) > 0   else (0,0)
           nikto,self.templateresult['xslt4']=(1,1) if int(self.my_frame.vul_label[4][6].cget("text")) > 0  else (0,0)
           formule = ((zap*weights["zap5"])+(nikto*weights["nikto5"]))/1
           if formule >= 0.5 : 
               self.my_frame.vul_label[4][1].configure(text="Positive",text_color='red')
               self.templateresult['xslt_meta']="Positive"
               weights["zap5"]=weights["zap5"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
               weights["nikto5"]=weights["nikto5"] + ( (nikto*(0.01)) + ((nikto-1)*(0.002)) )

           else : 
               self.my_frame.vul_label[4][1].configure(text="Negative",text_color='blue')
               self.templateresult['xslt_meta']="Negative"

           #xml 5 self.my_frame.vul_label[0][1].cget("text") 
           zap,self.templateresult['xml1']=(1,1) if int(self.my_frame.vul_label[5][2].cget("text")) > 0   else (0,0)
           skip,self.templateresult['xml2']=(1,1) if int(self.my_frame.vul_label[5][4].cget("text")) > 0  else (0,0)
           nikto,self.templateresult['xml4']=(1,1) if int(self.my_frame.vul_label[5][6].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['xml5']=(1,1) if int(self.my_frame.vul_label[5][7].cget("text")) > 0 else (0,0)
           formule = ((zap*weights["zap6"])+(skip*weights["skip6"])+(nikto*weights["nikto6"])+(nuclei*weights["nuclei6"]) )/1.5
           if formule >= 0.26 : 
               self.my_frame.vul_label[5][1].configure(text="Positive",text_color='red')
               self.templateresult['xml_meta']="Positive"
               weights["zap6"]=weights["zap6"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
               weights["skip6"]=weights["skip6"] + ( (skip*(0.01)) + ((skip-1)*(0.002)) )
               weights["nikto6"]=weights["nikto6"] + ( (nikto*(0.01)) + ((nikto-1)*(0.002)) )
               weights["nuclei6"]=weights["nuclei6"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )

           else : 
               self.my_frame.vul_label[5][1].configure(text="Negative",text_color='blue')
               self.templateresult['xml_meta']="Negative"

           #XXE 6 self.my_frame.vul_label[0][1].cget("text") 
           zap,self.templateresult['xxe1']=(1,1) if int(self.my_frame.vul_label[6][2].cget("text")) > 0   else (0,0)
           wapiti,self.templateresult['xxe3'] =(1,1) if int(self.my_frame.vul_label[6][5].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['xxe5']=(1,1) if int(self.my_frame.vul_label[6][7].cget("text")) > 0 else (0,0)
           formule = ((zap*weights["zap7"])+(wapiti*weights["wapiti7"])+(nuclei*weights["nuclei7"]) )/1.5
           if formule >= 0.33 : 
                self.my_frame.vul_label[6][1].configure(text="Positive",text_color='red')
                self.templateresult['xxe_meta']="True"
                weights["zap7"]=weights["zap7"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
                weights["wapiti7"]=weights["wapiti7"] + ( (wapiti*(0.01)) + ((wapiti-1)*(0.002)) )
                weights["nuclei7"]=weights["nuclei7"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )
           else : 
                self.my_frame.vul_label[6][1].configure(text="Negative",text_color='blue')
                self.templateresult['xxe_meta']="Negative"

           #code 7 self.my_frame.vul_label[0][1].cget("text") 
           zap,self.templateresult['code1']=(1,1) if int(self.my_frame.vul_label[7][2].cget("text")) > 0   else (0,0)
           nikto,self.templateresult['code4']=(1,1) if int(self.my_frame.vul_label[7][6].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['code5']=(1,1) if int(self.my_frame.vul_label[7][7].cget("text")) > 0 else (0,0)
           formule = ((zap*weights["zap8"])+(nikto*weights["nikto8"])+(nuclei*weights["nuclei8"]) )/1.5
           if formule >= 0.3 : 
               self.my_frame.vul_label[7][1].configure(text="Positive",text_color='red')
               self.templateresult['code_meta']="Positive"
               weights["zap8"]=weights["zap8"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
               weights["nikto8"]=weights["nikto8"] + ( (nikto*(0.01)) + ((nikto-1)*(0.002)) )
               weights["nuclei8"]=weights["nuclei8"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )
           else :
               self.my_frame.vul_label[7][1].configure(text="Negative",text_color='blue')
               self.templateresult['code_meta']="Negative"

           #os comand 8 self.my_frame.vul_label[0][1].cget("text") 
           zap,self.templateresult['os1']=(1,1) if int(self.my_frame.vul_label[8][2].cget("text")) > 0   else (0,0)
           wapiti,self.templateresult['os3'] =(1,1) if int(self.my_frame.vul_label[8][5].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['os5']=(1,1) if int(self.my_frame.vul_label[8][7].cget("text")) > 0 else (0,0)
           formule = ((zap*weights["zap9"])+(wapiti*weights["wapiti9"])+(nuclei*weights["nuclei9"]) )/1.5
           if formule >= 0.33 : 
               self.my_frame.vul_label[8][1].configure(text="Positive",text_color='red')
               self.templateresult['os_meta']="Positive"
               weights["zap9"]=weights["zap9"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
               weights["wapiti9"]=weights["wapiti9"] + ( (wapiti*(0.01)) + ((wapiti-1)*(0.002)) )
               weights["nuclei9"]=weights["nuclei9"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )
           else : 
               self.my_frame.vul_label[8][1].configure(text="Negative",text_color='blue')
               self.templateresult['os_meta']="Negative"

           #html 9 self.my_frame.vul_label[0][1].cget("text") 
           nikto,self.templateresult['html4']=(1,1) if int(self.my_frame.vul_label[9][6].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['html5']=(1,1) if int(self.my_frame.vul_label[9][7].cget("text")) > 0 else (0,0)
           formule = ((nikto*weights["nikto10"])+(nuclei*weights["nuclei10"]) )/1
           if formule >= 0.5 : 
               self.my_frame.vul_label[9][1].configure(text="Positive",text_color='red')
               self.templateresult['html_meta']="Positive"
               weights["nikto10"]=weights["nikto10"] + ( (nikto*(0.01)) + ((nikto-1)*(0.002)) )
               weights["nuclei10"]=weights["nuclei10"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )
           else : 
               self.my_frame.vul_label[9][1].configure(text="Negative",text_color='blue')
               self.templateresult['html_meta']="Negative"

           #template 10 self.my_frame.vul_label[0][1].cget("text") 
           zap,self.templateresult['template1']=(1,1) if int(self.my_frame.vul_label[10][2].cget("text")) > 0   else (0,0)
           formule =zap*weights["zap11"]
           if formule == 1 : 
               self.my_frame.vul_label[10][1].configure(text="Positive",text_color='red')
               self.templateresult['template_meta']="Positive"
               weights["zap"]=weights["zap"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
           else : 
               self.my_frame.vul_label[10][1].configure(text="Negative",text_color='blue')
               self.templateresult['template_meta']="Negative"

           #crlf 11 self.my_frame.vul_label[0][1].cget("text") 
           zap,self.templateresult['crlf1']=(1,1) if int(self.my_frame.vul_label[11][2].cget("text")) > 0   else (0,0)
           skip,self.templateresult['crlf2']=(1,1) if int(self.my_frame.vul_label[11][4].cget("text")) > 0  else (0,0)
           wapiti,self.templateresult['crlf3'] =(1,1) if int(self.my_frame.vul_label[11][5].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['crlf5']=(1,1) if int(self.my_frame.vul_label[11][7].cget("text")) > 0 else (0,0)
           formule = ((zap*weights["zap12"])+(skip*weights["skip12"])+(wapiti*weights["wapiti12"])+(nuclei*weights["nuclei12"]) )/2
           if formule >= 0.2 : 
               self.my_frame.vul_label[11][1].configure(text="Positive",text_color='red')
               self.templateresult['crlf_meta']="Positive"
               weights["zap12"]=weights["zap12"] + ( (zap*(0.01)) + ((zap-1)*(0.002)) )
               weights["skip12"]=weights["skip12"] + ( (skip*(0.01)) + ((skip-1)*(0.002)) )
               weights["wapiti12"]=weights["wapiti12"] + ( (wapiti*(0.01)) + ((wapiti-1)*(0.002)) )
               weights["nuclei12"]=weights["nuclei12"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )
               
           else : 
               self.my_frame.vul_label[11][1].configure(text="Negative",text_color='blue')
               self.templateresult['crlf_meta']="Negative"

           #OGNL 12 self.my_frame.vul_label[0][1].cget("text") 
           skip,self.templateresult['ognl2']=(1,1) if int(self.my_frame.vul_label[12][4].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['ognl5']=(1,1) if int(self.my_frame.vul_label[12][7].cget("text")) > 0 else (0,0)
           formule = ((skip*weights["skip13"])+(nuclei*weights["nuclei13"]) )/1
           if formule == 1 : 
               self.my_frame.vul_label[12][1].configure(text="Positive",text_color='red')
               self.templateresult['ognl_meta']="Positive"
               weights["skip13"]=weights["skip13"] + ( (skip*(0.01)) + ((skip-1)*(0.002)) )
               weights["nuclei13"]=weights["nuclei13"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )
           else : 
               self.my_frame.vul_label[12][1].configure(text="Negative",text_color='blue')
               self.templateresult['ognl_meta']="Negative"

           #host head 13 self.my_frame.vul_label[0][1].cget("text") 
           skip,self.templateresult['host2']=(1,1) if int(self.my_frame.vul_label[13][4].cget("text")) > 0  else (0,0)
           nuclei,self.templateresult['host5']=(1,1) if int(self.my_frame.vul_label[13][7].cget("text")) > 0 else (0,0)
           formule = ((skip*weights["skip14"])+(nuclei*weights["nuclei14"]) )/1
           if formule ==1 : 
                self.my_frame.vul_label[13][1].configure(text="Positive",text_color='red')
                self.templateresult['host_meta']="Positive"
                weights["skip14"]=weights["skip14"] + ( (skip*(0.01)) + ((skip-1)*(0.002)) )
                weights["nuclei14"]=weights["nuclei14"] + ( (nuclei*(0.01)) + ((nuclei-1)*(0.002)) )
           else : 
                self.my_frame.vul_label[13][1].configure(text="Negative",text_color='blue')
                self.templateresult['host_meta']="Negative"
           self.weights = weights
           fileObject = open("weights/weights.json", "w")
           fileObject.write(json.dumps(weights))
           fileObject.close()

           #print(self.templateresult)
#           1
#           2
#           3
#           4
#           5
#           6
#           7
#           8
#           9
#           10
#           11
#           12
#           13
#           14
           


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
        #print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        if new_appearance_mode=="Light":
                self.menubar.config(bg='#4d4d4d', fg='white', activebackground='white', activeforeground='#2d2d2d', borderwidth=0, relief='flat', font=('Arial', 12))
                self.file_menu.config(bg='#4d4d4d', fg='white', activebackground='white', activeforeground='#2d2d2d', borderwidth=0, relief='flat', font=('Arial', 12))
                self.modes_menu.config(bg='#4d4d4d', fg='white', activebackground='white', activeforeground='#2d2d2d', borderwidth=0, relief='flat', font=('Arial', 12))
                #self.target_menu.config(bg='#4d4d4d', fg='white', activebackground='white', activeforeground='#2d2d2d', borderwidth=0, relief='flat', font=('Arial', 12))
                
        else:
                self.menubar.config(bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
                self.file_menu.config(bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
                self.modes_menu.config(bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))
                #self.target_menu.config(bg='lightblue', fg='#2d2d2d', activebackground='#4d4d4d', activeforeground='white', borderwidth=0, relief='flat', font=('Arial', 12))

        
        customtkinter.set_appearance_mode(new_appearance_mode)
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def save_as_html(self):
         env = Environment(loader=FileSystemLoader('.'))
         template = env.get_template('result_template/template.html')
         output = template.render(self.templateresult)
         directory = filedialog.askdirectory()   
         directory_path = os.path.join(directory, self.templateresult['target_name'])
         os.mkdir(directory_path)
         
         with open('{}/{}/{}.html'.format(directory,self.templateresult['target_name'],self.templateresult['target_name']), 'w') as f:
               f.write(output)

         shutil.copy("/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/result_template/meta1.png", '{}/{}/'.format(directory,self.templateresult['target_name']))

         webbrowser.open('{}/{}/{}.html'.format(directory,self.templateresult['target_name'],self.templateresult['target_name']), new=2)




    def Load_resaults(self,name):
#        for i in self.my_frame.vul_label:
#            i[1].configure(text=int(0))

        self.log_textbox.insert(tkinter.END, "\n[Results]:", tags="yellow")            
        self.log_textbox.insert(tkinter.END, "Check The Results of :", tags=None) 
        self.log_textbox.insert(tkinter.END, "\n------", tags="red")            
        self.log_textbox.insert(tkinter.END, "{}".format(name), tags=None) 
        self.log_textbox.insert(tkinter.END, " ------", tags="red")            

        self.destroyResaults()
        self.templateresult['target_name']=name      
        self.print_wapiti_Result(name)
        self.print_skipfich_Result(name) 
        self.print_Nikto_Result(name)
        self.print_zap_Result(name)
        self.print_nuclei_Result(name)
        self.print_meta_Result()
    def Open_skipfish_site(self,name):
        webbrowser.open('/home/ostesayed/Desktop/Scanners/OSTE-Scanner/OSTEscaner/Resaults/{}/skipfish/{}/index.html'.format(name,name), new=2)
    def show_graph(self,name,x1,x2,x3,x4,x5):    
        x = ["ZAP", "SkipFish", "Wapiti", "Nikto","Nuclei"]
        y = [x1, x2, x3,x4, x5]
        colors = ['red', 'green', 'blue', 'orange', 'purple']
        bar(x,y,color=colors)
        ylim(0, 1)
        title("Scanner Weights for {}".format(name))
        show()

        
        
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
        self.label = customtkinter.CTkLabel(self,text="CWE-code:Vulnerability",width=200,anchor="w")

        self.label.grid(row=0, column=0,padx=3,pady=3)
        self.label1 = customtkinter.CTkLabel(self,text="Meta-Scan",width=50,anchor="w",text_color=("green","LightGreen"))
        self.label1.grid(row=0, column=6,padx=3,pady=3)
        
        self.label2 = customtkinter.CTkLabel(self,text="OWASP",width=50)
        self.label2.grid(row=0, column=1,padx=0,pady=0)
        self.label3 = customtkinter.CTkLabel(self,text="Skipfish",width=50)
        self.label3.grid(row=0, column=2,padx=0,pady=3)
        self.label4 = customtkinter.CTkLabel(self,text="Wapiti",width=50)
        self.label4.grid(row=0, column=3,padx=0,pady=3)
        self.label5 = customtkinter.CTkLabel(self,text="Nikto",width=50)
        self.label5.grid(row=0, column=4,padx=0,pady=3)
        self.label6 = customtkinter.CTkLabel(self,text="Nuclei",width=50)
        self.label6.grid(row=0, column=5,padx=0,pady=3)
        
        self.label7 = customtkinter.CTkLabel(self,text="Details")
        self.label7.grid(row=0, column=7,padx=3,pady=3,sticky="e")    
        self.vul_label=[]
        info=customtkinter.CTkImage(light_image=Image.open("images/info.png"),dark_image=Image.open("images/info.png"),size=(30, 30))
        graph=customtkinter.CTkImage(light_image=Image.open("images/bar-graph.png"),dark_image=Image.open("images/bar-graph.png"),size=(30, 30))
       
        xer="______________________________________________________________________________________________________________________________________________________"
        for i in range(14):
            temp=[]
            self.labeltemp=customtkinter.CTkLabel(self,text=xer,fg_color="transparent")
            self.labeltemp.grid(row=i+1, column=0,columnspan=8,pady=(40,0))

            self.labeltemp=customtkinter.CTkLabel(self,text=" injection:",width=200,fg_color="transparent",anchor="w")
            self.labeltemp.grid(row=i+1, column=0,padx=0,pady=3)
            self.labeltemp1=customtkinter.CTkLabel(self,text="P/N",width=50,fg_color="transparent",text_color=("green","LightGreen"))
            self.labeltemp1.grid(row=i+1, column=6,padx=0,pady=3)
            self.labeltemp2=customtkinter.CTkLabel(self,text=int(0),width=50,fg_color="transparent")
            self.labeltemp2.grid(row=i+1, column=1,padx=0,pady=3)
            self.labeltemp3=customtkinter.CTkLabel(self,text=int(0),width=50,fg_color="transparent")
            self.labeltemp3.grid(row=i+1, column=2,padx=0,pady=3)
            self.labeltemp4=customtkinter.CTkLabel(self,text=int(0),width=50,fg_color="transparent")
            self.labeltemp4.grid(row=i+1, column=3,padx=0,pady=3)
            self.labeltemp5=customtkinter.CTkLabel(self,text=int(0),width=50,fg_color="transparent")
            self.labeltemp5.grid(row=i+1, column=4,padx=0,pady=3)
            self.labeltemp6=customtkinter.CTkLabel(self,text=int(0),width=50,fg_color="transparent")
            self.labeltemp6.grid(row=i+1, column=5,padx=0,pady=3)
            
            self.new=customtkinter.CTkFrame(self,fg_color="transparent")
            self.new.grid(row=i+1, column=7,padx=3,pady=(5,30),sticky="e")
            
            self.grp=customtkinter.CTkButton(self.new,text="",image=graph,width=40 , height=40,fg_color="transparent")#,state="disabled"  ki tkml raj3ha
            self.grp.pack(side="left")
            self.but=customtkinter.CTkButton(self.new,text="",image=info,width=40 , height=40,fg_color="transparent")#,state="disabled"  ki tkml raj3ha
            self.but.pack(side="left")

            self.vul_label.append([self.labeltemp,self.labeltemp1,self.labeltemp2,self.but,self.labeltemp3,self.labeltemp4,self.labeltemp5,self.labeltemp6,self.grp])

        self.vul_label[0][0].configure(text="CWE-89:SQL injection")
        self.vul_label[0][3].configure(command=lambda:app.open_check("SQL Injection"))
        self.vul_label[0][8].configure(command=lambda:app.show_graph("SQL Injection",app.weights["zap1"],app.weights["skip1"],app.weights["wapiti1"],app.weights["nikto1"],app.weights["nuclei1"]))
        
        self.vul_label[1][0].configure(text="CWE-89:Blind SQL injection")
        self.vul_label[1][3].configure(command=lambda:app.open_check("Blind SQL injection"))
        self.vul_label[1][8].configure(command=lambda:app.show_graph("BlindSQL Injection",0,0,app.weights["wapiti2"],0,app.weights["nuclei2"]))
        
        self.vul_label[2][0].configure(text="CWE-79:Cross Site Scripting injection")
        self.vul_label[2][3].configure(command=lambda:app.open_check("Cross Site Scripting injection"))
        self.vul_label[2][8].configure(command=lambda:app.show_graph("Cross Site Scripting Injection",app.weights["zap3"],app.weights["skip3"],app.weights["wapiti3"],app.weights["nikto3"],app.weights["nuclei3"]))
        
        self.vul_label[3][0].configure(text="CWE-553:Shell injection")
        self.vul_label[3][3].configure(command=lambda:app.open_check("Shell injection"))
        self.vul_label[3][8].configure(command=lambda:app.show_graph("Shell Injection",0,app.weights["skip4"],0,0,app.weights["nuclei4"]))

        self.vul_label[4][0].configure(text="CVE-2006-4686:XSLT injection")
        self.vul_label[4][3].configure(command=lambda:app.open_check("XSLT injection"))
        self.vul_label[4][8].configure(command=lambda:app.show_graph("XSLT Injection",app.weights["zap5"],0,0,app.weights["nikto5"],0))

        self.vul_label[5][0].configure(text="CWE-91:XML injection")
        self.vul_label[5][3].configure(command=lambda:app.open_check("XML injection"))
        self.vul_label[5][8].configure(command=lambda:app.show_graph("XML Injection",app.weights["zap6"],app.weights["skip6"],0,app.weights["nikto6"],app.weights["nuclei6"]))

        self.vul_label[6][0].configure(text="CWE-611:XML external entities")
        self.vul_label[6][3].configure(command=lambda:app.open_check("XML external entities (XXE)"))
        self.vul_label[6][8].configure(command=lambda:app.show_graph("XML external entities (XXE)",app.weights["zap7"],0,app.weights["wapiti7"],0,app.weights["nuclei7"]))

        self.vul_label[7][0].configure(text="CWE-94:code injection")
        self.vul_label[7][3].configure(command=lambda:app.open_check("code injection"))
        self.vul_label[7][8].configure(command=lambda:app.show_graph("code Injection",app.weights["zap8"],0,0,app.weights["nikto8"],app.weights["nuclei8"]))

        self.vul_label[8][0].configure(text="CWE-78:OS command injection")
        self.vul_label[8][3].configure(command=lambda:app.open_check("OS command injection"))
        self.vul_label[8][8].configure(command=lambda:app.show_graph("os command Injection",app.weights["zap9"],0,app.weights["wapiti9"],0,app.weights["nuclei9"]))

        self.vul_label[9][0].configure(text="CWE-80:html injection")
        self.vul_label[9][3].configure(command=lambda:app.open_check("html injection"))
        self.vul_label[9][8].configure(command=lambda:app.show_graph("html Injection",0,0,0,app.weights["nikto10"],app.weights["nuclei10"]))

        self.vul_label[10][0].configure(text="CWE-1336:Template injection")
        self.vul_label[10][3].configure(command=lambda:app.open_check("Template injection"))
        self.vul_label[10][8].configure(command=lambda:app.show_graph("Template Injection",app.weights["zap11"],0,0,0,0))

        self.vul_label[11][0].configure(text="CWE-93:CRLF injection")
        self.vul_label[11][3].configure(command=lambda:app.open_check("CRLF injection"))
        self.vul_label[11][8].configure(command=lambda:app.show_graph("CRLF Injection",app.weights["zap12"],app.weights["skip12"],app.weights["wapiti12"],0,app.weights["nuclei12"]))

        self.vul_label[12][0].configure(text="CWE-1003:OGNL injection")
        self.vul_label[12][3].configure(command=lambda:app.open_check("OGNL injection"))
        self.vul_label[12][8].configure(command=lambda:app.show_graph("OGNL Injection",0,app.weights["skip13"],0,0,app.weights["nuclei13"]))

        self.vul_label[13][0].configure(text="CWE-644:Host Header injection")
        self.vul_label[13][3].configure(command=lambda:app.open_check("Host Header injection"))
        self.vul_label[13][8].configure(command=lambda:app.show_graph("Host Header Injection",0,app.weights["skip14"],0,0,app.weights["nuclei14"]))
        
if __name__ == "__main__":
    app = App()
#    app.iconbitmap("images/meta.ico")        #configure the menu:

    app.mainloop()
