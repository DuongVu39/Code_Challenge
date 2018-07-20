import numpy as np
from keras.models import Sequential
from keras.layers import BatchNormalization
from keras.layers.core import Dense, Dropout

def keras_model(n_layers, activation, n_feats, dropout_rate=0.2,
                loss="categorical_crossentropy"):  # Tested [N]
    """
    Creates and compiles a fully-connected feed forward neural network model using Keras

    Args:
        n_layers (int): Number of hidden layers to include in the network.
        activation (list or str): Activation functions to use at each layer.
                                If a string is supplied, that activation will be used at each layer
                                except for the output layer, which will always use softmax.
        n_feats (int): Number of features in the input data. Required to set input_shape
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
            model.add(Dropout(dropout))
        model.add(Dense(64, activation='relu'))
        
    model.add(Dropout(dropout))        
    
    model.add(Dense(2, activation='softmax'))
    model.compile(optimizer='adam', 
                  loss=loss, 
                  metrics=['accuracy'])

    return models