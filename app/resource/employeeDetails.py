from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, reqparse
import time
from app.helper.blankstring import catchEmptyString
from model.employeeModel import employeeModel
from app import db


resource_field= {
    "employeeId": fields.Integer,
    "employeeName": fields.String,
    "phoneNo": fields.Integer,
    "salary": fields.Integer,
    "address": fields.String,
    "createdAt": fields.Integer,
    "updatedAt": fields.Integer
}


class Employee(Resource):
    @marshal_with(resource_field, envelope="data")
    def get(self):
        data = employeeModel.query.all()
        return data

    def post(self):

        parser = reqparse.RequestParser(bundle_errors= True)

        parser.add_argument("employeeName", required= True, type= str)
        parser.add_argument("phoneNo", required= True, type= int)
        parser.add_argument("salary", required= True, type= int)
        parser.add_argument("address", required= True, type= str)
        try:
            args = parser.parse_args()

            blank_string_checking=[args["employeeName"], args["address"]]

            print(blank_string_checking)

            msg=["Employee Name","Address"]

            messages=catchEmptyString(blank_string_checking,msg)

            if messages:
                return messages
            else:
                CreatedAt = int(time.time())

                data = employeeModel(employeeName=args["employeeName"],\
                    phoneNo=args["phoneNo"],\
                    salary=args["salary"],\
                    address=args["address"],\
                    createdAt=CreatedAt)
                db.session.add(data)
                db.session.commit()
                return {"message":"Data saved succesfully"}

        except Exception:
            return {"message": "Failed to decode JSON object: Expecting value: \
             line 1 column 1 (char 0)"}
