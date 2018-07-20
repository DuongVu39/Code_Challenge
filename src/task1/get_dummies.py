import pandas as pd
import numpy as np

def get_dummies(df):  # Tested [N]

    """
    Transform categorical variable to dummies and select one less level to prevent colinearity 

    Args:
        df (dataframe): Original dataframe 
        
    Returns:
        df (dataframe): New dataframe with no categorical feature.
    """
    
    df_new = pd.get_dummies(df).iloc[:,:-1]
    
    return df_new