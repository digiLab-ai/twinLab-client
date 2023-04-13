# Third-party imports
import numpy as np


def get_blur_boundaries(n: int) -> np.ndarray:
    """
    Get boundaries for making a nice probability distribution of a Gaussian
    """
    frac = 1./(2.*(n+1.))
    fmin, fmax = frac, 1.-frac
    f = np.linspace(fmin, fmax, n)
    dy = -np.sqrt(2.)*np.log(f)
    return dy


def get_blur_alpha(n: int, alpha_mid=0.99) -> float:
    """
    Get a sensible alpha value for a given number of samples
    """
    alpha = 1.-(1.-alpha_mid)**(1/n)
    return alpha