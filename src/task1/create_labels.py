import numpy as np
import pandas s pd


def create_labels(df, range=40):  # Tested [Y]

    """
    Create labels with a time lapse

    Args:
        df (dataframe): The dataframe that needs to create label
        range (int): Default=40. After this range, check the wind turbin performance.

    Returns:
        df (dataframe): Original one with a label column with 2 values:
                        1 - Wind turbin break down after the time range
                        0 - Wind turbin still fine
    """
    # Order the dataframe chronologically
    df["time"] = pd.to_datetime(df["time_stamp"]).dt.date
    wind_turbin = df.sort_values("time")
    
    # Refactor the time_stamp column to datetime object
    wind_turbin["time_stamp"] = pd.to_datetime(wind_turbin["time_stamp"])
    
    # Reset index
    wind_turbin = wind_turbin.reset_index().iloc[:,1:29]
    
    # Creating label:
    wind_turbin["status_shift"] = wind_turbin.groupby("unit_number")['status'].transform(lambda g: g.shift(periods=-range))
    wind_turbin['label'] = np.where(wind_turbin["status_shift"]==0.0, 0, 1)
    
    return wind_turbin
    
