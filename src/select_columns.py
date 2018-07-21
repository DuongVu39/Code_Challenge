import pandas as pd
import numpy as np

def select_columns(df, col_names):  # Tested [N]

    """
    Select only the columns that appears in the train set

    Args:
        df (dataframe): Test dataframe 
        col_names (list): List of all desired column names.

    Returns:
        df (dataframe): Original dataframe with only selected columns
    """
    
    # Test if all given column are in the dataframe:
    if set(col_names).issubset(list(df.columns.values)):  # Branch A
        df_new = df[col_names]
        
    else:  # Branch B
        new_col_names = [col for col in col_names if col in list(df.columns.values)]
        df_new = df[new_col_names]
    
    return df_new