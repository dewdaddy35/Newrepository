from flask import Flask         # From the flask module import the Flask class

#OOP - Object Oriented Paradigm
# class is to object as blueprint is to house
app = Flask(__name__)            # Create an object from the Flask class (instance)

@app.get("/")                   # Flask decorator to map routes to veiw functions
def index():                    # Flask view function (wrapped)
    me = {                      # Python dictionary
        "first_name": "Eric",
        "last_name":  "Wells",
        "hobbies": "Baseball",
        "is_active": True
    }
    return me                   # When you return a dictionary from flask
                                # it gets converted to JSON automatically
