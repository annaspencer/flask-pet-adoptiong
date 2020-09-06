"""Seed file to make test pets"""

from models import Pet db
from app import app

#create all tables
db.drop_all()
db.create_all()

#If table isn't empty, then empty it
Pet.query.delete()


#add users

bp = Pet(name="BP", species="Cat", image_url="https://unsplash.com/photos/B4GLLQVIdLQ", available=True)
buddy = Pet(name="Buddy", species="Cat", image_url="https://unsplash.com/photos/B4GLLQVIdLQ", available=True)
sparky = Pet(name="Sparky", species="Dog", image_url="https://unsplash.com/photos/B4GLLQVIdLQ", available=True)
rainbow= Pet(name="Rainbow", species="Fish", image_url="https://unsplash.com/photos/B4GLLQVIdLQ", available=True)


#add to db
db.session.add(bp)
db.session.add(buddy)
db.session.add(sparky)
db.session.add(rainbow)

db.session.commit()
