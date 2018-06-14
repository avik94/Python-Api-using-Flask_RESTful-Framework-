from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, reqparse
import time
from app.helper.blankstring import catchEmptyString

from model.employeeModel import employeeModel
from model.employeeSportsModel import Employeesports
from app import db


class Sports(Resource):
    def get(self):
        return{"msg":"Data is comming! "}


    def post(self):
        try:
            parser = reqparse.RequestParser(bundle_errors= True)

            parser.add_argument("sportName", required= True, type= str)
            parser.add_argument("employeeId", required= True, type= int)

            args = parser.parse_args()

            blank_string_checking=[args["sportName"]]

            msg=["Sport Name"]

            messages=catchEmptyString(blank_string_checking,msg)

            if messages:
                return messages
            else:
                createdAt = int(time.time())
                                                   
                data = Employeesports(sportName=args["sportName"],\
                    employeeId=args["employeeId"],\
                    createdAt=createdAt)

                db.session.add(data)
                db.session.commit()

                return {"message":"Data saved succesfully"}


        except Exception:
            return {"message": "Failed to decode JSON object: Expecting value: \
             line 1 column 1 (char 0)"}
