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
     pet = Pet.query.all()
     return render_template('/index.html', pet=pet)

@app.route('/form/new', methods=["GET","POST"])
def add_pet():
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


