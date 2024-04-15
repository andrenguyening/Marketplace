from flask import Flask, request, render_template, redirect, session, url_for
from listings import ListingRepo, Listing
import sqlite3

app = Flask(__name__)

app.secret_key = 'secret_key'

DATABASE = 'data.db'

def create_connection():
    return sqlite3.connect(DATABASE)

@app.route("/")
def home():
    return render_template('layout.html')

@app.route('/account', methods=['POST','GET'])
def account():
    if 'user' in session:
        conn = create_connection()
        cursor = conn.cursor()
        #Retrieving the data
        cursor.execute("SELECT * FROM Listing WHERE author_id = ?", (session['user'],))
        rows = cursor.fetchall()
        listings = []
        for row in rows:
            listings.append(Listing(row[0],row[1], row[2], row[3], row[4], row[5]))
        cursor.close()
        conn.close()
        return render_template('account.html', listings = listings)
    return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    #DO NOT STORE USER AND PASS LIKE THIS, JUST FOR PROJECT SIMPLICITY
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = create_connection()
        cursor = conn.cursor()

        # Query the database to check if the username and password match
        cursor.execute("SELECT * FROM Account WHERE author_id = ? AND pass = ?", (username, password))
        account = cursor.fetchone()
        conn.close()

        if account:
            session['user'] = request.form['username']
            return redirect(url_for('market'))
        else:
            return "Invalid username or password."
    else:
            return render_template('login.html')
    
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route("/market")
def market():
    listing_data = ListingRepo()
    listings = []
    for row in listing_data.get_data('data.db'):
        listings.append(Listing(row[0],row[1], row[2], row[3], row[4], row[5]))
    return render_template('market.html', listings = listings)

@app.route('/sell', methods=['POST', 'GET'])
def sell():
    if 'user' not in session:
        return "Need to log in before selling!"
    if request.method == 'POST':
        print('hello')
        author_id = session['user']
        desc = request.form['desc']
        item_title = request.form['item_title']
        price = request.form['price']
        category = request.form['category']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Listing (author_id, title, desc, price, category) VALUES (?, ?, ?, ?, ?)", 
                    (author_id, item_title, desc, price, category))
        conn.commit()
        conn.close()
        return redirect(url_for('market'))
    else:
        return render_template('sell.html')
    
    
@app.route('/create', methods = ['POST','GET'])
def create():
    if request.method == 'POST':
        print('post')
        author_id = request.form['user']
        password = request.form['pass']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Account (author_id, pass) VALUES (?, ?)", 
                    (author_id, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    else:
        print('create page')
        return render_template('create.html')
    

if __name__ == '__main__':
    app.run(debug=True)