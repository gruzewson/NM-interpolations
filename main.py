import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def lagrange_basis(x, i, x_values):
    result = 1
    xi = x_values[i]
    n = len(x_values)
    for j in range(n):
        if i != j:
            xj = x_values[j]
            result *= (x - xj) / (xi - xj)
    return result

def lagrange_interpolation(x_values, y_values, num_points):
    x_min, x_max = min(x_values), max(x_values)
    x_inter = [x_min + i * (x_max - x_min) / (num_points - 1) for i in range(num_points)]
    y_inter = []

    for x in x_inter:
        total = 0
        n = len(x_values)
        for i in range(n):
            yi = y_values[i]
            total += yi * lagrange_basis(x, i, x_values)
        y_inter.append(total)

    return x_inter, y_inter

def select_nodes(x, y, num_nodes):
    step = len(x) // (num_nodes - 1)
    indices = [i * step for i in range(num_nodes - 1)] + [len(x) - 1]
    x_values = [x[i] for i in indices]
    y_values = [y[i] for i in indices]
    return x_values, y_values

def plot_data_from_file(filename, num_nodes):
    # Open the file and read its contents
    df = pd.read_csv(filename)
    x = list(df["Dystans (m)"])
    y = list(df["Wysokość (m)"])

    # Select evenly spaced nodes
    x_values, y_values = select_nodes(x, y, num_nodes)

    # Plot the original data points
    plt.plot(x, y, color='green', label='Original')
    plt.scatter(x_values, y_values, color='blue', label='Nodes', marker='o')

    # Compute the Lagrange interpolating polynomial
    x_inter, y_inter = lagrange_interpolation(x_values, y_values, 50)

    # Plot the interpolating polynomial
    plt.plot(x_inter, y_inter, color="red", label='Lagrange')

    # Set labels and title
    plt.xlabel('X Points')
    plt.ylabel('Y Points')
    plt.title('chelm')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

# Specify the path to your text file and the number of nodes
file_path = 'MountEverest.csv'
num_nodes = 9  # Example: change this number to select a different number of nodes
plot_data_from_file(file_path, num_nodes)