from flask import Flask         #From the flask module import the flask class


app+ Flask(__name__)            #Create an object from the flask class (instance)

@app.get("/")                   # flask decorator to map routes to veiw functions
def index():                    # flask view function (wrapped)
    me = {                      # Python dictionary
        "first_name": "Eric",
        "last_name":  "Wells",
        "hobbies": "Baseball",
        "is_active": True
    }

    return me                   # When you return a dictionary from flask
                                # it gets converted to JSON automatically