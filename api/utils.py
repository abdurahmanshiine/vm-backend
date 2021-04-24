import json
from api.data import Data

def prepareResponse(__id, quantity):
    item = [item for item in Data.items if item['__id'] == __id][0]
    response = json.dumps({'message':'Operation successful', 'Dispensed': f"{item['name']}", 'quantity': quantity, 'Total price': item['price'] * quantity})

    return response