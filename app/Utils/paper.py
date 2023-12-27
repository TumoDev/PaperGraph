class Paper:
    def __init__(self, title: str, author: str, date: str):
        self.title=title
        self.author=author
        self.date=date
        self.id=self.create_identifier()
        self.content=None
        self.location=None #"./assets/papers/"+id+".pdf" #innecesary
        self.references=[] 

    @property
    def get_title(self):
        return self.title
 
    @property
    def get_author(self):
        return self.author
    
    @property
    def get_date(self):
        return self.date
    
    @property
    def get_id(self):
        return self.id
    
    @property
    def get_content(self):
        return self.content
    
    @property
    def get_location(self):
        return self.location
    
    @property
    def get_references(self):
        return self.references

    #def set_content(self):
    #    texto_completo=self.extract_complete_text()
    #    self.content=GPT.extract_tokens(texto_completo)

    #def set_references(self,content):
    #    self.references=content
    
    def create_identifier(self):
        author_clean = self.author.split()[0].replace(" ", "").lower()
        title_word = self.title.split()[0].lower()
        return f"{author_clean}-{self.date}-{title_word}"