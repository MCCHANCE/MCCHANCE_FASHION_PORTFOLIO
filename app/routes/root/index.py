from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template('root/index.html')


@app.route("/products.html")
def products():
    return render_template('root/products.html')


@app.route("/about.html")
def about():
    return render_template('root/about.html')


@app.route("/contact.html")
def contact():
    return render_template('root/contact.html')
