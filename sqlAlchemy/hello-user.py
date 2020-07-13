from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
file = open(r'C:\Users\luvku\Documents\credentials.txt')
line = file.read()
app.config['SQLALCHEMY_DATABASE_URI'] = line 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  identity = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Person ID: {self.identity}, name: {self.name}>'

db.create_all()

@app.route('/')
def index():
  person = Person.query.first()
  return 'Hello ' + person.name

if __name__ == '__main__':
  app.run(debug=True )