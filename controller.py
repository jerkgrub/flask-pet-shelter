from flask import Flask, render_template, session, request, redirect, url_for
from pets import Pet  # Ensure this import matches your project structure

app = Flask(__name__)
app.secret_key = "flaskProject"

@app.route("/")
def index():
    pets = Pet.getall_pets()
    return render_template("index.html", allpets=pets)

@app.route("/pet/new")
def newpet():
    return render_template("newpet.html")

@app.route("/process/new/pet", methods=['POST'])
def create_new_pet():
    petname = request.form['petname']
    pettype = request.form['pettype']
    petdesc = request.form['petdesc']
    petskill1 = request.form.get('skill1')
    petskill2 = request.form.get('skill2')
    petskill3 = request.form.get('skill3')
    data = {
        "petname": petname,
        "pettype": pettype,
        "petdesc": petdesc,
        "petskill1": petskill1,
        "petskill2": petskill2,
        "petskill3": petskill3
    }
    Pet.new_pet(data)
    return redirect("/")

@app.route("/profile/<id>")
def profile(id):
    data = {
        "id": int(id)
    }
    pet = Pet.get_one(data)
    if not pet:
        return redirect("/")
    return render_template("profile.html", pet=pet)

if __name__ == "__main__":
    app.run(debug=True)
