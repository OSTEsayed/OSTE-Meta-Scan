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
            app.log_textbox.insert(tkinter.END, "\n [INFO] 		OWASPZAP Scanning started", tags=None)            
            starting_zap= threading.Thread(target=new_scan.check_for_zap)
            starting_zap.start()
            app.log_textbox.insert(tkinter.END, "\n [INFO] 		NIKTO Scanning started", tags=None)            
            starting_nikto = threading.Thread(target=new_scan.start_nikto)
            starting_nikto.start() 
            app.log_textbox.insert(tkinter.END, "\n [INFO] 		Nuclei Scanning started", tags=None)            
            starting_nuclei = threading.Thread(target=new_scan.start_nuclei)
            starting_nuclei.start() 

            CHECKER = threading.Thread(target=self.check_for_finished,args=(starting_zap,starting_nikto,starting_nuclei,starting_wapiti,starting_skipfish))
            CHECKER.start() 

#            new_scan.starting_all_scanner(self.target_name.get(),self.target_url.get())
    def check_for_finished(self,a,b,c,d,e):
                zap_statu,nikto_statu,nuclei_statu,wapiti_statu,skipfish_statu="scanning","scanning","scanning","scanning","scanning"
                number_scaner=5
                time.sleep(5)
                self.destroy()
                while number_scaner>0:
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
                  time.sleep(5)
    
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
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text="Load old Results")
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
        self.label_1 = customtkinter.CTkLabel(self.results_tabview.tab("Our Resault"),text="Resault Table:", justify=customtkinter.CENTER)
        self.label_1.pack(pady=0, padx=0)
        
        
        self.my_frame = MyFrame(master=self.results_tabview.tab("Our Resault"))
        self.my_frame.pack(fill="both",padx=0,pady=0,expand=True)        
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

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self,text="Vulnerability",width=250)
        self.label.grid(row=0, column=0)
        self.label1 = customtkinter.CTkLabel(self,text="Exist",width=50)
        self.label1.grid(row=0, column=1)
        self.label2 = customtkinter.CTkLabel(self,text="Scanners",width=150)
        self.label2.grid(row=0, column=2)
        self.label3 = customtkinter.CTkLabel(self,text="Action",width=150)
        self.label3.grid(row=0, column=3,sticky="N")    

if __name__ == "__main__":
    app = App()
    app.mainloop()
