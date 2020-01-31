"""API Base """
import os
from flask import Flask
from flask import g
from flask_cors import CORS
from flask_restful_swagger_2 import Api

from service.request_handler import FLPORequestHandler

from resources.v1.mlmodel.supervisionado.classificacao import ClassificacaoResource

from resources.v1.healthchecks import HCAlive

config = {
    "dev": "config.dev.DevelopmentConfig",
    "prod": "config.prod.ProductionConfig",
    "staging": "config.staging.StagingConfig",
}

application = Flask(__name__, static_folder='static', static_url_path='') #pylint: disable=C0103
config_name = os.getenv('FLASK_CONFIGURATION', 'dev')
application.config.from_object(config[config_name])

CORS = CORS(application, resources={r"/*": {"origins": "*"}})
api = Api(application, api_version='0.1', api_spec_url='/api/swagger') #pylint: disable=C0103

api.add_resource(HCAlive, '/hcalive')

# Endpoints de modelos de Machine Learning
api.add_resource(ClassificacaoResource, '/ml/classificacao/<string:model_id>')

if __name__ == '__main__':
    application.run(request_handler=FLPORequestHandler)
