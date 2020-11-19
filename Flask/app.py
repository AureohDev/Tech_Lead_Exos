import os
from flask import Flask, request, render_template, jsonify, json, url_for
app = Flask(__name__)

books=[{
    'id':1,
    'titre' : 'un titre',
},
{
    'id':2,
    'titre' : 'un autre titre random',
}]

def load_books():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "json", "books.json")
    return json.load(open(json_url))  


@app.route("/")
def index():
    return render_template('index.html')

#API
@app.route("/api/books", methods=['GET','POST'])
def books():
    return jsonify(load_books())

@app.route("/api/book/id/<book_id>")
def book_by_id(book_id=1):
    book_id = int(book_id)
    results = []
    for book in books:
        if book['id'] == book_id:
            results.append(book)

    if not results:
        return 'Livre introuvable'
    else :
        return jsonify(results)


@app.route("/about")
def about():
    return 'The about page'

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form() 

if __name__ == '__main__':
    app.run(debug=True)