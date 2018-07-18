import numpy as np
import pandas s pd


def create_labels(df, time_range=40):  # Tested [Y]

    """
    Create labels with a time lapse

    Args:
        df (dataframe): The dataframe that needs to create label
        range (int): Default=40. After this range, check the wind turbine performance.

    Returns:
        df (dataframe): Original one with a label column with 2 values:
                        1 - Wind turbine break down within the time range
                        0 - Wind turbine still fine
    """
    # Order the dataframe chronologically
    df["time"] = pd.to_datetime(df["time_stamp"]).dt.date
    wind_turbine = df.sort_values("time")
    
    # Refactor the time_stamp column to datetime object
    wind_turbine["time_stamp"] = pd.to_datetime(wind_turbine["time_stamp"])
    
    # Reset index
    wind_turbine = wind_turbine.reset_index().iloc[:,1:29]
    
    # Creating label:
    for i in range(1,time_range+1):
        wind_turbine["status_shift"] = wind_turbine.groupby("unit_number")['status'].transform(lambda g: g.shift(periods=-i))
        wind_turbine['mark'] = 0 # default value
        wind_turbine['mark'] = wind_turbine['mark'] + np.where(wind_turbine["status_shift"]==0.0, 0, 1)
    
    wind_turbine['label'] = np.where(wind_turbine["mark"]==0.0, 0, 1)
    final_col = [ i for i in wind_turbine.columns if i not in ['mark', 'status_shift']]
    return wind_turbine[final_col]
    
