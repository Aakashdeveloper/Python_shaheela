from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='')
app.config["MONGO_URI"] = "mongodb://localhost:27017/carsApp"
mongo = PyMongo(app)

books = [
    {
        'name': 'Green egges and hams',
        'price': '$3.67',
        'isbn': 78900765478
    },
    {
        'name': 'The cat in the hat',
        'price': '$9.67',
        'isbn': 98765465544
    }
]
@app.route('/')
def static_page():
    return "welcome to book store"

@app.route("/index/")
def render_static():
    return render_template('index.html',books=books)

@app.route("/data/")
def home_page():
    online_users = mongo.db.cars.find({})
    return render_template("data.html",
        online_users=online_users)

@app.route('/books/')
def hi_flask():
    users = [ "Frank", "Steve", "Alice", "Bruce" ]
    return render_template('books.html',users=users)



app.run(port=3300)


#JSON=> Javascript object notataion