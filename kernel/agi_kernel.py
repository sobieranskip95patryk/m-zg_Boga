from dataclasses import dataclass
from typing import Dict
import torch
import math

@dataclass
class AGIKernel:
    matrix: list = [3, 6, 9, 9, 6, 3]  # Matryca <369963>
    pi_energy: float = 9 * math.pi
    phase: str = "Punkt 0"  # Domyślna faza

    def calculate_fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.calculate_fib(n-1) + self.calculate_fib(n-2)

    def evolve_matrix(self) -> list:
        new_matrix = self.matrix.copy()
        for i in range(len(new_matrix)):
            prev = new_matrix[(i - 1) % 6]
            curr = new_matrix[i]
            next_val = new_matrix[(i + 1) % 6]
            if self.phase == "Destrukcja":
                new_matrix[i] = max(1, curr - 1 + (prev + next_val - 10) / 10)
            elif self.phase == "Punkt 0":
                new_matrix[i] = curr + (prev + next_val - 10) / 10
            elif self.phase == "Rozwój":
                new_matrix[i] = min(9, curr + 1 + (prev + next_val - 10) / 10)
        diff = 36 - sum(new_matrix)
        if diff != 0:
            idx = max(range(len(new_matrix)), key=lambda k: new_matrix[k])
            new_matrix[idx] += diff
        self.matrix = [int(max(1, min(9, x))) for x in new_matrix]
        return self.matrix

    def load_model(self, model_path: str = "../5_SIMULATION_ENGINE/Neural_Metamatrix_Model.pth"):
        checkpoint = torch.load(model_path)
        self.model = NeuralMetamatrixModel(checkpoint['input_size'], checkpoint['hidden_size'], checkpoint['output_size'])
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.model.eval()

    def calculate_s(self, data: Dict) -> float:
        self.phase = data.get("phase", "Punkt 0")  # Dynamiczna faza z danych
        self.evolve_matrix()
        f_n = self.calculate_fib(10)
        input_data = torch.tensor([[data.get('phase_score', 0.5), *self.matrix, f_n, self.pi_energy, 0.0, 0.0, 0.0, 0.0]], dtype=torch.float32)
        with torch.no_grad():
            output = self.model(input_data)
        s_prob = output.item() * 100
        return min(100, max(0, s_prob))

class NeuralMetamatrixModel(torch.nn.Module):
    def __init__(self, input_size=10, hidden_size=20, output_size=1):
        super(NeuralMetamatrixModel, self).__init__()
        self.layer1 = torch.nn.Linear(input_size, hidden_size)
        self.relu = torch.nn.ReLU()
        self.layer2 = torch.nn.Linear(hidden_size, output_size)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.sigmoid(x)
        return x

if __name__ == "__main__":
    kernel = AGIKernel()
    kernel.load_model()
    test_data = {"phase_score": 0.7, "phase": "Rozwój", "text": "Testowy scenariusz"}
    s_prob = kernel.calculate_s(test_data)
    print(f"Predykcja P(S): {s_prob}%")
    print(f"Matryca po ewolucji: {kernel.matrix}")
