# Jonathan Sonnek
# December 5 2025
# Program 2

import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('cities.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Display the cities.
    print('Contents of Cities database:')
    cur.execute('SELECT CityName, Population FROM Cities')
    results = cur.fetchall()
    for Name, Population in results:
        print(f'{Name} {Population:,.0f}')

    # Close the connection.
    conn.close()

if __name__ == '__main__':
    main()