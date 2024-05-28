import matplotlib.pyplot as plt
import pandas as pd
from interpolations import *


def plot_data_from_file(filename, num_nodes, num_points=50):
    df = pd.read_csv(filename)
    x = list(df["Dystans (m)"])
    y = list(df["Wysokość (m)"])
    x_values, y_values = select_nodes(x, y, num_nodes)

    plt.plot(x, y, color='green', label='Original')
    plt.scatter(x_values, y_values, color='blue', label='Nodes', marker='o')

    #x_inter, y_inter = lagrange_interpolation(x_values, y_values, num_points)
    #print(x_inter, y_inter)
    x_inter, y_inter = interpolation_splines(x_values, y_values, num_points)

    plt.plot(x_inter, y_inter, color="red", label='Lagrange')

    plt.xlabel('X Points')
    plt.ylabel('Y Points')
    plt.title('mount everest')

    plt.legend()
    plt.show()

def main():
    file_path = 'MountEverest.csv'
    num_nodes = 12
    plot_data_from_file(file_path, num_nodes)

main()