import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from .menu_frame import MenuFrame
from .graph_frame import GraphFrame

class AplicationView:
    def __init__(self, controller):
        self.controller = controller
        self.ventana = tk.Tk()
        self.configure_window()
        self.left_content()
        self.right_content()

    def show_error(self, error_message):
        messagebox.showerror("Error", error_message)
    
    def configure_window(self):
        self.ventana.title("PaperGraph")
        self.ventana.configure(bg="#263D42")
        self.ventana.geometry("1200x700") 
        self.ventana.resizable(True, True)

        # Add logo to window        
        ruta_logo = "./assets/images/logo2.png"  
        logo = Image.open(ruta_logo)
        logo_tk = ImageTk.PhotoImage(logo)
        self.ventana.iconphoto(True, logo_tk)

        self.ventana.protocol("WM_DELETE_WINDOW", self.controller.on_close)
        

    def left_content(self):
        self.graph_frame = GraphFrame(self.ventana, self.controller, bg_color="#A7BEBE")
        # Coloca el graph_frame en la primera columna, y se expande en ambas direcciones
        self.graph_frame.grid(row=0, column=0, sticky="nsew")

    def right_content(self):
        self.menu_frame = MenuFrame(self.ventana, self.controller)
        # Coloca el menu_frame en la segunda columna, ocupando toda la altura
        self.menu_frame.grid(row=0, column=1, sticky="ns")

        # Configura el contenedor para que la segunda columna se expanda con la ventana
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(0, weight=1)
    
    
