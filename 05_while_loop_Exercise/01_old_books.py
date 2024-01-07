books = input()
books_counter = 0

while True:
    current_book = input()
    if current_book == books:
        print(f"You checked {books_counter} books and found it.")
        break
    elif current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_counter} books.")
        break
    books_counter += 1
