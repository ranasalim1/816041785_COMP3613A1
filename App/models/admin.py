from App.database import db
from App.models import User, Shift, Staff

class Admin(User):

    adminID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __init__(self, username, firstName, lastName, password):
        super().__init__(username, firstName, lastName, password, role="Admin")

    def schedule_shift(self, staffID, shiftID):
        from App.models.shift_assignment import ShiftAssignment

        staff = Staff.query.get(staffID)
        shift = Shift.query.get(shiftID)

        if not staff:
            print(f"No staff found with ID {staffID}")
            return None
        
        if not shift:
            print(f"No shift found with ID {shiftID}")
            return None

        assignment = ShiftAssignment(staffID=staffID, shiftID=shiftID)
        db.session.add(assignment)
        db.session.commit()
        return assignment
    

    def view_report(self, week):
        from App.models.shift_assignment import ShiftAssignment

        report = (ShiftAssignment.query
                  .join(Shift, ShiftAssignment.shiftID == Shift.id)
                  .filter(db.extract('week', Shift.date) == week)
                  .filter(ShiftAssignment.timeIn.isnot(None))
                  .filter(ShiftAssignment.timeOut.isnot(None))
                  .all())

        return report

    