from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure DB connection String
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create DB Engine
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, Name: {self.name}>'


db.create_all()

@app.route("/")
def index():
    person = Person.query.first()
    return f"Hello, {person.name}!"


if __name__ == "__main__":
    app.run(debug=1)
