import sys
sys.path.append(r"D:\seminar8")
from domain.book import Book
#from infrastructure.authorrepo import AuthorRepository,ar,author1,author2,author3,author4
from infrastructure.authorrepo import AuthorRepository

class BookRepository:
    def __init__(self):
        self.__data=[]

    def getData(self):
        return self.__data
    def setData(self,d):
        self.__data=d

    #add a book to the repository
    def addBook(self,book):
        self.__data.append(book)

    #insert a book to the repository at a certain index
    def insertBook(self,book,index):
        self.__data.insert(index,book)

    #3. Delete a book from the repository
    def delete(self,index):
        del self.__data[index]

    #get the author of a book at a certain index
    def author_of_book_by_index(self,index):
        author=self.__data[index].author_getter()
        return author

    #verify if at least 2 books have the same author (one of them has index given)
    def books_same_author(self,index):
        author = self.__data[index].author_getter()
        c=0
        for elem in self.__data:
            if author == elem.author_getter():
                c+=1
        if c>=2:
            return True
        return False
    #4.delete all books from the repository with a given author
    def delete_booksByAuthor(self,author):
        for i in range(len(self.__data)-1,-1,-1):
            if self.__data[i].author_getter()==author:
                del self.__data[i]

    #5.Delete all books in given period (two years are specified)
    def delete_booksByPeriod(self,year1,year2):
        authorsToDelete=[]
        for i in range(len(self.__data)-1,-1,-1):
            if (self.__data[i].year_getter()>=year1 and self.__data[i].year_getter()<=year2):
                if self.books_dif_periods_same_authors(i,year1,year2):
                    authorsToDelete.append(self.__data[i].author_getter())
                del self.__data[i]
        return authorsToDelete

    #check if we have at least two books in different time periods but with the same author(we should not delete the author in this case!)
    def books_dif_periods_same_authors(self,i,year1,year2):
        for j in range(len(self.__data) - 1, -1, -1):
            if i != j and self.__data[j].author_getter() == self.__data[i].author_getter() and not (self.__data[j].year_getter() >= year1 and self.__data[j].year_getter() <= year2):
                return False
        return True

    #7. Get all books from a certain year
    def get_books_by_year_repo(self,year):
        for elem in self.__data:
            if elem.year_getter()==year:
                print(elem)


    #8.Get all books with title containing a given word

    def books_word_repo(self,w):
        lst=[]
        for elem in self.__data:
            if elem.checkTitle(w):
                lst.append(str(elem))
        return lst

    #9.Determine the oldest book
    def oldest_book_repo(self):
        year=self.__data[0].year_getter()
        book=self.__data[0]
        for i in range(1,len(self.__data)):
            if self.__data[i].year_getter()<year:
                year=self.__data[i].year_getter()
                book=self.__data[i]
        return book

    #10.Filter books with author starting with specified letter
    def books_starting_with_letter_repo(self,l):
        s=""
        for elem in self.__data:
            if elem.author_getter().check_first_letter(l):
                s+=str(elem)+"\n"
        return s

    #11.Identify books with at least 2 authors
    def books_at_least2_authors(self):
        s=""
        for i in range(0,len(self.__data)-1):
            for j in range(0,len(self.__data)):
                if self.__data[i].author_getter()!=self.__data[j].author_getter() and self.__data[i]==self.__data[j]:
                    s+=str(self.__data[i])+"\n"
        return s


    #12.Update book by price
    def update_book_by_code_repo(self,code):
        for i in range(0,len(self.__data)):
            if str(self.__data[i].code_getter())==str(code):
                oldAuthor=self.__data[i].author_getter()
                self.__data[i].read_book()
                return [self.__data[i].author_getter(),oldAuthor]

    #sort books by price
    def sortByPrice(self):
        #sort method (we dont have to return it)
        #sorted method if we dont want to return it
        self.__data.sort(key=lambda x: x.getPrice())


    def __str__(self):
        s=""
        for i in range (0,len(self.__data)):
            s+=str(self.__data[i])+"\n"
        return s

'''
book1=Book(author1,"e",1200,73)
book2=Book(author2,"e1",1892,82)
book3=Book(author3,"e2",3029,28)
book4=Book(author3,"enjss",30289,281)
book5=Book(author4,"enjss",30289,281)

br=BookRepository()

br.addBook(book1)
br.addBook(book2)
br.addBook(book3)
'''
#br.insertBook(book4,0)