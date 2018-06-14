from app import db

class Employeesports(db.Model):
    __tablename__ = 'employee_sports'

    sportId = db.Column(db.Integer, primary_key=True)
    sportName = db.Column(db.String(20), nullable=False)
    employeeId = db.Column(db.Integer, db.ForeignKey(\
        'employee_details.employeeId'), nullable=False)
    createdAt = db.Column(db.Integer, nullable=False)
    updatedAt = db.Column(db.Integer, default=0,nullable=False)
