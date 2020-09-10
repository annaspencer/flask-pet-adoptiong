from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pet
from forms import PetForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "105-919-298"
# debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug =True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def home():
    """Home page for all pets table"""
     pet = Pet.query.all()
     return render_template('/index.html', pet=pet)

@app.route('/form/new', methods=["GET","POST"])
def add_pet():
    """routes for add a pet form"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        image_url = form.image_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, image_url=image_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    
    else:
        return render_template("pet-form.html", form=form)

@app.route("/<int:id>/edit", methods=['GET', 'POST'])
def edit_pet(id):
    """routes for pet details and edit page"""
    pet = Pet.query.get_or_404(id)

    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.image_url = form.image_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)



