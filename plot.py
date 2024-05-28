import os

import pandas as pd

from interpolations import *
import matplotlib.pyplot as plt

def plot_orignal_data(filename):
    df = pd.read_csv(filename)
    basename = os.path.basename(filename)
    name_without_extension = os.path.splitext(basename)[0]
    x = list(df["Dystans (m)"])
    y = list(df["Wysokość (m)"])

    plt.plot(x, y, color='green', label='Original')

    plt.xlabel('X Points')
    plt.ylabel('Y Points')
    plt.title(name_without_extension)
    plt.legend()

    if not os.path.exists('plots'):
        os.makedirs('plots')
    plt.savefig(f'plots/{name_without_extension}_original.png')

    plt.show()

def plot_data_from_file(filename, num_nodes, cheb, lagrange, num_points=100):
    df = pd.read_csv(filename)
    basename = os.path.basename(filename)
    name_without_extension = os.path.splitext(basename)[0]
    x = list(df["Dystans (m)"])
    y = list(df["Wysokość (m)"])
    if cheb == True:
        x_values, y_values = select_chebyshev_nodes(x, y, num_nodes)
    else:
        x_values, y_values = select_nodes(x, y, num_nodes)

    plt.plot(x, y, color='green', label='Original')
    plt.scatter(x_values, y_values, color='blue', label='Nodes', marker='o')

    if lagrange:
        x_inter, y_inter = lagrange_interpolation(x_values, y_values, num_points)
        method_label = 'Lagrange'
    else:
        x_inter, y_inter = interpolation_splines(x_values, y_values, num_points)
        method_label = 'Splines'

    plt.plot(x_inter, y_inter, color="red", label=method_label)

    plt.xlabel('X Points')
    plt.ylabel('Y Points')
    plt.title(name_without_extension)

    plt.legend()

    # Save plot
    if not os.path.exists('plots'):
        os.makedirs('plots')
    plt.savefig(f'plots/{name_without_extension}_{method_label.lower()}_{num_nodes}_{cheb}.png')

    plt.show()