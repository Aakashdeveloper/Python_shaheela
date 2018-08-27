from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='')

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

@app.route('/about/')
def about_page():
    return render_template('about.html', books = books)

app.run(port=4500)