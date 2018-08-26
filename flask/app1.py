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
def static_page():
    return "welcome to book store"

@app.route("/index/")
def render_static():
    return render_template('index.html',books=books)


@app.route('/books/')
def hi_flask():
    users = [ "Frank", "Steve", "Alice", "Bruce" ]
    return render_template('books.html',users=users)



app.run(port=3300)


#JSON=> Javascript object notataion