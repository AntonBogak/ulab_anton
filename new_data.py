

import torch
import numpy as np

# Function to generate data with added noise/obscured pattern
def generate_hidden_data(N=1000, D_in=2, noise_factor=0.1):
    x_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
    y_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
    X, Y = np.meshgrid(x_data, y_data)

    pattern = np.sin(X) + np.cos(Y)

    # Actual data 
    x = torch.randn(N, D_in) * 3.1415  # Input data
    y = (x[:, 0].sin() + x[:, 1].cos()).unsqueeze(1)  # True pattern

    # Add noise to the data to obscure the pattern
    noise = torch.randn(N, 1) * noise_factor
    y += noise

    x_values = x.numpy()[:, 0]
    y_values = x.numpy()[:, 1]
    color_values = y.numpy().flatten()

    return x, y, x_values, y_values, color_values

if __name__ == "__main__":
    x, y, x_vals, y_vals, color_vals = generate_hidden_data()