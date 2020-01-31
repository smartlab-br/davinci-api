''' Base Model '''
import json

#pylint: disable=R0903
class BaseModel():
    ''' Definição do repo '''
    METADATA = {}

    def wrap_result(self, dataset=None, options=None):
        ''' Adiciona metadados à resposta '''
        if dataset is None:
            return None
        if options is not None:
            if 'as_pandas' in options and options['as_pandas']:
                return {
                    "metadata": self.fetch_metadata(options),
                    "dataset": dataset
                }
            if 'as_dict' in options and options['as_dict']:
                return {
                    "metadata": self.fetch_metadata(options),
                    "dataset": dataset.to_dict('records')
                }
        return f'{{ \
            "metadata": {json.dumps(self.fetch_metadata(options))}, \
            "dataset": {dataset.to_json(orient="records")} \
            }}'

    def fetch_metadata(self, options):
        ''' Gets metadata to add to the response '''
        pass

    def get_repo(self):
        ''' Método abstrato para carregamento do repositório '''
        raise NotImplementedError("Models precisam implementar get_repo")
