from plot import *


def main():
    files = ['paths/WielkiKanionKolorado.csv', 'paths/stale.txt']#'paths/SpacerniakGdansk.csv', 'paths/MountEverest.csv']#, ]

    #originals
    #for file in files:
    #    plot_orignal_data(file)

    #interpolations
    for file in files:
        for num_nodes in [7, 14, 21, 28]:
            plot_data_from_file(file, num_nodes, False, True)

main()