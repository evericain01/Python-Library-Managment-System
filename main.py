# Importing Random module to generate random ISBN numbers
from random import randrange


class Book:
    # Constructor for the Book class
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = randrange(1000000000000, 9999999999999)

    # Method to display the book details
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) ISBN: {self.isbn}"


class Library:
    # Constructor for the Library class
    def __init__(self, name):
        self.name = name
        self.books = []

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)

    # Method to remove a book from the library
    def remove_book(self, book):
        self.books.remove(book)

    # Method to update a book in the library
    def update_book(self, book, new_title, new_author, new_year, new_isbn):
        book.title = new_title
        book.author = new_author
        book.year = new_year
        book.isbn = new_isbn

    # Method to display all the books in the library
    def display_books(self):
        print("\n*******BOOKS*******")
        for book in self.books:
            print(book)
        print("*******************\n")

    # Method to return the number of books in the library
    def __str__(self):
        return f"{self.name} has {len(self.books)} books."

def main():
  # Instantiating library
  library = Library("Your Library")
  
  # Adding some books to the library
  book1 = Book("Coding101", "Andrew Peterson", 1937)
  book2 = Book("Networking", "Henry Killon", 1954)
  book3 = Book("Java Fundamentals", "Sasha Cliton", 1977)
  
  # Adding the books to the library
  library.add_book(book1)
  library.add_book(book2)
  library.add_book(book3)
  
  while True:
      # Display the number of books in the library
      print("You have " + str(len(library.books)) + " books in your library.")
  
      # Display all the books in the library
      library.display_books()
  
      while True:
          # Display the menu
          try:
              # Get the user's choice
              choice = int(input("What would you like to do?\n"
                                 "1. Add a book\n"
                                 "2. Remove a book\n"
                                 "3. Update a book\n"
                                 "4. Exit\n"
                                 "Enter your choice: "))
              # If the user enters 1, add a book
              if choice == 1:
                  title = input("Enter the title of the book: ")
                  author = input("Enter the author of the book: ")
                  year = int(input("Enter the year the book was published: "))
                  book = Book(title, author, year)
                  library.add_book(book)
                  print(f"\n{book} has been added to the library.\n")
  
              # If the user enters 2, remove a book
              elif choice == 2:
                  while True:
                      try:
                          isbn = int(input("Enter the ISBN of the book you want to remove: "))
                          break
                      except ValueError:
                          print("Invalid ISBN. Please enter a number.")
                  for book in library.books:
                      if book.isbn == isbn:
                          library.remove_book(book)
                          print(f"\n{book} has been removed from the library.\n")
                          break
                  else:
                      print("\nBOOK NOT FOUND!\n")
  
              # If the user enters 3, update a book
              elif choice == 3:
                  while True:
                      try:
                          isbn = int(input("Enter the ISBN of the book you want to update: "))
                          break
                      except ValueError:
                          print("\nInvalid ISBN. Please enter a number.\n")
                  for book in library.books:
                      if book.isbn == isbn:
                          new_title = input("Enter the new title of the book: ")
                          new_author = input("Enter the new author of the book: ")
                          new_year = int(input("Enter the new year the book was published: "))
                          new_isbn = int(input("Enter the new ISBN of the book: "))
                          library.update_book(book, new_title, new_author, new_year, new_isbn)
                          print(f"\n{book} has been updated.\n")
                          break
                  else:
                      print("\nBOOK NOT FOUND!\n")
  
              # If the user enters 4, exit the program
              elif choice == 4:
                  print("Goodbye!")
                  exit()
              if choice not in [1, 2, 3, 4]:
                  raise ValueError
              break
          # If the user enters a number that is not 1, 2, 3, or 4, display an error message
          except ValueError:
              print("\nInvalid choice. Please enter a number between 1 and 4.\n")
              break

# To run the main function above
if __name__ == "__main__":
    main()
