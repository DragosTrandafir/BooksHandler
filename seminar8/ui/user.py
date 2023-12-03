import sys
sys.path.append(r"D:\seminar8")
from app.bookcontroller import BookController
from domain.book import Book
from domain.author import Author
class BookUI:
    def __init__(self,bCtrl):
        self.__bCtrl=bCtrl

    #6. Print all books
    def printBooks(self):
        return self.__bCtrl.bRepo_getter()

    #7. Get all books from a certain year
    def books_by_year_console(self,year):
        self.__bCtrl.books_by_year_controller(year)

    #8. Get all books containing a given word
    def printMenu(self):
        s=""
        s+="Menu\n"+"\t1.Add a new book to the library\n"+"\t2.Insert a book to the library\n"+"\t3.Delete a book from the library\n"+"\t4.Delete all books written by a given author\n"+"\t5.Delete all books in given period (two years are specified)\n"+"\t6.Get all books\n"+"\t7.Get all books from a certain year\n"+"\t8.Get all books with title containing a given word\n"+"\t9.Determine the oldest book\n"+"\t10.Filter books with author starting with specified letter\n"+"\t11.Identify books with at least 2 authors\n"+"\t12.Update book by code\n"+"\t0.STOP"
        return s

    def readOption(self):
        option= int(input("Read an option: "))
        return option
    def readIndex(self):
        index= int(input("Read an index: "))
        return index
    def readYear(self):
        year= int(input("Read an year: "))
        return year
    def readWord(self):
        word=input("Read a word: ")
        return word
    def readLetter(self):
        letter=input("Read a letter: ")
        return letter

    def readCode(self):
        code=input("Read a price: ")
        return code

    def readBookConsole(self):
        #return self.__bCtrl.readBookController()
        book = Book()
        book.read_book()
        return book
    def readAuthorConsole(self):
        a=Author()
        a.read_author()
        return a


    def start(self):
       start=False
       while start==False:
           print(self.printMenu())
           option=self.readOption()
           if option==1:
               b=self.readBookConsole()
               self.__bCtrl.addBook(b)
               print(str(self.__bCtrl))
           elif option==2:
               b = self.readBookConsole()
               index=self.readIndex()
               self.__bCtrl.insertBook(b,index)
               print(str(self.__bCtrl))
           elif option == 3:
               index = self.readIndex()
               self.__bCtrl.deleteBook(index)
               print(str(self.__bCtrl))
           elif option==4:
               author=self.readAuthorConsole()
               self.__bCtrl.delete_books_by_author(author)
               print(str(self.__bCtrl))
           elif option==5:
               year1=self.readYear()
               year2=self.readYear()
               self.__bCtrl.delete_books_by_period(year1, year2)
               print(str(self.__bCtrl))
           elif option==6:
               print(str(self.printBooks()))
           elif option==7:
               year = self.readYear()
               self.books_by_year_console(year)
           elif option==8:
               word= self.readWord()
               print(self.__bCtrl.books_word_controller(word))
           elif option==9:
               print(self.__bCtrl.oldest_book_controller())
           elif option==10:
               letter=self.readLetter()
               print(self.__bCtrl.books_starting_with_letter_controller(letter))
           elif option==11:
               print(self.__bCtrl.books_more_authors_controller())
           elif option==12:
               code=self.readCode()
               self.__bCtrl.update_book_by_code_controller(code)
               print(str(self.__bCtrl))
           elif option==0:
               start=True
           else:
               print("The option is not available!")

