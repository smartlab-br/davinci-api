''' Controller para fornecer dados das organizações de assistência social '''
from flask import request
from flask_restful_swagger_2 import swagger
from resources.base import BaseResource
from model.empresa.empresa import Empresa

class EmpresaResource(BaseResource):
    ''' Classe de múltiplas incidências '''
    def __init__(self):
        ''' Construtor'''
        self.domain = Empresa()

    @swagger.doc({
        'tags':['empresa'],
        'description':'Obtém todos os registros de uma única empresa',
        'parameters':[
            {
                "name": "cnpj_raiz",
                "description": "CNPJ Razi da empresa consultada",
                "required": True,
                "type": 'string',
                "in": "path"
            }
        ],
        'responses': {
            '200': {
                'description': 'Todos os datasets da empresa'
            }
        }
    })
    def get(self, cnpj_raiz):
        ''' Obtém todos os datasets da empresa '''
        column_family = None
        if 'dados' in request.args:
            column_family = request.args['dados']
        column = None
        if 'competencia' in request.args:
            column = request.args['competencia']
        return self.__get_domain().find_datasets(cnpj_raiz, column_family, column)

    def __get_domain(self):
        ''' Carrega o modelo de domínio, se não o encontrar '''
        if self.domain is None:
            self.domain = Empresa()
        return self.domain
