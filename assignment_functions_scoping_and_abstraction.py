def print_menu():
    pass

def format_record(book_info):
    pass

def list_books(list_of_books):
    pass

def add_book(file_name, list_of_books):
    pass

def edit_book(file_name, list_of_books):
    pass

def search_book(list_of_books):
    pass

def delete_book(file_name, list_of_books):
    pass

def checkout_book(file_name, list_of_books):
    pass

def return_book(file_name, list_of_books):
    pass

def display_totals(list_of_books):
    pass

def load_books(file_name):
    pass

def update_books(file_name, list_of_books):
    pass

def main():
    file_name = input('Enter the book catalog file name: ')
    list_of_books = load_books(file_name)

    print_menu()
    option = input('Select an option: ')
    
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
            checkout_book(file_name, list_of_books)
        elif option.lower() == 'r':
            return_book(file_name, list_of_books)
        elif option.lower() == 't':
            display_totals(list_of_books)

        print_menu()
        option = input('Select an option: ')
    
    print('Goodbye!')

if __name__=="__main__":
    main()