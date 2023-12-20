from app.Controller import UploadPaperController, AplicationController, LoadingController

def main():
    UploadPaperController().run()
    
    LoadingController().run()
    
    AplicationController().run()

if __name__ == "__main__":
   main()


