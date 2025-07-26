# strategy.py
# Logic for recommending CRM strategies based on emotional vector
import numpy as np

def normalize_vector(vec):
    arr = np.array(list(vec.values()), dtype=float)
    norm = np.linalg.norm(arr)
    if norm == 0:
        return dict(zip(vec.keys(), arr))
    return dict(zip(vec.keys(), arr / norm))

def recommend_strategy(emotion_vec):
    # Define strategy vectors (these can be tuned)
    strategies = {
        'personalize': {'trust': 0.8, 'curiosity': 0.6, 'urgency': 0.2},
        'respond immediately': {'trust': 0.2, 'curiosity': 0.3, 'urgency': 0.9},
        'build trust': {'trust': 1.0, 'curiosity': 0.2, 'urgency': 0.1}
    }
    emotion_vec = normalize_vector(emotion_vec)
    # Compute dot product scores
    scores = {name: np.dot(list(emotion_vec.values()), list(normalize_vector(vec).values()))
              for name, vec in strategies.items()}
    # Select the strategy with the highest score
    best_strategy = max(scores, key=scores.get)
    return best_strategy, scores
