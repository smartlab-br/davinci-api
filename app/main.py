"""API Base """
import os
from flask import Flask
from flask import g
from flask_cors import CORS
from flask_restful_swagger_2 import Api

from service.request_handler import FLPORequestHandler

from resources.v1.municipio import MunicipiosResource, MunicipioResource

from resources.v1.mlmodel.supervisionado.classificacao import ClassificacaoResource

# from resources.v1.empresa.empresa import EmpresaResource
# from resources.v1.empresa.estabelecimento import EstabelecimentoResource

# from resources.v1.indicadores.indicadores_municipais \
#     import IndicadoresMunicipaisResource, IndicadoresMunicipaisChartResource
# from resources.v1.indicadores.indicadores_estaduais \
#     import IndicadoresEstaduaisResource
# from resources.v1.indicadores.indicadores_microrregionais \
#     import IndicadoresMicrorregionaisResource
# from resources.v1.indicadores.indicadores_mesorregionais \
#     import IndicadoresMesorregionaisResource
# from resources.v1.indicadores.indicadores_regionais \
#     import IndicadoresRegionaisResource
# from resources.v1.indicadores.indicadores_nacionais \
#     import IndicadoresNacionaisResource
# from resources.v1.indicadores.indicadores_mpt_unidades \
#     import IndicadoresMptUnidadesResource

# # Endpoints temáticos de Saúde e Segurança
# from resources.v1.sst.beneficio import BeneficiosResource
# from resources.v1.sst.cat import CatsResource, CatsOpResource

# # Endpoints temáticos de Trabalho Escravo
# from resources.v1.te.incidencia import IncidenciaEscravoResource
# from resources.v1.te.operacoes import OperacoesEscravoResource
# from resources.v1.te.migracoes import MigracoesEscravoResource
# from resources.v1.te.migracoes_sankey import MigracoesSankeyEscravoResource

# # Endpoints temáticos do Trabalho Infantil
# # Endpoints do Mapear - Trabalho Infantil
# from resources.v1.ti.mapear import MapearInfantilResource
# # Endpoints da Prova Brasil - Trabalho Infantil
# from resources.v1.ti.prova_brasil import ProvaBrasilInfantilResource
# # Endpoints do Censo Agro
# from resources.v1.ti.censo_agro import CensoAgroMunicipiosResource
# from resources.v1.ti.censo_agro_uf import CensoAgroEstadosResource
# from resources.v1.ti.censo_agro_br import CensoAgroBrasilResource
# # Endpoints das organizações assistência social
# from resources.v1.orgs.orgs_assistencia_social import OrgsAssistenciaSocialResource

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

# # Endpoints para obter datasets de empresa e estabelecimento
# api.add_resource(EmpresaResource, '/empresa/<string:cnpj_raiz>')
# api.add_resource(EstabelecimentoResource, '/estabelecimento/<string:cnpj>')

# # Endpoints de buscas por datasets de indicadores
# api.add_resource(IndicadoresMunicipaisResource, '/indicadores/municipais')
# api.add_resource(IndicadoresEstaduaisResource, '/indicadores/estaduais')
# api.add_resource(IndicadoresMicrorregionaisResource, '/indicadores/microrregionais')
# api.add_resource(IndicadoresMesorregionaisResource, '/indicadores/mesorregionais')
# api.add_resource(IndicadoresRegionaisResource, '/indicadores/regionais')
# api.add_resource(IndicadoresNacionaisResource, '/indicadores/nacionais')
# api.add_resource(IndicadoresMptUnidadesResource, '/indicadores/mptunidades')

# ## Endpoints temáticos
# # Saúde e Segurança no Trabalho
# api.add_resource(CatsResource, '/sst/cats')
# api.add_resource(CatsOpResource, '/sst/cats/<string:operation>')
# api.add_resource(BeneficiosResource, '/sst/beneficios')

# # Trabalho Escravo
# api.add_resource(IncidenciaEscravoResource, '/te/incidencia')
# api.add_resource(MigracoesEscravoResource, '/te/migracoes')
# api.add_resource(MigracoesSankeyEscravoResource, '/te/migracoes/sankey')
# api.add_resource(OperacoesEscravoResource, '/te/operacoes')

# # Trabalho Infantil
# api.add_resource(MapearInfantilResource, '/ti/mapear')
# api.add_resource(ProvaBrasilInfantilResource, '/ti/provabrasil')
# api.add_resource(CensoAgroMunicipiosResource, '/ti/censoagromunicipal')
# api.add_resource(CensoAgroEstadosResource, '/ti/censoagroestadual')
# api.add_resource(CensoAgroBrasilResource, '/ti/censoagronacional')

# # Organizações de Assistência social
# api.add_resource(OrgsAssistenciaSocialResource, '/orgs/assistenciasocial')

# # Endpoint de obtenção de gráficos de indicadores
# api.add_resource(IndicadoresMunicipaisChartResource, '/charts/indicadoresmunicipais')

if __name__ == '__main__':
    application.run(request_handler=FLPORequestHandler)
