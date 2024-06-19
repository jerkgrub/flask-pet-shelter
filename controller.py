from flask import Flask, render_template, session, request, redirect, url_for
from pets import Pet  # Ensure this import matches your project structure

app = Flask(__name__)
app.secret_key = "flaskProject"

@app.route("/")
def index():
    pets = Pet.getall_pets()
    return render_template("index.html", allpets=pets)

if __name__ == "__main__":
    app.run(debug=True)
