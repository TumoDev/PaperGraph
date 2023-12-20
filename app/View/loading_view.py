import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class LoadingView():
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.configure_window()
        self.content()

    def configure_window(self):
        self.window.title('Cargando Procesos')
        self.window.configure(bg="#263D42")
        self.window.geometry('300x100') 
        self.window.resizable(False, False)

        # Add logo to window        
        route_logo = "./assets/images/logo2.png"  
        logo = Image.open(route_logo)
        logo_tk = ImageTk.PhotoImage(logo)
        self.window.iconphoto(True, logo_tk)

        self.window.protocol("WM_DELETE_WINDOW", self.controller.on_close)

    def show_error(self, error_message):
        messagebox.showerror("Error", error_message)

    def content(self):
        # Progress bar
        self.progress = ttk.Progressbar(self.window, orient="horizontal", length=200, mode='determinate')
        self.progress.pack(pady=20)

        # Status text
        self.status_label = tk.Label(self.window, text="Iniciando...", bg="#263D42", fg="#FFFFFF")
        self.status_label.pack()

    def update_progress(self, value, text):
        self.progress['value'] = value
        self.status_label.config(text=text)
        self.window.update_idletasks() 

    

    