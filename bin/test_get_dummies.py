import pytest
import numpy as np
import pandas as pd
from src.get_dummies import get_dummies

dat = pd.read_csv("data/data_for_test.csv")

class TestClass:
    
    def test_output(self):
    """ Tests that the output of get_dummies() does not have any categorical variables."""
    
        df_out = get_dummies(dat, "level")

        assert 'object' in list(df_out), "Error, there are still categorical variable in the dataframe."
        
        
    