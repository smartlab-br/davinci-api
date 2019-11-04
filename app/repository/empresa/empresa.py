''' Repository para recuperar informações de uma empresa '''
from repository.base import HBaseRepository
# import pandas as pd

#pylint: disable=R0903
class EmpresaRepository(HBaseRepository):
    ''' Definição do repo '''
    TABLE = 'sue'
    CNPJ_COLUMNS = {} # Dados que possuem nomes diferentes para a coluna de cnpj

    def find_datasets(self, cnpj_raiz, column_family, column, cnpj=None):
        ''' Localiza um município pelo código do IBGE '''
        if cnpj_raiz is not None:
            # return self.find_row(self.TABLE, cnpj_raiz)
            result = self.find_row('test', cnpj_raiz, column_family, column)

            for ds_key in result:
                # Filtrar cnpj nos datasets pandas
                if cnpj is not None:
                    col_name = 'cnpj'
                    if ds_key in self.CNPJ_COLUMNS:
                        col_name = self.CNPJ_COLUMNS[ds_key]
                    result[ds_key] = result[ds_key][result[ds_key][col_name] == cnpj]

                # Conversão dos datasets em json
                result[ds_key] = result[ds_key].to_json(orient="records")

            return result
