import tkinter as tk
from tkinter import messagebox, Canvas, Scrollbar, Frame
from PIL import Image, ImageTk
from .menu_frame import MenuFrame
from .graph_frame import GraphFrame

class AplicationView:
    def __init__(self, controller):
        self.controller = controller
        self.ventana = tk.Tk()
        self.configure_window()
        self.content()

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


    def content(self):
        # Create the frame container for GraphFrame and MenuFrame        
        frames_container = Frame(self.ventana)
        frames_container.pack(fill="both", expand=True)

        # Set the weight of columns in frames_container
        frames_container.grid_columnconfigure(0, weight=95)  
        frames_container.grid_columnconfigure(1, weight=5)
        frames_container.grid_rowconfigure(0, weight=1)

        # Add the GraphFrame and MenuFrame directly to the frames_container
        self.graph_frame = GraphFrame(frames_container, self.controller, bg_color="#A7BEBE")
        self.graph_frame.grid(row=0, column=0, sticky="nsew")
        self.menu_frame = MenuFrame(frames_container, self.controller)
        self.menu_frame.grid(row=0, column=1, sticky="nsew")

      