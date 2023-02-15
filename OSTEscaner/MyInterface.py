import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
"""class Second_start_scan(customtkinter.CTk):
   def __init__(self):
        super().__init__()

        # configure window
        self.title("new Scan")
        self.geometry(f"{500}x{350}")
   """
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x350")

        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20,padx=60,fill ="both",expand=True)
        self.label = customtkinter.CTkLabel(self.frame, text="Start The New Scan")
        self.label.pack(padx=20, pady=20)


        self.entry1=customtkinter.CTkEntry(self.frame,placeholder_text="Name of target")
        self.entry1.pack(pady=12,padx=10)

        self.entry1=customtkinter.CTkEntry(self.frame,placeholder_text="URL of target: (http://....)")
        self.entry1.pack(pady=12,padx=10)
        self.butto=customtkinter.CTkButton(self.frame, text="Start Scanning",command=print("fuckyes:"))
        self.butto.pack(pady=12,padx=20)

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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_toplevel,text="Start New Scan")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text="Load old Results")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text="check Scanners")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.toplevel_window = None
        
        
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()
            
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


if __name__ == "__main__":
    app = App()
    app.mainloop()
