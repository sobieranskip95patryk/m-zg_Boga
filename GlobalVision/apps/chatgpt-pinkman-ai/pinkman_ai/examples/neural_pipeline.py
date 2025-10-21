"""Neural pipeline demo for ChatGPT-PinkMan-AI.
Run: python -m pinkman_ai.examples.neural_pipeline
Requires: numpy
"""
import numpy as np
from dataclasses import dataclass

# --- Core modules ---

@dataclass
class FeatureExtractor:
    config: dict | None = None

    def transform(self, x: dict) -> np.ndarray:
        X = x.get("features")
        if isinstance(X, np.ndarray):
            return X
        return np.asarray(X, dtype=float)

class SemanticModel:
    def __init__(self, config: dict | None = None):
        self.config = config or {}
        self.weights: np.ndarray | None = None

    def train(self, X: np.ndarray, y: np.ndarray, epochs: int = 5, lr: float = 0.01):
        n, d = X.shape
        out = y.shape[1]
        rng = np.random.default_rng(self.config.get("seed", 7))
        self.weights = rng.normal(scale=0.1, size=(d, out))
        for _ in range(epochs):
            pred = X @ self.weights
            grad = (X.T @ (pred - y)) / n
            self.weights -= lr * grad
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.weights is None:
            # lazy init to correct output shape
            self.weights = np.zeros((X.shape[1], 1))
        return X @ self.weights

class Recommender:
    def __init__(self, config: dict | None = None):
        self.config = config or {}

    def generate(self, scores: np.ndarray) -> dict:
        conf = float(np.clip(np.mean(np.abs(scores)), 0.0, 1.0))
        action = "explore" if conf < 0.33 else ("tune" if conf < 0.66 else "commit")
        return {"action": action, "confidence": conf}

class ErrorLearner:
    def __init__(self):
        self.history: list[float] = []

    def update(self, pred: np.ndarray, true: np.ndarray) -> float:
        pred = np.asarray(pred)
        true = np.asarray(true)
        loss = float(np.mean((pred - true) ** 2))
        self.history.append(loss)
        return loss

class EvolutionEngine:
    def __init__(self, population_size: int = 10, seed: int = 13):
        rng = np.random.default_rng(seed)
        self.population = [self._random_arch(rng) for _ in range(population_size)]
        self.fitness = [0.0] * population_size
        self.rng = rng

    def _random_arch(self, rng) -> dict:
        return {"layers": int(rng.integers(1, 5)), "activation": "relu"}

    def evaluate(self, candidate: dict, data: dict) -> float:
        X = data["features"]
        # simple proxy: prefer deeper when signal-to-noise is higher
        s = float(np.linalg.norm(X) / (np.sqrt(X.size) + 1e-9))
        return float(s / (1.0 + abs(3 - candidate["layers"])))

    def _mutate(self, arch: dict) -> dict:
        child = dict(arch)
        child["layers"] = max(1, child["layers"] + int(self.rng.choice([-1, 1])))
        return child

    def evolve(self, data: dict):
        self.fitness = [self.evaluate(c, data) for c in self.population]
        k = max(1, len(self.population) // 2)
        best = [c for _, c in sorted(zip(self.fitness, self.population), key=lambda t: t[0], reverse=True)[:k]]
        new_pop = best.copy()
        while len(new_pop) < len(self.population):
            parent = self.rng.choice(best)
            new_pop.append(self._mutate(parent))
        self.population = new_pop

    def sample(self) -> dict:
        return self.population[int(self.rng.integers(0, len(self.population)))]

class GaiaHub:
    def __init__(self):
        self.extractor = FeatureExtractor()
        self.semantic = SemanticModel()
        self.recommender = Recommender()
        self.error_learner = ErrorLearner()
        self.evolution = EvolutionEngine()

    def run_step(self, data: dict) -> tuple[dict, float]:
        X = self.extractor.transform(data)
        # train once per step on synthetic target for demo
        y = data.get("target", np.zeros((X.shape[0], 1)))
        self.semantic.train(X, y, epochs=3, lr=0.05)
        cons = self.semantic.predict(X)
        rec = self.recommender.generate(cons)
        loss = self.error_learner.update(cons, y)
        self.evolution.evolve({"features": X})
        return rec, loss

def main():
    hub = GaiaHub()
    for t in range(20):
        X = np.random.randn(32, 16)
        W_true = np.random.randn(16, 1)
        y = X @ W_true + 0.1 * np.random.randn(32, 1)
        rec, loss = hub.run_step({"features": X, "target": y})
        print(f"Step {t:02d} | loss={loss:.4f} | rec={rec} | arch={hub.evolution.sample()}")

if __name__ == "__main__":
    main()
