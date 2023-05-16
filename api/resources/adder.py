from flask_restful import Resource
from flask import request, abort
from marshmallow import exceptions
from services.evaluators import Adder as adder_service
from schemas.schemas import EvaluatorSchema


class Adder(Resource):
    def get(self):
        return {"test": "hello world"}
        
    def post(self):
        raw_input_data = request.get_json()
        try:
            input_data = EvaluatorSchema().load(raw_input_data)
        except exceptions.ValidationError as e:
            abort(400, str(e))

        result = adder_service.execute(input_data)
        return result

