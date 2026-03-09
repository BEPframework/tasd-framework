```python
import numpy as np
from sklearn.decomposition import PCA
from scipy.optimize import minimize

class TASD:
    """
    TASD Unified Framework – Toroidal-Attractor Signal Dynamics
    Combines attractor stability with dynamic modulation.
    """
    def __init__(self, dim=216, gamma=0.05, sigma=1.0):
        self.dim = dim
        self.gamma = gamma
        self.sigma = sigma
        self.a_i = np.random.uniform(0.5, 1.5, dim)
        self.pca = PCA(n_components=3)

    def evolve(self, features_scaled, t=0.0):
        """Main TASD evolution function"""
        psi = np.zeros((len(t), self.dim))
        for i in range(self.dim):
            oscillatory = (np.cos(2*np.pi*0.1*t) + 1j*np.sin(2*np.pi*0.1*t)) * np.exp(-self.gamma*t)
            psi[:, i] = self.a_i[i] * np.real(oscillatory) * features_scaled[:, i % features_scaled.shape[1]]
        return self.pca.fit_transform(psi)

    def optimize(self, features_scaled, t):
        """Simple stability optimizer"""
        def objective(x):
            self.gamma = x[0]
            return np.std(self.evolve(features_scaled, t)[:, 0])
        from scipy.optimize import minimize
        result = minimize(objective, [self.gamma], bounds=[(0.01, 0.2)])
        self.gamma = result.x[0]
        return result.fun
