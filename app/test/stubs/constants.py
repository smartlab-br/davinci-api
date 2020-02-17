''' Constants used in stub classes '''
from io import StringIO
import pandas as pd

COMMON_EXPECTED_RESPONSE_STRING = """{{
    "metadata": {{}},
    "dataset": [{{{0}}}]
    }}"""

COMMON_OPTIONS = {
    "valor": ['vl_indicador'],
    "agregacao": ['sum'],
    "ordenacao": ['-nm_indicador'],
    "where": ['eq-nu_competencia-2010'],
    "joined": None,
}

STR_DATASET = StringIO(
    """nm_indicador;nu_competencia;vl_indicador
        Ficticio;2099;1
        Ficticio;2047;0.5
        """
)
SAMPLE_DATAFRAME = pd.read_csv(STR_DATASET, sep=";")
