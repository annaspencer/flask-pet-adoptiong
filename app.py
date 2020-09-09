from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pet
from forms import PetForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "252-495-152"
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

@app.route('/form/new')
def add_pet():
    form = PetForm()
    return render_template("pet-form.html", form=form)