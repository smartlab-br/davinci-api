"""API Base """
import os
from flask import Flask
from flask import g
from flask_cors import CORS
from flask_restful_swagger_2 import Api

from service.request_handler import FLPORequestHandler

from resources.v1.municipio import MunicipiosResource, MunicipioResource

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

@application.teardown_appcontext
def close_db_connection(error):
    ''' Cleanup on application crash '''
    # # Encerra a conexão com o hive
    # if hasattr(g, 'hive_connection'):
    #     g.hive_connection.close()
    #     g.hive_connection = None
    # # Encerra a conexão com o impala
    # if hasattr(g, 'impala_connection'):
    #     g.impala_connection.close()
    #     g.impala_connection = None
    # # Encerra a conexão com o impala
    # if hasattr(g, 'hbase_connection'):
    #     g.hbase_connection.close()
    #     g.hbase_connection = None

CORS = CORS(application, resources={r"/*": {"origins": "*"}})
api = Api(application, api_version='0.1', api_spec_url='/api/swagger') #pylint: disable=C0103

api.add_resource(HCAlive, '/hcalive')

api.add_resource(MunicipiosResource, '/municipios')
api.add_resource(MunicipioResource, '/municipio/<int:cd_municipio_ibge>')

# Endpoints de modelos de Machine Learning
api.add_resource(ClassificacaoResource, '/ml/classificacao/<string:model_id>')

if __name__ == '__main__':
    application.run(request_handler=FLPORequestHandler)
