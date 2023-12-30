import sys
from app.View import LoadingView
import tkinter as tk

class LoadingController:
    def __init__(self, model):
        self.model= model
        self.view=LoadingView(self)
        self.tasks=[
            (15, "Conectando con GPT...", lambda: self.connect_gpt()),
            (30, "Recopilando Informacion del Paper...", lambda: self.search_information_paper()),
            (45, "Buscando Referencias...", lambda: self.search_references()),
            (60, "Buscando Contribuciones...", lambda: self.search_contributions()),
            (99, "Armando Grafo...", lambda: self.arming_graph()),
            (100, "Cerrando Ventana...", lambda: self.destroy_view())
        ]
        self.current_task_index = 0

    def run(self):
        self.execute_next_task()
        self.view.window.mainloop()
        
    def update_progress(self, value, text):
        self.view.update_progress(value, text)

    def execute_next_task(self):
        if self.current_task_index < len(self.tasks):
            progress, text, task = self.tasks[self.current_task_index]
            self.update_progress(progress, text)
            task()

    def complete_task(self):
        self.current_task_index += 1
        self.view.window.after(20, self.execute_next_task)

    def on_close(self):
        sys.exit()

    def destroy_view(self):
        self.view.window.destroy()
        

    def connect_gpt(self):
        print("Connecting with GPT...")
        # Here goes the logic to connect with GPT
        self.complete_task()

    def search_information_paper(self):
        from app.Controller import InformationPaperController
        print("Searching for information...")
        #paper=gpt_funcion():
        #if paper:
        #    self.paper=paper
        #else:
        secondary_window = tk.Toplevel(self.view.window)
        InformationPaperController(self.model,secondary_window, self.complete_task).run()
        self.complete_task()

    def search_references(self):
        print("Searching for references...")
        # Reference search logic
        self.complete_task()

    def search_contributions(self):
        print("Searching for contributions...")
        # Contribution search logic
        self.complete_task()

    def arming_graph(self):
        print("Constructing graph...")
        # Logic for constructing the graph
        self.complete_task()

    
