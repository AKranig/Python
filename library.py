import book as b

class Library:
    
    def __init__(self):
        None
        
    def __init__(self, books):
        self.books = books
        
    def getBooks(self):
        return self.books
    
    def findTitle(self, title):
        for book in self.books:
            if book.getTitle() == title:
                return book
            else:
                None
        return 0
    
    def findAuthor(self, author):
        authors = []
        for book in self.books:
            if book.getAuthor() == author:
                authors.append(book.getAuthor())
            else:
                None
        if authors.count > 0:
            return authors
        else:
            return 0
    
    def contains(self, book):
        return book in self.books
                                      
    def printBookTitles(self):
        for book in self.books:
            print(book.getTitle())
            
    def printBookAuthors(self):
        for book in self.books:
            print(book.getAuthor())
    
    def showDesc(self, book):
        foundBook = self.findTitle(book)
        if(foundBook == 0):
            print("Book not found")
        else:
            print(foundBook.getDesc())
            
    def addBook(self, book):
        if(book in self.books):
            return False
        else:
            self.books.append(book)
            return True
        
    def removeBook(self, book):
        if(book in self.books):
            self.books.remove(book)
            return True
        else:
            return False