import os
from flask import Flask
import api.routes as routes
from api.config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)

app.add_url_rule('/items', view_func=routes.get_items)
app.add_url_rule('/item:<int:__id>', view_func=routes.get_item)
app.add_url_rule('/vend', view_func=routes.vend_item, methods=['POST'])

if __name__ == '__main__':
    if os.environ.get("FLASK_ENV") == "Development":
        app.run(port=DevelopmentConfig.PORT, debug=DevelopmentConfig.DEBUG, host='0.0.0.0')
    elif os.environ.get("FLASK_ENV") == "Production":
        app.run(port=ProductionConfig.PORT, debug=ProductionConfig.DEBUG, host='0.0.0.0')
    else:
        print('No FLASK_ENV specified')