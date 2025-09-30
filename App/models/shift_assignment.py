from App.database import db
from App.models import Staff, Admin, Shift

class ShiftAssignment(db.Model):
    shiftAssignmentID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'), nullable=False)
    shiftID = db.Column(db.Integer, db.ForeignKey('shift.shiftID'), nullable=False)
    timeIn = db.Column(db.DateTime, nullable=True)
    timeOut = db.Column(db.DateTime, nullable=True)

    staff = db.relationship('Staff', backref=db.backref('shift_assignments', lazy=True))
    shift = db.relationship('Shift', backref=db.backref('shift_assignments', lazy=True))

    def __init__(self, staffID, shiftID):
        self.staffID = staffID
        self.shiftID = shiftID
        self.timeIn = None
        self.timeOut = None 