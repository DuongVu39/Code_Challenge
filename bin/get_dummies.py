import pandas as pd
import numpy as np

# Do I want to pass a list or do I want to pass only a string or both?

def get_dummies(df):  # Tested [P]

    """
    Transform categorical variable to dummies and select one less level to prevent colinearity 

    Args:
        df (dataframe): Original dataframe 
        col_name(str): Name of column to be transformed
        
    Returns:
        df (dataframe): New dataframe with no categorical feature.
    """
    
    if isinstance(col_name, list):  # Branch A
        for i in col_name:
            
    
    else:  # Branch B
    num_level = len(set(df[col_name]))
    
    # Excluding one level to prevent colinearity
    new_level = pd.get_dummies(df[col_name]).iloc[:,0:(num_level-1)]
    
    
    return df