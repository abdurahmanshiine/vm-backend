import json
from flask import Response, request
from api.data import Data
from api.middleware import dispenseItem
from api.utils import prepareResponse, removeSlot

# @app.route('/items', methods=['GET'])
def get_items():
    return Response(json.dumps([removeSlot(item) for item in Data.items]), status=200, mimetype='application/json')

# @app.route('/item:<int:__id>', methods=['GET'])
def get_item(__id):
    item = [item for item in [removeSlot(item) for item in Data.items] if item['__id'] == __id][0]
    return Response(json.dumps(item), status=200, mimetype='application/json')

# @app.route('/vend', methods=['POST'])
def vend_item():
    __id = request.json['__id']
    quantity = request.json['quantity']
    message, command = dispenseItem(__id, quantity)
    response = prepareResponse(__id, quantity, message, command)
    return Response(response, status=200, mimetype='application/json')
