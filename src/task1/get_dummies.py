import pandas as pd
import numpy as np

def get_dummies(df, col_name):  # Tested [N]

    """
    Transform categorical variable to dummies and select one less level to prevent colinearity 

    Args:
        df (dataframe): Original dataframe 
        col_name(str): Name of column to be transformed
        
    Returns:
        df (dataframe): New dataframe with no categorical feature.
    """
    
    df[col_name] = pd.get_dummies(df[col_name]).iloc[:,0]
    
    return df