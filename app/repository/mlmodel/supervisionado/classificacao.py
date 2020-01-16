''' Repository para recuperar modelos de Machine Learning '''
from repository.base import MLModelsRepository

#pylint: disable=R0903
class ClassificacaoRepository(MLModelsRepository):
    ''' Definição do repo '''
    TIPO = 'classificacao'
