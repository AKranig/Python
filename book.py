class Book:
    def __init__(self):
        None
        
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def setDesc(self, newDesc):
        self.description = newDesc
    
    def getDesc(self):
        return self.description
    
    