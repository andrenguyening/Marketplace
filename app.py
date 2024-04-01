from flask import Flask, request, render_template
from listings import ListingRepo, Listing
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)