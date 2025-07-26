# emotion.py
# Logic for deriving emotional state from biometrics
import numpy as np

def normalize_vector(vec):
    arr = np.array(list(vec.values()), dtype=float)
    norm = np.linalg.norm(arr)
    if norm == 0:
        return dict(zip(vec.keys(), arr))
    return dict(zip(vec.keys(), arr / norm))

def derive_emotion(biometrics):
    # Example weights for mapping biometrics to emotions
    weights = {
        'trust': 0.5 * biometrics.get('HRV', 0) + 0.2 * biometrics.get('BrainwaveRatio', 0),
        'curiosity': 0.7 * biometrics.get('EDA', 0) + 0.3 * biometrics.get('BrainwaveRatio', 0),
        'urgency': 1.0 - biometrics.get('HRV', 0) + 0.5 * biometrics.get('EDA', 0)
    }
    return normalize_vector(weights)
