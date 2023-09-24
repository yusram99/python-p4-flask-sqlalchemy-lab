# app.py

from flask import Flask, render_template, make_response
from flask_migrate import Migrate
from models import db, Animal, Zookeeper, Enclosure

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    response = make_response('<h1>Zoo app</h1>', 200)
    return response

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)

    if animal is None:
        return 'Animal not found', 404

    return render_template('animal.html', animal=animal)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)

    if zookeeper is None:
        return 'Zookeeper not found', 404

    return render_template('zookeeper.html', zookeeper=zookeeper)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)

    if enclosure is None:
        return 'Enclosure not found', 404

    return render_template('enclosure.html', enclosure=enclosure)

if __name__ == '__main__':
    app.run(port=5553, debug=True)
