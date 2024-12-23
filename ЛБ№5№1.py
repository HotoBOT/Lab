class Book():


    title = "Искуство пофигизма"
    author = "М. Менсон"
    year = "6 сен 2017г"

    def get_info(self):
        print(Book.title)
        print(Book.author)
        print(Book.year)

info = Book()
Book().get_info()
