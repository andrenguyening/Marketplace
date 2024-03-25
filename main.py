import sqlite3
from listings import Listing
from account import Account

#Data access layer
class ListingRepo():
    def get_data(self, database):
        #Connecting to the database
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        #Retrieving the data
        cursor.execute("SELECT * FROM Listing")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    
#Presentation
class ListingView():
    def __init__(self, listings):
        self.listings = listings
    def show(self):
        for row in self.listings:
            print(row.id, " ",
                  row.author, " ", 
                  row.title, " ", 
                  row.desc, " ", 
                  row.price, " ", 
                  row.category, " ", 
                  row.status
                  )
        
def main():
    listing_data = ListingRepo()
    listings = []
    for row in listing_data.get_data('data.db'):
        listings.append(Listing(row[0],row[1], row[2], row[3], row[4], row[5]))
    view = ListingView(listings)
    view.show()
    
if __name__ == "__main__":
    main()