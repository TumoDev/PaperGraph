from app.View import InformationPaperView
from app.Utils import Paper
from app.Utils import GPT
import sys


class InformationPaperController:
    def __init__(self, model, window, on_close_callback=None):
        self.model=model
        self.view=InformationPaperView(self, window)
        self.on_close_callback=on_close_callback

    def run(self):
        self.view.window.mainloop()

    def destroy_view(self):
        if self.on_close_callback:
            self.on_close_callback()
        self.view.window.destroy()
    
    def on_close(self):
        sys.exit()
    
    def create_paper(self,title,author,date):
        paper = Paper(title,author,date)
        content=GPT.extract_fragment_with_tokens('assets/papers/input_paper/archivo.pdf')
        paper.set_content(content)
        id = paper.get_id
        self.model.set_current_id_node(id)
        self.model.add_paper(paper, None)
        self.destroy_view()
        
