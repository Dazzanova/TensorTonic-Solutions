import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """

    n = len(x)

    mean = sum(x) / n;

    variance = sum( (num - mean)**2 for num in x) / (n-1)

    sd = variance ** 0.5

    return {
        "variance": float(variance),
        "standard_deviation": float(sd),
    }
    
    pass