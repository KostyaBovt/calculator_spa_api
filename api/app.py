from flask import Flask
from flask_restful import Resource, Api
from marshmallow import Schema, fields
from flask_cors import CORS

from resources.adder import Adder
from resources.reducer import Reducer
from resources.multiplier import Multiplier
from resources.divider import Divider

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Adder, '/add')
api.add_resource(Reducer, '/reduce')
api.add_resource(Multiplier, '/multiply')
api.add_resource(Divider, '/divide')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')