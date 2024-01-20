import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def on_entry_click(event, default_text):
    if event.widget.get() == default_text:
        event.widget.delete(0, "end")
        event.widget.config(fg='black')

def on_focusout(event, default_text):
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
        route_image = "./assets/images/UploadPaper-interfaz.png"
        original_image = Image.open(route_image)
        resized_image = original_image.resize((200, 120)) 
        image = ImageTk.PhotoImage(resized_image)

        label_image = tk.Label(self.window, image=image, bg="#263D42")
        label_image.image = image  
        label_image.pack(pady=(20, 0))

        description = tk.Label(self.window, text="Ingrese los siguientes datos.",
                               bg="#263D42", fg="#A7BEBE",
                               font=("Arial", 12, "bold"))
        description.pack(pady=(20, 20))

        self.title = self.create_labeled_entry("Nombre del Paper:", "Escriba el nombre del paper", pady=(10,10), entry_width=50, validate_function=self.validate_paper_name)
        self.author = self.create_labeled_entry("Autores:", "Escriba los autores", pady=(10,10), entry_width=50, validate_function=self.validate_authors)
        self.date = self.create_labeled_entry("Fecha de Publicación:", "DD/MM/AAAA", pady=(10,20), entry_width=50, validate_function=self.validate_date)

        close_button = tk.Button(self.window, text="Continuar",
                                 command=self.try_to_continue,
                                 font=("Arial", 10), bg="#A7BEBE")
        close_button.pack(pady=10)

    def create_labeled_entry(self, label_text, default_text, pady=(10, 0), entry_width=30, validate_function=None):
        label = tk.Label(self.window, text=label_text, bg="#263D42", fg="white", font=("Arial", 10))
        label.pack(pady=(pady[0], 0))

        entry = tk.Entry(self.window, fg='grey', font=("Arial", 10), width=entry_width, highlightthickness=2, highlightcolor="#A7BEBE")
        entry.insert(0, default_text)
        entry.bind("<FocusIn>", lambda event, default_text=default_text: on_entry_click(event, default_text))
        entry.bind("<FocusOut>", lambda event, default_text=default_text: on_focusout(event, default_text))
        entry.pack(pady=(0, pady[1]))

        if validate_function:
            entry.bind("<FocusOut>", lambda event, validate_function=validate_function: self.on_focusout_with_validation(event, validate_function))

        return entry

    def on_focusout_with_validation(self, event, validate_function):
        input_text = event.widget.get()
        if not validate_function(input_text):
            event.widget.config(fg='red')
        else:
            event.widget.config(fg='black')

    def try_to_continue(self):
        title_value = self.title.get()
        author_value = self.author.get()
        date_value = self.date.get()

        error_messages = []

        if not self.validate_paper_name(title_value):
            error_messages.append("Nombre del paper debe tener menos de 100 caracteres.")

        if not self.validate_authors(author_value):
            error_messages.append("Lista de autores debe tener menos de 100 caracteres.")

        if not self.validate_date(date_value):
            error_messages.append("Formato de fecha incorrecto. Debe ser DD/MM/AAAA.")

        if error_messages:
            error_message = "\n".join(error_messages)
            messagebox.showerror("Error de Validación", f"Por favor, corrija lo siguiente:\n\n{error_message}")
        else:
            self.controller.create_paper(title_value, author_value, date_value)

    def validate_paper_name(self, value):
        return len(value) <= 100

    def validate_authors(self, value):
        return len(value) <= 100

    def validate_date(self, value):
        try:
            day, month, year = map(int, value.split('/'))
            if 1 <= day <= 31 and 1 <= month <= 12:
                return True
        except ValueError:
            pass

        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = InformationPaperView(None, root)
    root.mainloop()