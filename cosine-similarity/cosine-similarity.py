import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    x = math.sqrt(sum(i * i for i in a))
    y = math.sqrt(sum(i * i for i in b))
    if x == 0 or y == 0:
        return 0.0
    else:
        return (float)( np.array(a) @ np.array(b) / (x*y) )
    pass