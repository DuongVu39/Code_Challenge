import pytest
import numpy as np
import pandas as pd
from src.select_column import select_column

dat = pd.read_csv("data/data_for_test.csv")
col_names = ["time"]
col_names_2 = ["animal", "time"]

class TestClass:

    def test_num_column_A(self):
    """ Tests branch A: the list of column is the subset of given dataset's column
    Check if the number of column output is correct """
    
    df_out = select_column(dat, col_name)
    
    assert df_out.shape[1] == len(col_names), "Error, the number of column should be the same as the given list"
        
    def test_num_column_B(self):
    """ Tests branch B: the list of column and the given dataset's column does not contain each other.
    Check if the number of column output is belong to the subset of  both """
    
    df_out = select_column(dat, col_names_2)
    
    new_col_names = [col for col in col_names_2} if col in list(dat.columns.values)]
    
    assert df_out.shape[1] == len(new_col_names), "Error, check the number of column in new dataset."
    