'''Main tests in API'''
import unittest
import numpy as np
import pandas as pd
from model.base import BaseModel

SAMPLE_DATAFRAME = pd.DataFrame.from_dict(
    {
        'col_1': ['d', 'b', 'a', 'c'],
        'col_2': [3, 2, 1, 0],
        'col_3': [3, 2, 1, 0]
    }
)
SAMPLE_DATAFRAME_NA = pd.DataFrame.from_dict(
    {
        'col_1': ['d', 'b', 'a', 'c'],
        'col_2': [3, 2, 1, None],
        'col_3': [3, 2, 1, None]
    }
)
SAMPLE_DATAFRAME_REAL = pd.DataFrame.from_dict(
    {
        'col_1': ['d', 'b', 'a', 'c'],
        'col_2': [3000.3, 2000.2, 1000.1, 0.0],
        'col_3': [3000.3, 2000.2, 1000.1, 0.0],
        'col_4': [3000.3, 2000.2, 1000.1, 0.0],
        'col_5': [3000.3, 2000.2, 1000.1, None]
    }
)
