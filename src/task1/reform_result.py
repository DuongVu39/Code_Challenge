def hard_label(ypred, thresh=0.5):
    """
    Hard assign label after prediction of Keras model

    Args:
        ypred (int): Percentage that the label will be 0 or 1.
        thresh (float): Default=0.5 Threshold to assign labels.
        
    Returns:
        Label 0 if smaller than threshold and label 1 if larger than threshold.
    """
    
    if ypred > thresh:
        return 1
    else:
        return 0
    