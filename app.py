"""Flask application for animal shelter"""

# flask app imports
from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
# models.py imports:
from models import db, connect_db, Pet
# forms.py imports:
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "shhh1234567"

# database import
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///animalshelter"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

toolbar = DebugToolbarExtension(app)

# Create the tables within the app context
with app.app_context():
    db.create_all()

# ..................................................................................................
# website routes

@app.route("/")
def pet_list():
    "Homepage of list of all pets at shelter"
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('pet_list'))

    else:
        # re-present form for editing
        return render_template("pet_add_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('pet_list'))

    else:
        # failed; re-present form for editing
        return render_template("pet_edit_form.html", form=form, pet=pet)


@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}
    
    return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True)
