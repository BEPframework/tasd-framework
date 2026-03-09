import numpy as np
from tasd import TASD

# Simple test
t = np.linspace(0, 10, 1000)
features = np.random.randn(1000, 2)
features_scaled = (features - features.mean(0)) / features.std(0)

filter = TASD()
result = filter.evolve(features_scaled, t)
print("TASD result shape:", result.shape)
print("First few values:", result[:5, 0])
