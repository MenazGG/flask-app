Hello this is where you will put any documentation or how the codes work

Today 18/5/2026, 
me and Azizul will try to build the simple structure/skeleton of the web

In app.py 
# Import Flask tools
from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__)

# Homepage route
@app.route("/") <---------WARNING!name for homepage  here is "/" 
def home():
    return render_template("index.html")

# About page route
@app.route("/about")   <------------WARNING!
def about():
    return render_template("about.html")

# Contact page route
@app.route("/contact") 
def contact():
    return render_template("contact.html")

# Start the server
if __name__ == "__main__":
    app.run(debug=True)


JUST REMEMBER THAT THE NAME MUST BE SAME ON PYTHON ONLY 

