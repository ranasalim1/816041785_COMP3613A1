from App.database import db
from App.models import Staff, Admin, Shift  

class Roster(db.Model):
    rosterID = db.Column(db.Integer, primary_key=True)
    weekStartDate = db.Column(db.Date, nullable=False)
    shiftAssignments = db.relationship('ShiftAssignment', backref='roster', lazy=True)
    

    def __init__(self, weekStartDate):
        self.weekStartDate = weekStartDate