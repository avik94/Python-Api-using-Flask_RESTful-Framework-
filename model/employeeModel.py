from app import db

class employeeModel(db.Model):
    __tablename__ = "employee_details"

    employeeId = db.Column(db.Integer, primary_key= True, nullable=False)
    employeeName = db.Column(db.String(10), nullable=False)
    phoneNo = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(20), nullable=False)
    createdAt = db.Column(db.Integer, nullable=False)
    updatedAt = db.Column(db.Integer, default=0)
    employeeSports = db.relationship('Employeesports', backref='employee')
        # backref=db.backref('employee', lazy=True))
