#!/user/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World</h1>"




@app.route("/products")
def products():
    product_list = ["Apples", "Oranges", "Bananas"]
    bullet_list = "".join(
        "<li>%s</li" for product in product_list
    )
    return "<ul>%s</ul>" % bullet_list