from marshmallow import Schema, fields, validate

class EvaluatorSchema(Schema):
    arg_1 = fields.Int(required=True)
    arg_2 = fields.Int(required=True)
