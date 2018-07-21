import pytest
import numpy as np
import pandas as pd
from src.keras_model import keras_model

dat = pd.read_csv("data/data_for_test.csv")

class TestClass:

    def test_output(self):
    """ Tests that the output of keras_model() is a NN model"""
    
        pass 