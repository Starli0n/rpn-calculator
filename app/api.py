import logging

from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from blueprint import autoregister

logging.basicConfig(level=logging.INFO)


app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "RPN Calculator"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

api_cors_config = {
    "origins": ["*"],
    "methods": ["GET", "POST", "PUT", "DELETE"]
}
CORS(app, resources={r"/api/*": api_cors_config})

app.config['OPERAND'] = [ '+', '-', '*', '/' ]
app.config['STACKS'] = {}
app.config['STACKID'] = 0

logging.info('--- Starting RPN Calculator server ---')
autoregister.blueprint(app, sub_dir='api')

@app.route('/')
def welcome():

    return 'Welcome to RPN Calculator Api'
