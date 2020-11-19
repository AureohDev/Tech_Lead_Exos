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
def api_books():
    return jsonify(load_books())

@app.route("/api/book/id/<id>")
def api_book_by_id(id=1):
    id = int(id)
    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)

    if not results:
        return 'Livre introuvable'
    else :
        return jsonify(results)

@app.route("/api/book/title/<title>")
def api_book_by_title(title=1):
    title = str(title)
    results = []
    books = load_books()
    for book in books:
        if book['title'] == title:
            results.append(book)

    if not results:
        return 'Livre introuvable'
    else :
        return jsonify(results)

@app.route("/api/book/pagecount/<count>")
def api_book_by_pagecount(count=1):
    count = int(count)
    results = []
    books = load_books()
    for book in books:
        if book['pageCount'] == count:
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