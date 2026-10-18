from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    n = len(x);
    mean = sum(x) / n

    y = sorted(x)

    if n % 2 == 1:
        median = ( y[n // 2] )
    else:
        median = ( y[n // 2 - 1] + y[n // 2] ) / 2

    counts = {}
    for num in x:
        counts[num] = counts.get(num,0) + 1

    mode = max(counts, key = counts.get)

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode)
    }
    
    pass
    