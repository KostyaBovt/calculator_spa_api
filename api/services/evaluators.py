from flask_restful import Resource
from flask import request, abort
from marshmallow import exceptions


class Adder():
    @staticmethod
    def execute(input_data):
        return input_data["arg_1"] + input_data["arg_2"]

class Reducer():
    @staticmethod
    def execute(input_data):
        return input_data["arg_1"] - input_data["arg_2"]

class Multiplier():
    @staticmethod
    def execute(input_data):
        return input_data["arg_1"] * input_data["arg_2"]

class Divider():
    @staticmethod
    def execute(input_data):
        return input_data["arg_1"] / input_data["arg_2"]
