from app.View import InformationPaperView

import sys

class InformationPaperController:
    def __init__(self, window, on_close_callback=None):
        self.view = InformationPaperView(self, window)
        self.on_close_callback = on_close_callback

    def run(self):
        self.view.window.mainloop()

    def destroy_view(self):
        if self.on_close_callback:
            self.on_close_callback()
        self.view.window.destroy()
    
    def on_close(self):
        sys.exit