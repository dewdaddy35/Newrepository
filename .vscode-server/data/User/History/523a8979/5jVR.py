#!/user/bin/env python3

app = Flask(__name__)            # Create an object from the Flask class (instance)

@app.get("/")                   # Flask decorator to map routes to veiw functions
def index():                    # Flask view function (wrapped)
    me = {                      # Python dictionary
        "first_name": "Eric",
        "last_name":  "Wells",
        "hobbies": "Baseball",
        "is_active": True
    }
    return me       



@app.route("/products")
def products():
    product_list = ["Apples", "Oranges", "Bananas"]
    bullet_list = "".join(
        "<li>%s</li" % product for product in product_list
    )
    return "<ul>%s</ul>" % bullet_list