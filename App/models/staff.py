from App.database import db
from App.models import User, Shift
from datetime import datetime, timedelta    

class Staff(User):

    staffID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __init__(self, username, firstName, lastName, password):
        super().__init__(username, firstName, lastName, password, role="Staff")

    def view_combined_roster(self):
        pass

    def time_in(self, shiftID):
        from App.models.shift_assignment import ShiftAssignment

        assignment = self.assignments.filter_by(shiftID=shiftID).first()
        if not assignment:
            return None

        assignment.timeIn = datetime.now()
        db.session.commit()
        return assignment

    def time_out(self, shiftID):
        from App.models.shift_assignment import ShiftAssignment

        assignment = self.assignments.filter_by(shiftID=shiftID).first()
        if not assignment:
            return None

        assignment.timeOut = datetime.now()
        db.session.commit()
        return assignment
