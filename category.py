import sqlite3

class Category:
    def __init__(self, name):
        self.name = name
    
    def get_listings(self):
        #Connecting to the database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        #Retrieving the data
        cursor.execute("SELECT * FROM Listing WHERE category = ?", (self.name,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        print(rows)
        return rows