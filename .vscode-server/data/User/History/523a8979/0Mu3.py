#!/user/bin/env python3
from flask import Flask
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



