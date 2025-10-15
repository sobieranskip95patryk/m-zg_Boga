import torch
import torch.nn as nn
import numpy as np
import random
import json
import os
from gtts import gTTS
from src.utils import process_input, get_weights
from flask import Flask, request, jsonify

# LSTM-based PsycheNet
class PsycheNet(nn.Module):
    def __init__(self, input_size=10, hidden_size=12, num_layers=2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)
    
    def forward(self, x):
        h0 = torch.zeros(2, x.size(0), 12).to(x.device)  # num_layers, batch, hidden_size
        c0 = torch.zeros(2, x.size(0), 12).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])  # Ostatni output
        return torch.sigmoid(out) * 100

# Trening z gradient descent (placeholder, wymaga danych)
def train_net(net, inputs, T, env_factors, epochs=10, lr=0.01):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=lr)
    input_tensor = torch.tensor([inputs + [T] + env_factors], dtype=torch.float32).unsqueeze(0)
    target = torch.tensor([70.0])  # Domyślny target (zmień z danych)
    for epoch in range(epochs):
        optimizer.zero_grad()
        output = net(input_tensor)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
    print(f"Training epoch {epoch+1}, Loss: {loss.item():.2f}")
    return net

# Reszta funkcji (calculate_S_dec, evolve_net, assess_phase, simulate_monte_carlo, voice_output) pozostaje bez zmian
# ... (kopiuj z poprzedniej wersji)

# Ulepszony run_pipeline z treningiem
def run_pipeline(data=None, file_path=None, weight_variant='linear'):
    processed = process_input(data, file_path)
    inputs, env_factors = processed['inputs'], processed['env_factors']
    W, M, D, C, A, E, T = inputs
    base_S = W + M + D + C + E + T
    S_dec = calculate_S_dec(inputs, T, env_factors, weight_variant)
    phase = assess_phase(S_dec, T)
    
    net = PsycheNet()
    if phase != "Rozwój":
        print("Ewolucja macierzy...")
        net = evolve_net(net, inputs, T, env_factors, generations=5)  # 5 generacji
    else:
        try:
            net = train_net(net, inputs, T, env_factors)  # Próba treningu
        except:
            net = evolve_net(net, inputs, T, env_factors, generations=5)  # Fallback na GA
    
    p_s = fitness(net, inputs, T, env_factors)
    mean_p_s, std_p_s = simulate_monte_carlo(inputs, T, env_factors)
    
    recs = []
    if p_s < 50:
        recs.append("Zwiększ E o 1-2 (energia) dla boostu.")
    if phase == "Destrukcja":
        recs.append("Reset do Punktu 0: Skup się na A (aspiracja).")
    if env_factors[1] > 0.5:
        recs.append("Redukuj CO2 dla lepszej stabilności.")
    
    result = {
        "Base_S": base_S,
        "S_dec": S_dec,
        "Phase": phase,
        "P(S)_%": p_s,
        "P(S)_Mean_%": mean_p_s,
        "P(S)_Std_%": std_p_s,
        "Recommendations": recs,
        "Env_Factors": {"Health_Index": env_factors[0], "CO2_Levels": env_factors[1], "Humidity": env_factors[2]},
        "Timestamp": "2025-10-09 17:07 CEST"
    }
    result_json = json.dumps(result, indent=2)
    voice_output(result_json)
    return result_json

# Test
if __name__ == "__main__":
    data = [7, 6, 5, 4, 8, 6, 0.5, 0.6, 0.4, 0.5]
    result = run_pipeline(data=data, weight_variant='sinusoidal')
    print(result)