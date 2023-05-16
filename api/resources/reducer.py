from flask_restful import Resource
from flask import request, abort
from marshmallow import exceptions
from services.evaluators import Reducer as reducer_service
from schemas.schemas import EvaluatorSchema


class Reducer(Resource):
    def post(self):
        raw_input_data = request.get_json()
        try:
            input_data = EvaluatorSchema().load(raw_input_data)
        except exceptions.ValidationError as e:
            abort(400, str(e))

        result = reducer_service.execute(input_data)
        return result

