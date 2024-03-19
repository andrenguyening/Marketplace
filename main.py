import sqlite3
from listings import Listing
from account import Account
def main():
    
    #Data access layer
    #Connecting to the database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    #Retrieving the data
    cursor.execute("SELECT * FROM Listing")
    rows = cursor.fetchall()
    
    #Presentation Layer (row is a tuple)
    for row in rows:
        print(row)
        
    cursor.close()
    conn.close()
if __name__ == "__main__":
    main()