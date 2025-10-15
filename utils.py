import pandas as pd
import numpy as np
import os

def process_input(data=None, file_path=None):
    """
    Process input data for Apex Circuitry Pipeline.
    Args:
        data (list): Optional [W, M, D, C, A, E, T, H, CO2, Hmd]
        file_path (str): Path to CSV file with columns W,M,D,C,A,E,T,H,CO2,Hmd
    Returns:
        dict: Processed and validated inputs
    """
    if file_path and os.path.exists(file_path):
        df = pd.read_csv(file_path)
        # "Okno treści 1/9" - losowy subsample 1/9 danych
        if len(df) > 9:
            df = df.sample(frac=1/9, random_state=369963)
        inputs = df[['W', 'M', 'D', 'C', 'A', 'E', 'T', 'H', 'CO2', 'Hmd']].values
    elif data:
        inputs = np.array([data])
    else:
        raise ValueError("Provide either data or file_path")

    # Walidacja
    for i, row in enumerate(inputs):
        W, M, D, C, A, E, T, H, CO2, Hmd = row
        if any(x <= 0 for x in [W, M, D, C, A, E]):
            raise ValueError(f"Input {i}: W,M,D,C,A,E must be positive")
        if not 0 <= T <= 1:
            raise ValueError(f"Input {i}: T must be in [0,1]")
        if not 0 <= H <= 1 or not 0 <= CO2 <= 1 or not 0 <= Hmd <= 1:
            raise ValueError(f"Input {i}: Env factors must be in [0,1]")

    # Normalizacja dla NN
    inputs[:, :6] = inputs[:, :6] / inputs[:, :6].max(axis=0)
    inputs[:, 7:] = inputs[:, 7:] / inputs[:, 7:].max(axis=0)

    return {
        'inputs': inputs[0, :7].tolist(),
        'env_factors': inputs[0, 7:].tolist()
    }

def get_weights(T, variant='linear'):
    """
    Calculate dynamic weights for W, M, D, C, A based on T and variant.
    Args:
        T (float): Phase (0 to 1)
        variant (str): 'linear' or 'sinusoidal'
    Returns:
        np.array: Normalized weights [w_W, w_M, w_D, w_C, w_A]
    """
    # Inspiracja <369963> jako mnożniki
    tesla_mult = np.array([3, 6, 9, 9, 6]) / 9  # Normalizacja do 1
    if variant == 'linear':
        w_A = 1 - T
        w_M = 1 - 2 * abs(T - 0.5)
        w_W = T
        w_D = w_M
        w_C = (1 - T)**2
    elif variant == 'sinusoidal':
        w_A = np.sin(np.pi * (1 - T))
        w_M = np.sin(np.pi * T)
        w_W = np.cos(np.pi * T / 2)
        w_D = w_M
        w_C = np.sin(np.pi * (1 - T))**2
    else:
        raise ValueError("Unknown variant: choose 'linear' or 'sinusoidal'")
    
    weights = np.array([w_W, w_M, w_D, w_C, w_A]) * tesla_mult
    return weights / weights.sum()