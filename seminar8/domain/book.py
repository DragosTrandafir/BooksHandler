from domain.author import Author
class Book:
    def __init__(self,a=Author(),t="",y=0,p=0,code=0):
        self.__author = a #Author
        self.__title = t
        self.__year = y
        if p<0:
            raise ValueError("Price cannot be negative!")
        self.__price = p
        self.__code = code

    #checks if a string is in title
    def checkTitle(self,w):
        if w in self.__title:
            return True
        return False


    def __eq__(self,other):
        return (
            self.__year==other.__year and self.__title==other.__title and self.__price==other.__price
        )
    def author_getter(self):
        return self.__author
    def title_getter(self):
        return self.__title
    def year_getter(self):
        return self.__year
    def price_getter(self):
        return self.__price
    def code_getter(self):
        return self.__code

    def author_setter(self,a):
        self.__author=a
    def title_setter(self,t):
        self.__title=t
    def year_setter(self,y):
        self.__year=y
    def price_setter(self,p):
        if p<0:
            raise ValueError("Price cannot be negative!")
        self.__price=p
    def code_setter(self,code):
        self.__code=code

    def read_book(self):
        author=Author()
        author.read_author()
        t=input("Book title: ")
        y=int(input("Book year: "))
        p=int(input("Book price: "))
        c=int(input("Book code: "))
        self.author_setter(author)
        self.title_setter(t)
        self.year_setter(y)
        self.price_setter(p)
        self.code_setter(c)

    def __str__(self):
        return ("Book- "+str(self.__author)+" "+self.__title+" "+str(self.__year)+" "+str(self.__price)+" "
                +str(self.__code))



'''
author=Author("Mihai","Eminescu",18)
print(str(author))
book=Book(author,"Luceafarul",1800,199)
print(str(book))
'''
'''
book=Book()
book.read_book()
print(str(book))
'''
