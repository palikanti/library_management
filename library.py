git Init
Available_books = ["Harry Potter", "Percy Jackson", "Hobbit", "Dracula", "Frankenstein"]
Borrowed_books = {}

def func():
  borrow = input("what book would you like to borrow? ")
  error = input("Please try again? ")
  if borrow == Available_books:
    y = 1
  elif:
  print('try a different book.')

  Time = input("when would you like to borrow? ")
  Available_books.remove(borrow)
  Borrowed_books.update({borrow: Time})
func()


def view_Borrowed_books():
  for i in range(len(Borrowed_books)):
    print(f'These books are being borrowed on these dates, {Borrowed_books}')
view_Borrowed_books()


def view_Available_books():
    for i in range(len(Available_books)):
      print(Available_books)
view_Available_books()

while x != 3:
  if x 
