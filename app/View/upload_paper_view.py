import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


class UploadPaperView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.configure_window()
        self.content()

    def show_error(self, error_message):
        messagebox.showerror("Error", error_message)

    def configure_window(self):
        self.window.title("PaperGraph")
        self.window.configure(bg="#263D42")
        self.window.geometry("600x500") 
        self.window.resizable(False, False)
        
        # Add logo to window        
        route_logo = "./assets/images/logo2.png"  
        logo = Image.open(route_logo)
        logo_tk = ImageTk.PhotoImage(logo)
        self.window.iconphoto(True, logo_tk)

        # Kill window 
        self.window.protocol("WM_DELETE_WINDOW", self.controller.on_close)


    def content(self):
        # Image
        route_image = "./assets/images/UploadPaper-interfaz.png"
        original_image = Image.open(route_image)
        resized_image = original_image.resize((500, 300)) 
        image = ImageTk.PhotoImage(resized_image)

        label_image = tk.Label(self.window, image=image, bg="#263D42")
        label_image.image = image  
        label_image.pack(pady=(20, 0))

        # Header Text
        title = tk.Label(self.window, text="¡Dale sentido a los papers!", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 24, "bold"))
        title.pack(pady=(10, 10))

        # Text
        description = tk.Label(self.window, 
                                text="PaperGraph analiza automáticamente un artículo académico, inspeccionando sus referencias y contribuciones para generar un gráfico visual a partir de esta información.", 
                                bg="#263D42", 
                                fg="#A7BEBE", 
                                wraplength=500, 
                                justify="center")
        description.pack(pady=(0, 20))

        # Button to upload PDF
        self.upload_button = tk.Button(self.window, text="Subir Paper", command=self.upload_file, bg="#4A6572", fg="#FFFFFF", font=("Helvetica", 16), borderwidth=0)
        self.upload_button.pack(pady=(0, 20))

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")]
        )
        self.controller.file_selection(file_path)