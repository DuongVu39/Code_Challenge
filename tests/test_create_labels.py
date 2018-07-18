import pytest
import numpy as np
import pandas as pd
from src.task1.create_labels import create_labels

dat = pd.read_csv("data/data_for_test.csv")

class TestClass:

    def test_df_out_size(self):
        """ Tests that the output of create_labels() has the correct size."""
        df_out = create_labels(dat, time_range=4)

        assert df_out.shape[1] == dat.shape[1]+1, "Error, the produced DataFrame is not the correct size"

