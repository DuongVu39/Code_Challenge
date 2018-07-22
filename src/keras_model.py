import numpy as np
from keras.models import Sequential
from keras.layers import BatchNormalization
from keras.layers.core import Dense, Dropout

def keras_model(n_layers=1, n_feats=25, dropout_rate=0.2,
                loss="mean_squared_error"):  # Tested [N]
    """
    Creates and compiles a fully-connected feed forward neural network model using Keras

    Args:
        n_layers (int): Default=1. Number of hidden layers to include in the network.
        n_feats (int): Default=25. Number of features in the input data. Required to set input_shape
        dropout_rate (int): Default=0.2. Determines dropout rate for dropout layer.
        loss (str): Loss function to use when compiling the model.
                    Will be used by the optimizer during training to determine fit
        
    Returns:
        (keras.model) Compiled model containing the desired Dense layers.
                      After this, just needs to be fit with training/test data
    """
    
    model = Sequential()
    model.add(BatchNormalization())
    model.add(Dense(64, activation='relu', input_shape = (n_feats,)))
    
    for i in range(1, n_layers):  # Add each of the desired layers
        if i % 3 == 0:
            model.add(Dropout(dropout_rate))
        model.add(Dense(64, activation='relu'))
        
    model.add(Dropout(dropout_rate))        
    
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', 
                  loss=loss, 
                  metrics=['accuracy'])

    return model