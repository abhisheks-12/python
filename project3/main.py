class Library:

    def __init__(self,listofbooks):
        self.books = listofbooks

    def displayBooks(self):
        print("List of books are: ")
        for book in self.books:
            print("*" + book)

    def borrowBooks(self,bookName):
        if bookname in self.books:
            print("You have borrowed book succesfully.")
            self.books.remove(bookname)
            return True
        else:
            print("This book is not Avilable.")
            return False

    
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning book...")


class Student:  

    def reqBook(self):
        self.book = input("Enter the name of book u want to return. ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book u want to borrow: ")
        return self.book


if __name__ == "__main__":
    central_library = Library(["Lets us c","python","Java","Data structure"])
    student = Student()

    while True:

        wlcmsg = ''' _____Welcome to The central Library____
        List of books:
        1.Press 1 to get list of books
        2.Press 2 to req book
        3.Press 3  to return book
        4.Press 4 to Exit 
        '''

        print(wlcmsg)
        a = int(input("Enter u r choice: "))

        if a == 1:
            central_library.displayBooks()

        elif a == 2:
            central_library.borrowBooks(student.reqBook())

        elif a == 3: 
            central_library.returnBook(student.returnBook())

        else:
            print("thanks for using this library.")
            exit()


 
