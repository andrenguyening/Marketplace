from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('layout.html')

@app.route("/market")
def market():
    # get data
    return render_template('market.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)