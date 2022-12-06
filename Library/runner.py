import book as b
import library as l

def main():
    booksForLib = fileRead("DumbPython/books.txt")
    lib = createLib(booksForLib)
    lib.printBookTitles()
    print()
    lib.printBookAuthors()
    print()
    book = lib.findTitle("Python: For Dummies!")
    if book == 0:
        None
    else:
        print(book.getTitle())
        print(book.getAuthor())
        print(book.getDesc())
    print()
    print("Test lib.contains: " + str(lib.contains(book)))
    testBook = b.Book("author", "title")
    print("Test lib.contains nonexistent: " + str(lib.contains(testBook)))
    print()
    print("Test addBook: " + str(lib.addBook(testBook)))
    print("Test addBook duplicate: " + str(lib.addBook(testBook)))
    print()
    print("Test removeBook: " + str(lib.removeBook(testBook)))
    print("Test removeBook nonexisitent: " + str(lib.removeBook(testBook)))
    print()
    


def fileRead(filename):
    books = []
    f = open(filename, "r")
    line = f.readline()
    while not line == "":
        steps = line.split("_")
        if len(steps) == 3:
            book = b.Book(steps[0], steps[1])
            book.setDesc(steps[2])
        elif len(steps) == 2:
            book = b.Book(steps[0], steps[1])
        elif len(steps) == 1:
            book = b.Book(steps[0], "unknown")
        else:
            None
        books.append(book)
        line = f.readline()
    
    f.close()
    return books
    
def createLib(bookSet):
    lib = l.Library(bookSet)
    return lib


main()