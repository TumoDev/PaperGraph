from app.Model import GraphModel
from app.View import UploadPaperView, LoadingView, AplicationView
from app.Controller import UploadPaperController, LoadingController, AplicationController



def main():
    UploadPaperController().run()
    
    model=GraphModel()

    LoadingController(model).run()

    AplicationController(model).run()

   
if __name__ == "__main__":
   main()


