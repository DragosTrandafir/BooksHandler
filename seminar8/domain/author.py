class Author:
    def __init__(self,f="",l="",a=0):
        self.__first=f
        self.__last=l
        self.__age=a

    def __eq__(self, other):
        return (

                self.__first == other.__first and
                self.__last == other.__last and
                self.__age==other.__age
        )

    def first_getter(self):
        return self.__first
    def last_getter(self):
        return self.__last
    def age_getter(self):
        return self.__age
    def read_author(self):
        f=input("Author first name: ")
        l=input("Author last name: ")
        a=int(input("Author age: "))
        self.first_setter(f)
        self.last_setter(l)
        self.age_setter(a)

    def first_setter(self,f):
        self.__first=f
    def last_setter(self,l):
        self.__last=l
    def age_setter(self,a):
        self.__age=a

    #checks if the author is starting with a letter
    def check_first_letter(self,l):
        if self.__first[0]==l:
            return True
        return False

    def __str__(self):
        return "Author( "+self.__first+" "+self.__last+", "+str(self.__age)+" years )"

