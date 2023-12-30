import tkinter as tk
from PIL import Image, ImageTk

def on_entry_click(event, default_text):
    """Function to clear sample text when user clicks."""
    if event.widget.get() == default_text:
        event.widget.delete(0, "end")
        event.widget.config(fg='black')

def on_focusout(event, default_text):
    """Function to redisplay sample text if there is no input."""
    if not event.widget.get():
        event.widget.insert(0, default_text)
        event.widget.config(fg='grey')
        
class InformationPaperView():
    def __init__(self, controller, window):
        self.controller = controller
        self.window = window
        self.configure_window()
        self.content()
        
    def configure_window(self):
        self.window.title("Información del Paper")
        self.window.configure(bg="#263D42")
        self.window.geometry('500x500') 
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.controller.on_close)

    def content(self):
        # Load and display image
        route_image = "./assets/images/UploadPaper-interfaz.png"
        original_image = Image.open(route_image)
        resized_image = original_image.resize((200, 120)) 
        image = ImageTk.PhotoImage(resized_image)

        label_image = tk.Label(self.window, image=image, bg="#263D42")
        label_image.image = image  
        label_image.pack(pady=(20, 0))

        # Intro text
        description = tk.Label(self.window, text="Ingrese los siguientes datos.",
                               bg="#263D42", fg="#A7BEBE",
                               font=("Arial", 12, "bold"))
        description.pack(pady=(20, 20))

      
        # Create and organize input fields
        self.title = self.create_labeled_entry("Nombre del Paper:", "Escriba el nombre del paper", pady=(10,10), entry_width=50)
        self.author = self.create_labeled_entry("Autores:", "Escriba los autores", pady=(10,10), entry_width=50)
        self.date = self.create_labeled_entry("Fecha de Publicación:", "DD/MM/AAAA", pady=(10,20), entry_width=50)


        # Button to close the window
        close_button = tk.Button(self.window, text="Continuar",
                                 command=lambda: self.controller.create_paper(self.title.get(), self.author.get(), self.date.get()),
                                 font=("Arial", 10), bg="#A7BEBE")
        close_button.pack(pady=10)

    def create_labeled_entry(self, label_text, default_text, pady=(10, 0), entry_width=30):
        label = tk.Label(self.window, text=label_text, bg="#263D42", fg="white", font=("Arial", 10))
        label.pack(pady=(pady[0], 0))

        entry = tk.Entry(self.window, fg='grey', font=("Arial", 10), width=entry_width, highlightthickness=2, highlightcolor="#A7BEBE")
        entry.insert(0, default_text)
        entry.bind("<FocusIn>", lambda event, default_text=default_text: on_entry_click(event, default_text))
        entry.bind("<FocusOut>", lambda event, default_text=default_text: on_focusout(event, default_text))
        entry.pack(pady=(0, pady[1]))

        return entry  
        
