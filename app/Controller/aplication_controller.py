from app.View import AplicationView

import sys

class AplicationController:
    def __init__(self, model):
        self.model=model
        self.view=AplicationView(self)
        
    def run(self):
        self.view.window.mainloop()

    def on_close(self):
        sys.exit()

    def display_paper_data(self):
        paper=self.model.get_first_paper()
        return paper.get_title, paper.get_author, paper.get_date, paper.get_content