import numpy as np

def calculate(list):
    # Ensure the list has exactly 9 numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Reshape into 3x3 matrix
    matrix = np.array(list).reshape(3, 3)
    
    # Mean calculations
    mean_axis0 = matrix.mean(axis=0).tolist()  # per column
    mean_axis1 = matrix.mean(axis=1).tolist()  # per row
    mean_flat  = matrix.mean().item()          # overall mean
    
    # --- variance ---
    var_axis0 = matrix.var(axis=0).tolist()
    var_axis1 = matrix.var(axis=1).tolist()
    var_flat  = matrix.var().item()

    # --- standard deviation ---
    std_axis0 = matrix.std(axis=0).tolist()
    std_axis1 = matrix.std(axis=1).tolist()
    std_flat  = matrix.std().item()

    # max
    max_axis0 = matrix.max(axis=0).tolist()
    max_axis1 = matrix.max(axis=1).tolist()
    max_flat  = matrix.max().item()

    # min
    min_axis0 = matrix.min(axis=0).tolist()
    min_axis1 = matrix.min(axis=1).tolist()
    min_flat  = matrix.min().item()

    # sum
    sum_axis0 = matrix.sum(axis=0).tolist()
    sum_axis1 = matrix.sum(axis=1).tolist()
    sum_flat  = matrix.sum().item()

    # Build return dictionary (only for 'mean' for now)
    calculations = {
        'mean': [mean_axis0, mean_axis1, mean_flat],
        'variance': [var_axis0, var_axis1, var_flat],
        'standard deviation': [std_axis0, std_axis1, std_flat],
        'max': [max_axis0, max_axis1, max_flat],
        'min': [min_axis0, min_axis1, min_flat],
        'sum': [sum_axis0, sum_axis1, sum_flat]
    }

    return calculations