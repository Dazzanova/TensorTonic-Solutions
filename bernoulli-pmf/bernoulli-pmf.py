import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """

    pmf = []
    
    for num in x:
        if num == 0:
            y = 1 - p
        else:
            y = p
        pmf.append(float(y))

    mean = float( sum(x) / len(x) )
    var = float( sum( (num - mean)**2  for num in x ) )

    return {
        "pmf": np.array(pmf),
        "mean": float(p),
        "variance": float( p * (1-p) )
    }
    pass