import numpy as np
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    usamples, counts = np.unique(samples,return_counts=True)
    probabilities = counts / len(samples)

    return [(val, p)for val, p in zip(usamples, probabilities)]