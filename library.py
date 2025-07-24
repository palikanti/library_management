Available_books = ["Harry Potter", "Percy Jackson", "Hobbit", "Dracula", "Frankenstein"]
Borrowed_books = {}

def borrowing():
  name = input("What is your name? ")
  borrow = input("what book would you like to borrow? ")
  Available_books.remove(borrow)
  Borrowed_books.update({name: borrow})
  print(Borrowed_books)

def view_Borrowed_books():
  for i in Borrowed_books:
    print(f'These books are being borrowed by these people, {Borrowed_books}.')

def view_Available_books():
  print(f"{Available_books} are available to borrow.")

def returning():
  username = input("What is your name? ")
  returned_book = input("what book are you returning? ")
  Borrowed_books[username]
  Available_books.append(returned_book)
  del Borrowed_books[username]
  print(Available_books)


choice = input("Choose an option. 1 for available books. 2 for borrowed books. 3 to borrow. 4 to return. 5 to end and exit. ")

while choice != '5':
  if choice == '1':
    view_Available_books()
  elif choice == '2':
    view_Borrowed_books()
  elif choice == '3':
    borrowing()
  elif choice == '4':
    returning()
  else:
    print('That is not an option, please try again. ')
  choice = input("Choose the options 1, 2, 3, 4 or 5 . 1 for available books. 2 for borrowed books. 3 to borrow. 4 to return. 5 to exit. ")

print('bye!')
