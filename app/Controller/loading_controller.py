import sys
from app.View import LoadingView
from app.Utils import GPT
from app.Utils import Paper
import tkinter as tk
import json

class LoadingController:
    def __init__(self, model):
        self.model= model
        self.view=LoadingView(self)
        self.tasks=[
            (33, "Recopilando Informacion del Paper...", lambda: self.search_information_paper()),
            (66, "Buscando Referencias y contribuciones...", lambda: self.search_references_and_contributions()),
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

    def search_information_paper(self):
        from app.Controller import InformationPaperController
        print("Searching for information...")
        #paper=GPT_funcion():
        #if paper:
        #    self.paper=paper
        #else:
        secondary_window = tk.Toplevel(self.view.window)
        InformationPaperController(self.model,secondary_window, self.complete_task).run()
        self.complete_task()

    def search_references_and_contributions(self):
        print("Searching references and contributions...")
        references = GPT.Gpt('assets/papers/input_paper/archivo.pdf')
        for ref_details in references["references"]:
            paper = Paper(title=ref_details["title"], 
                        author=ref_details["author"], 
                        date=ref_details["year"])
            self.model.add_paper(paper)
            print(paper.get_title)
            print(paper.get_author)
            print("----------------------------------------------")
        self.complete_task()