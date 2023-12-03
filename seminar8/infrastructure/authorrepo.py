import sys
sys.path.append(r"D:\seminar8")
from domain.author import Author


class AuthorRepository:

    def __init__(self):
        self.__data=[]

    def getData(self):
        return self.__data
    def setData(self,d):
        self.__data=d

    #does our repository contain an author?
    def contains(self,a):
        for elem in self.__data:
            if a==elem:
                return True
        return False

    #adds an author to the repository
    def add_author(self,a):
        self.__data.append(a)

    #insert an author to the repository at a certain index
    #def insertBook(self,a,index):
        #self.__data.insert(index,a)

    #delete a certain author from the authors repository
    def delete_author_from_authorRepo(self,author):
        for i in range(len(self.__data)-1,-1,-1):
            if self.__data[i]==author:
                del self.__data[i]



    def __str__(self):
        s=""
        for i in range (0,len(self.__data)):
            s+=str(self.__data[i])+"\n"
        return s

'''
author1=Author("m","e",28)
author2=Author("m","e1",30)
author3=Author("m","e2",30)
author4=Author("hsjs","e2",30)

ar=AuthorRepository()

ar.add_author(author1)
ar.add_author(author2)
ar.add_author(author3)
'''
#print(str(ar))
