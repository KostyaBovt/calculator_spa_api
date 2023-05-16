from flask_restful import Resource
from flask import request, abort
from marshmallow import exceptions
from services.evaluators import Divider as devider_service
from schemas.schemas import EvaluatorSchema


class Divider(Resource):
    def post(self):
        raw_input_data = request.get_json()
        try:
            input_data = EvaluatorSchema().load(raw_input_data)
        except exceptions.ValidationError as e:
            abort(400, str(e))

        result = devider_service.execute(input_data)
        return result

