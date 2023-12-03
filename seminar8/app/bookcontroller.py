# it knows where all the functions are
import sys
sys.path.append(r"D:\seminar8")
from infrastructure.bookrepo import BookRepository
from infrastructure.authorrepo import AuthorRepository

#from infrastructure.bookrepo import BookRepository,br,book4,book5
#from infrastructure.authorrepo import AuthorRepository,ar

class BookController:
    def __init__(self,bRepo,aRepo):
        self.__bRepo=bRepo
        self.__aRepo=aRepo

    def bRepo_getter(self):
        return self.__bRepo
    def aRepo_getter(self):
        return self.__aRepo

    def bRepo_setter(self,bRepo):
        self.__bRepo=bRepo
    def aRepo_setter(self,aRepo):
        self.__aRepo=aRepo

   #1.Add a new book to the library
    def addBook(self,b): #directly the book object
        self.__bRepo.addBook(b)
        if not self.__aRepo.contains(b.author_getter()):
            self.__aRepo.add_author(b.author_getter())

    # 2.Insert a new book to the library
    def insertBook(self,b,index):
        self.__bRepo.insertBook(b,index)
        if not self.__aRepo.contains(b.author_getter()):
            self.__aRepo.add_author(b.author_getter())

    #3. Delete a book from the library
    def deleteBook(self,index):
        if not self.__bRepo.books_same_author(index):
            authorAtIndex=self.__bRepo.author_of_book_by_index(index)
            self.__aRepo.delete_author_from_authorRepo(authorAtIndex)
        self.__bRepo.delete(index)

    #4. Delete all books written by a given author
    def delete_books_by_author(self,author):
        self.__aRepo.delete_author_from_authorRepo(author)
        self.__bRepo.delete_booksByAuthor(author)

    #5.Delete all books in given period (two years are specified)
    def delete_books_by_period(self,year1,year2):
        authors=self.__bRepo.delete_booksByPeriod(year1,year2)
        for elem in authors:
            self.__aRepo.delete_author_from_authorRepo(elem)

    def __str__(self):
        return str(self.__bRepo)+"\n"+str(self.__aRepo)
    #7. Get all books from a certain year
    def books_by_year_controller(self,year):
        self.__bRepo.get_books_by_year_repo(year)

    #8.Get all books with title containing a given word
    def books_word_controller(self,w):
       books=self.__bRepo.books_word_repo(w)
       return books

    #9.Determine the oldest book
    def oldest_book_controller(self):
        book=self.__bRepo.oldest_book_repo()
        return book

    #10.Filter books with author starting with specified letter
    def books_starting_with_letter_controller(self, l):
        booksList=self.__bRepo.books_starting_with_letter_repo(l)
        return booksList

    #11.Identify books with at least 2 authors
    def books_more_authors_controller(self):
        s=self.__bRepo.books_at_least2_authors()
        return s
    #12.Update book by price
    def update_book_by_code_controller(self,code):
        authors=self.__bRepo.update_book_by_code_repo(code)
        self.__aRepo.delete_author_from_authorRepo(authors[1])
        self.__aRepo.add_author(authors[0])


#print(str(ar))
#print(str(br))

'''
bc=BookController(br,ar)
print(str(bc))
'''

'''
bc.addBook(book4)
print(str(bc))

bc.addBook(book5)
print(str(bc))
'''
'''
bc.insertBook(book4,2)
print(str(bc))

bc.insertBook(book5,0)
print(str(bc))
'''
