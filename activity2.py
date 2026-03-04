class library:
    def __init__(self,book,list):
        self.book = book
        self.booklist = list
        self.lenddict = {}
    
    def display(self):
        print("Available books are:", self.book)
        for i in self.booklist:
            print(i)
    
    def lend_book(self,username,book):
        if book in self.lenddict.keys():
            print(f"book is already being used {self.lenddict[book]}" )
        else:
            self.lenddict.update({book:username})
            print("Lender OOPs database has been update. You can take the book")
    
    def add_book(self,book):
        self.booklist.append(book)
        print("Book has been added to the booklist")

    def return_book(self,username,book):
        if book in self.lenddict.keys():
            self.lenddict.pop(book)
            print("Book has been removed from lent list")
        else:
            print("Book is not in database")


if __name__ == "__main__":
    books = library("Let's Upskill", ["Python", "Rich dad poor dad", "Harry Potter", "C++ Basics"])
    while True:
        print(f"Welcome to the {books.book} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend books")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input()
        if user_choice not in ["1", "2","3","4"]:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            books.display()
        
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend")
            user = input("Enter your name")
            books.lend_book(user,book)
        
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add")
            books.add_book(book)
        
        elif user_choice == 4:
            book = input("Enter the book you want to return")
            books.return_book("Bhavishya",book)
        
        else:
            print("Not a valid option")
        

        print("Press Q to quit and C to continue")

        user_choice2 = input()
        while(user_choice2 != "C" and user_choice2 != "Q"):
            if user_choice2 == "Q":
                exit()
            elif user_choice2 == "C":
                continue

    


    
        