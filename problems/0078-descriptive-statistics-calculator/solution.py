import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    arr = np.asarray(data)
    
    # 1. Central Tendency
    mean = np.mean(arr)
    median = np.median(arr)
    
    # Mode: np.unique returns sorted unique values and their counts.
    # np.argmax grabs the first index with the highest count (smallest value on ties).
    values, counts = np.unique(arr, return_counts=True)
    mode = values[np.argmax(counts)]
    
    # 2. Dispersion (Population variance & std dev: ddof=0)
    variance = np.var(arr)
    std_dev = np.std(arr)
    
    # 3. Percentiles & Interquartile Range (IQR)
    percentiles = np.percentile(arr, [25, 50, 75])
    iqr = percentiles[2] - percentiles[0]
    
    return {
        "mean": np.round(mean, 4),
        "median": np.round(median, 4),
        "mode": mode,
        "variance": np.round(variance, 4),
        "standard_deviation": np.round(std_dev, 4),
        "25th_percentile": np.round(percentiles[0], 4),
        "50th_percentile": np.round(percentiles[1], 4),
        "75th_percentile": np.round(percentiles[2], 4),
        "interquartile_range": np.round(iqr, 4)
    }