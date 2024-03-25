import sqlite3

class Account:
    def __init__(self, id, username, password):
        self.user = username
        self.id = id
        self.password = password
    
    #Get listings only owned by account
    def get_listings(self):
        #Connecting to the database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        #Retrieving the data
        cursor.execute("SELECT * FROM Listing WHERE id = ?", (self.id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        print(rows)
        return rows