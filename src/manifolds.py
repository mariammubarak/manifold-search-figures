import numpy as np
from sklearn.datasets import make_swiss_roll


def generate_swiss_roll(n_samples=1200, noise=0.0, random_state=42):
    """
    Generate a swiss roll point cloud.

    Returns
    -------
    X : ndarray of shape (n_samples, 3)
        3D coordinates of the swiss roll points.
    t : ndarray of shape (n_samples,)
        Unrolled parameter used by make_swiss_roll.
    """
    X, t = make_swiss_roll(
        n_samples=n_samples,
        noise=noise,
        random_state=random_state
    )
    return X, t
