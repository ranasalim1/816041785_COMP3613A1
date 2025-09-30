from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role= db.Column(db.String(20), nullable=False)

    def __init__(self, username, firstName, lastName, password, role):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.set_password(password)
        self.role = role

    def get_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "role": self.role
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

