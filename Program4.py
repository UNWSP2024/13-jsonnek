# Jonathan Sonnek
# December 5th 2025
# Program 4

import sqlite3

def main():
    choice = 0
    # Not Exit
    while choice != 4:
        print('\n----- Inventory Menu -----')
        print('1. Read a Phone Number')
        print('2. Update a Phone Number')
        print('3. Delete a Phone Number')
        print('4. Exit the program')

        choice = int(input('Enter your choice: '))

        # Validate the input.
        while choice < 1 or choice > 4:
            print(f'Valid choices are 1 through 4.')
            choice = int(input('Enter your choice: '))

        # Read
        if choice == 1:
            read()
        # Update
        elif choice == 2:
            update()
        # Delete
        elif choice == 3:
            delete()

# The read function reads an existing item.
def read():
    number = input('Enter a phone number to search for: ')

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''SELECT EntryId, Name, PhoneNumber FROM Entries
                           WHERE PhoneNumber == ?''',
                (number,))
    results = cur.fetchall()
    conn.close()

    for EntryId, Name, PhoneNumber in results:
        print(f'ID: {EntryId} Name: {Name} '
              f'Phone Number: {PhoneNumber}')
    print(f'{len(results)} row(s) found.')


def readAll():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''SELECT EntryId, Name, PhoneNumber FROM Entries''',)
    results = cur.fetchall()
    conn.commit()

    for EntryId, Name, PhoneNumber in results:
        print(f'ID: {EntryId} Name: {Name} '
              f'Phone Number: {PhoneNumber}')
    print(f'{len(results)} row(s) found.')

# The update function updates an existing item's data.
def update():
    # First let the user search for the row.
    readAll()

    # Get the ID of the selected item.
    selected_id = int(input('Select Entry Id to update: '))

    # Get the new values for item name and price.
    name = input('Enter the new name: ')
    phone_number = input('Enter the new phone number: ')

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    # Update the row.
    cur.execute('''UPDATE Entries
                           SET Name = ?, PhoneNumber = ?
                           WHERE EntryId == ?''',
                (name, phone_number, selected_id))

    print(f'{cur.rowcount} row(s) updated.')

    conn.commit()
    conn.close()

# The delete function deletes an item.
def delete():
    # First let the user search for the row.
    readAll()

    # Get the ID of the selected item.
    selected_id = int(input('Select Entry Id to delete: '))

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute('''Delete from Entries
                               WHERE EntryId == ?''',
                (selected_id,))

    print(f'{cur.rowcount} row(s) deleted.')

    conn.commit()
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()