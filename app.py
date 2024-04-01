from flask import Flask, request, render_template
from listings import ListingRepo, Listing
import sqlite3

app = Flask(__name__)
DATABASE = 'data.db'

def create_connection():
    return sqlite3.connect(DATABASE)

@app.route("/")
def home():
    return render_template('layout.html')

@app.route("/market")
def market():
    listing_data = ListingRepo()
    listings = []
    for row in listing_data.get_data('data.db'):
        listings.append(Listing(row[0],row[1], row[2], row[3], row[4], row[5]))
    return render_template('market.html', listings = listings)

@app.route('/sell', methods=['POST', 'GET'])
def sell():
    if request.method == 'POST':
        author_id = request.form('user')
        desc = request.form('desc')
        item_title = request.form['item_title']
        price = request.form['price']
        category = request.form('category')
        new_listing = Listing(0,author_id,item_title,desc,price,category)
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Listing (author_id, title, desc, price, category) VALUES (?, ?, ?, ?, ?)", 
                    (author_id, item_title, desc, price, category))
        conn.commit()
        conn.close()
    else:
        return render_template('sell.html')
if __name__ == '__main__':
    app.run(debug=True)