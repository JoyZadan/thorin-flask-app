"""
Imports the Flask class and creates an instance of this class
"""
import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    The @app.route above is a decorator
    A decorator is a way of wrapping functions.
    The root decorator binds the index() function to itself, so that
    whenever that root is called, the function is called.
    This function renders content as HTML
    Flask will look inside the templates directory or folder
    to find the HTML files referenced in the return, ie, index page
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    This function renders content as HTML
    Flask will look inside the templates directory or folder
    to find the HTML files referenced in the return, ie about page.
    Creates an empty directory to hold the json data.
    """
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    """
    Same as above functions.
    Creates an empty object to store data.
    Advanced routing features in Flask:
    - creates separate url (key) for each member inside the json file
    and returns url in individual member's name (value).
    - returns the view for member.html for each member
    """
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # return "<h1>" + member["name"] + "</h1>"
    return render_template("member.html", member=member)


@app.route("/contact")
def contact():
    """
    Renders content as HTML
    Flask will look inside of the templates directory or folder
    to find the HTML files referenced in the return, ie contact
    """
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    """
    Renders content as HTML
    Flask will look inside of the templates directory or folder
    to find the HTML files referenced in the return, ie careers
    """
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
