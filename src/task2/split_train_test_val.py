import 

def split_train_test_val(X, y, threshold=0.1):  # Tested [N]
    """
    Creates and compiles a fully-connected feed forward neural network model using Keras

    Args:
        X (DataFrame): 
        y (ndarray): Labels
        threshold (float): The proportion to split the data
        
    Returns:
        Xval (DataFrame): Validation set 
        Xtest (DataFrame): Test set proportion to the threshold
        Xtrain (DataFrame): Train set
        
        yval (ndarray): Validation labels 
        ytest (ndarray): Test labels
        ytrain (ndarray): Train labels
        
    """
    
    # Split Train, Test, Validation set
    total_obs = X.shape[0]
    thred = int(total_obs * threshold)
    
    # For X
    Xval = X[ total_obs - thred : total_obs ]
    Xtest = X[ total_obs - thred * 2 : total_obs - thred ]
    Xtrain = X[ : total_obs - thred * 2 ]

    # For y:
    yval = y[ total_obs - thred : total_obs ]
    ytest = y[ total_obs - thred * 2 : total_obs - thred ]
    ytrain = y[ : total_obs - thred * 2 ]
    
    return Xval, Xtest, Xtrain, yval, ytest, ytrain