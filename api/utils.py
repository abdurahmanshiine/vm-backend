import json
from api.data import Data

def prepareResponse(__id, quantity, message, command):
    item = [item for item in Data.items if item['__id'] == __id][0]
    response = json.dumps({'message': message, 'VM code': command, 'Dispensed': f"{item['name']}", 'quantity': quantity, 'Total price': item['price'] * quantity})

    return response

def removeSlot(item):
    filtered_item = {k:v for k,v in item.items() if k != 'slot'}

    return filtered_item

def getItemSlot(__id):
    slot = [item for item in Data.items if item['__id'] == __id][0]['slot']

    return slot