import numpy as np
import matplotlib.pyplot as plt

def load_initial_conditions(file_path):
    return np.genfromtxt(file_path).astype(int)

def count_neighbors(matrix, i, j):
    neighbors = [
        matrix[i - 1, j - 1], matrix[i - 1, j], matrix[i - 1, j + 1],
        matrix[i, j - 1], matrix[i, j + 1],
        matrix[i + 1, j - 1], matrix[i + 1, j], matrix[i + 1, j + 1]
    ]
    return sum(neighbors)

def update_game(matrix):
    new_matrix = matrix.copy()

    for i in range(1, matrix.shape[0] - 1):
        for j in range(1, matrix.shape[1] - 1):
            neighbors_count = count_neighbors(matrix, i, j)

            if matrix[i, j] == 1:  # live 
                if neighbors_count not in [2, 3]:
                    new_matrix[i, j] = 0  # died
            else:  # dead 
                if neighbors_count == 3:
                    new_matrix[i, j] = 1  # alive

    return new_matrix

def plot_game(matrix, step, save_path):
    plt.imshow(matrix, cmap='binary', interpolation='none')
    plt.title(f"Step {step}")
    plt.savefig(save_path)
    plt.close()

if __name__ == "__main__":
    initial_conditions_file = "gun.txt"
    output_folder = "output_serial"
    initial_matrix = load_initial_conditions(initial_conditions_file)

    plt.figure(figsize=(5, 7))
    plt.title("Initial")
    plot_game(initial_matrix, 0, f"{output_folder}/step_0.png")

    for step in range(1, 5):
        initial_matrix = update_game(initial_matrix)
        plot_game(initial_matrix, step, f"{output_folder}/step_{step}.png")
