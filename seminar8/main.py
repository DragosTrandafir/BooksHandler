import sys
sys.path.append(r"D:\seminar8")
from ui.user import BookUI
from app.bookcontroller import BookController
from domain.author import Author
from domain.book import Book
from infrastructure.authorrepo import AuthorRepository
from infrastructure.bookrepo import BookRepository

bR=BookRepository()
aR=AuthorRepository()
ctrl=BookController(bR,aR)
user=BookUI(ctrl)
user.start()