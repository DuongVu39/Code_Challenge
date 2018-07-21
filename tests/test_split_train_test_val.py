import pytest
import numpy as np
import pandas as pd
from src.task2.split_train_test_val import split_train_test_val

dat = pd.read_csv("data/data_for_test.csv")

class TestClass:
    
    def test_output(self):
    """ Tests that the output of split_train_test_val() contains 6 elements"""
    
        list_out = split_train_test_val(dat)

        assert len(list_out) == 6, "Error, missing one result set"

    