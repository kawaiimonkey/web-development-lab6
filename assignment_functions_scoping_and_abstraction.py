from typing import Final
import os

#output a list of options and returns choice value
def print_menu():
    print("******************************")
    print("Library Book Management System")
    print("******************************")
    print("A) Add a book")
    print("L) List books")
    print("E) Edit a book")
    print("S) Search for a book")
    print("D) Delete a book")
    print("C) Checkout a book")
    print("R) Return a book")
    print("T) Display books totals")
    print("Q) Quit")
    return input("Select an option: ").lower()
    
#format details of book in string type
def format_record(book_info):
    return f"{book_info[0]},{book_info[1]},{book_info[2]},{book_info[3]},{book_info[4]}"

#show all books
def list_books(list_of_books):
    print("-" * 82)
    print(f"{'Title':<25}{'ID':<5}{'Author':<20}{'Year':<6}{'Available'}")
    print("-" * 82)
    for book in list_of_books:
        print(f"{book[0]:<25}{book[1]:<5}{book[2]:<20}{book[3]:<6}{book[4]}")
    
#add a book and save in a file
def add_book(file_name, list_of_books):
    book_id = input('Enter book ID: ')
    for book in list_of_books:
        if book_id == book[1]:
            return print(f'Book with ID# {book_id} already exists.')
    book_title = input('Enter book title: ')
    book_author = input('Enter book author: ')
    book_year = input('Enter book year: ')
    book_info = [book_title, book_id, book_author, book_year, 'Yes']
    list_of_books.append(book_info)
    update_books(file_name, list_of_books)
    print('Book added successfully.')

#edit a book by id and update the data of the book
def edit_book(file_name, list_of_books):
    book_id = input('Enter book ID to edit: ')
    for book in list_of_books:
        if book_id == book[1]:
            book[0] = input('Enter new title: ')
            book[2] = input('Enter new author: ')
            book[3] = input('Enter new year: ')
            update_books(file_name, list_of_books)
            return print(f'Book #{book[1]} is edited successfully.')
    return print('Book not found.')

#search books by id or name of book
def search_book(list_of_books):
    search = input('Enter book title or ID to search: ')
    count = 0
    found_list = []
    for book in list_of_books:
        if search.isdigit() == True and search == book[1]:
            count +=1
            found_list.append(book)
        elif search.isalpha() == True and (search in book[0] or search.lower() in book[0].lower()):
            count +=1
            found_list.append(book)        
    if count != 0:
        print('-'*90)
        print(f"{'Title':<25}{'ID':>0}{'Author':>20}{'Year':>25}{'Available':>20}")
        print('-'*90)
        for book in found_list:
            print(f'{book[0]:<25}{book[1]:<15}{book[2]:<28}{book[3]:<18}{book[4]:>0}')
        return print(f'{count} books found ')
    else:
        return print('Book not Found')

#delete a book by id and update data
def delete_book(file_name, list_of_books):
    del_id = input('Enter book ID to delete: ')
    for index in range(len(list_of_books)):
        if del_id == list_of_books[index][1]:
            list_of_books.remove(list_of_books[index])
            update_books(file_name, list_of_books)
            return print(f'Book with ID# {del_id} deleted successfully.')
    return print('Book not found.')
    

#checkout a book by id and update data
def checkout_book(file_name, list_of_books):
    book_id = input("Enter book ID to checkout: ")
    for book in list_of_books:
        if book[1] == book_id:
            if book[4] == "No":
                return f"Book #{book_id} is already checked out."
            else:
                book[4] = "No"
                update_books(file_name, list_of_books)
                return f"Book #{book_id} is checked out successfully."
    return "Book not found."

#return a book by id and status of return
def return_book(file_name, list_of_books):
    checkout_id = input('Enter book ID to return: ')
    for book in list_of_books:
        if book[1] == checkout_id and book[4] == 'No':
            book[4] = 'Yes'
            update_books(file_name, list_of_books)
            return print(f'Book #{checkout_id} is returned successfully.')
        elif book[1] == checkout_id and book[4] == 'Yes':
            return print(f'Book #{checkout_id} is already available.')
    return print('Book not found')
    
#Display the total number of states according to the book return status
def display_totals(list_of_books):
    available = 0
    checked = 0
    total = 0
    for book in list_of_books:
        total += 1
        if book[4] == 'Yes':
            available += 1
        elif book[4] == 'No':
            checked +=1
    print('-'*75)
    print(f"{'*** Summary of Books ***':^75}")
    print(f"{'# of Available Books':<0}{'# of Checked Books':^37}{'Total # of Books':>0}")
    print('-'*75)
    print(f"{available:>10}{checked:>30}{total:>25}")

#load data of books from file and store in a list
def load_books(file_name):
    book_list = []

    if os.path.isfile(file_name):
        with open(file_name,'r') as f:
            line = f.readline()
            while line != '':
                line = line.rstrip()
                if line == '':
                    break
                else:
                    book_list.append(line.split(','))
                line = f.readline()
        print(f'{len(book_list)} books have been loaded')
    else:
        with open(file_name, 'w') as f:
            print('File does not exist.')
    return book_list

#update data of books
def update_books(file_name, list_of_books):
    with open(file_name, 'w') as f:
        for book in list_of_books:
            line = format_record(book)
            f.write(line+'\n')
    return


#operation of system
def main():
    file_name = input('Enter the book catalog file name: ')
    list_of_books = load_books(file_name)

    
    option = print_menu()
    
    while option.lower() != 'q':
        if option.lower() == 'a':
            add_book(file_name, list_of_books)
        elif option.lower() == 'l':
            list_books(list_of_books)
        elif option.lower() == 'e':
            edit_book(file_name, list_of_books)
        elif option.lower() == 's':
            search_book(list_of_books)
        elif option.lower() == 'd':
            delete_book(file_name, list_of_books)
        elif option.lower() == 'c':
            print(checkout_book(file_name, list_of_books))
        elif option.lower() == 'r':
            return_book(file_name, list_of_books)
        elif option.lower() == 't':
            display_totals(list_of_books)
        else:
            print('Invalid option. Please try again.')

        option = print_menu()
    
    print('Goodbye!')

if __name__=="__main__":
    main()