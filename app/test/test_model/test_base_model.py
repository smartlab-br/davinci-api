'''Main tests in API'''
import unittest
from test.stubs.constants import COMMON_OPTIONS, SAMPLE_DATAFRAME, COMMON_EXPECTED_RESPONSE_STRING
from model.base import BaseModel

class BaseModelTest(unittest.TestCase):
    ''' Classe que testa a obtenção de dados de acordo com os parâmetros
        dados. '''
    def test_wrapping(self):
        ''' Verifica se retorna o dataset apenas com o wrapping '''
        model = BaseModel()

        options = {
            **{
                "categorias": [
                    'nm_indicador', 'nu_competencia', 'vl_indicador', 'lat_mun', 'long_mun'
                ],
                "pivot": None
            }, **COMMON_OPTIONS
        }

        result = "".join(model.wrap_result(SAMPLE_DATAFRAME.copy(), options).split())

        str_expected = COMMON_EXPECTED_RESPONSE_STRING.format(
            """
                "nm_indicador": "Ficticio",
                "nu_competencia": 2099,
                "vl_indicador": 1.0
            },
            {
                "nm_indicador": "Ficticio",
                "nu_competencia": 2047,
                "vl_indicador": 0.5
            """
        )
        expected = "".join(str_expected.split())

        self.assertEqual(result, expected)

    def test_wrapping_as_pandas(self):
        ''' Verifica se retorna o dataset com o wrapping como pandas '''
        model = BaseModel()

        options = {
            **{
                "categorias": [
                    'nm_indicador', 'nu_competencia', 'vl_indicador', 'lat_mun', 'long_mun'
                ],
                "pivot": None
            }, **COMMON_OPTIONS
        }

        result = "".join(model.wrap_result(SAMPLE_DATAFRAME.copy(), options).split())

        str_expected = COMMON_EXPECTED_RESPONSE_STRING.format(
            """
                "nm_indicador": "Ficticio",
                "nu_competencia": 2099,
                "vl_indicador": 1.0
            },
            {
                "nm_indicador": "Ficticio",
                "nu_competencia": 2047,
                "vl_indicador": 0.5
            """
        )
        expected = "".join(str_expected.split())

        self.assertEqual(result, expected)

    def test_wrapping_as_dict(self):
        ''' Verifica se retorna o dataset com o wrapping como dicionario '''
        model = BaseModel()

        options = {
            **{
                "categorias": [
                    'nm_indicador', 'nu_competencia', 'vl_indicador', 'lat_mun', 'long_mun'
                ],
                "pivot": None
            }, **COMMON_OPTIONS
        }

        result = "".join(model.wrap_result(SAMPLE_DATAFRAME.copy(), options).split())

        str_expected = COMMON_EXPECTED_RESPONSE_STRING.format(
            """
                "nm_indicador": "Ficticio",
                "nu_competencia": 2099,
                "vl_indicador": 1.0
            },
            {
                "nm_indicador": "Ficticio",
                "nu_competencia": 2047,
                "vl_indicador": 0.5
            """
        )
        expected = "".join(str_expected.split())

        self.assertEqual(result, expected)
