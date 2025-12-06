# Jonathan Sonnek
# December 5th 2025
# Program 3

import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a database cursor.
    cur = conn.cursor()
    
    # Add the Entries table.
    add_table(cur)
    
    # Add rows to the Cities table.
    add_entries(cur)
    
    # Commit the changes.
    conn.commit()

    # Display the cities.
    display_entries(cur)
    
    # Close the connection.
    conn.close()

# The add_cities_table adds the Cities table to the database.
def add_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Entries')

    # Create the table.
    cur.execute('''CREATE TABLE Entries (EntryId INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT NOT NULL,
                                        PhoneNumber TEXT NOT NULL)''')

# The add_cities function adds 5 rows to the Entries table.
def add_entries(cur):
    entries_pop = [(1,'Herold','380-010-9500'),
                  (2,'Frank','257-031-0968'),
                  (3,'Jim','237-407-2378'),
                  (4,'Max','210-662-4523'),
                  (5,'Terry','210-425-3800')]
    
    for row in entries_pop:
        cur.execute('''INSERT INTO Entries (EntryId, Name, PhoneNumber)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

# The display_cities function displays the contents of
# the Cities table.
def display_entries(cur):
    print('Contents of phonebook.db/Entires table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:10}')

# Execute the main function.
if __name__ == '__main__':
    main()
