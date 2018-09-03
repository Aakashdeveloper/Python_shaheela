from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='')
app.config["MONGO_URI"] = "mongodb://localhost:27017/shaheela"
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
def home_page():
    return render_template('home.html')

#@app.route('/about/')
#def about_page():
#    return render_template('about.html', books = books)

@app.route('/about/')
def about_page():
    online_users = mongo.db.first.find({})
    return render_template('about.html', online_users=online_users)

app.run(port=4500)