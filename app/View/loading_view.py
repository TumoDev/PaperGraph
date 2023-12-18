import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class LoadingView():
    def __init__(self, controller):
        self.controller = controller
        self.ventana = tk.Tk()
        self.configure_window()
        self.content()

    def configure_window(self):
        self.ventana.title('Cargando Procesos')
        self.ventana.configure(bg="#263D42")
        self.ventana.geometry('300x100') 
        self.ventana.resizable(False, False)

        # Add logo to window        
        ruta_logo = "./assets/images/logo2.png"  
        logo = Image.open(ruta_logo)
        logo_tk = ImageTk.PhotoImage(logo)
        self.ventana.iconphoto(True, logo_tk)

        self.ventana.protocol("WM_DELETE_WINDOW", self.controller.on_close)

    def show_error(self, error_message):
        messagebox.showerror("Error", error_message)

    def content(self):
        # Barra de progreso
        self.progress = ttk.Progressbar(self.ventana, orient="horizontal", length=200, mode='determinate')
        self.progress.pack(pady=20)

        # Texto de estado
        self.status_label = tk.Label(self.ventana, text="Iniciando...", bg="#263D42", fg="#FFFFFF")
        self.status_label.pack()

    def update_progress(self, value, text):
        self.progress['value'] = value
        self.status_label.config(text=text)
        self.ventana.update_idletasks()  # Actualiza la interfaz gráfica

    

    