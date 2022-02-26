#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Created By: Roger IL Grande
# ---------------------------------------------------------------------------
"""ES-660 Assignment 2"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

EdgeList = nx.read_edgelist('assignment2.txt')  # Read in the given edge list

# Number of nodes, links, and degrees in the network
Nodes = EdgeList.number_of_nodes()
Links = EdgeList.number_of_edges()
Degrees = [val for (node, val) in sorted(EdgeList.degree())]


def average(lst):
    return sum(lst) / len(lst)


Average_Degree = average(Degrees)  # Calculate average degree


# Print out the summary of results
print("\nNumber of nodes:", Nodes)
print("Number of links:", Links)
print("Degrees for each node: (node, degree)", sorted(EdgeList.degree()))
print("Degrees only:", Degrees)
print("Average Degree:", Average_Degree)
print("Network density:", nx.density(EdgeList))


# Plot the degree distribution in log-log scale
def plot_degree_distribution(g, normalized=True):
    print("Creating degree distribution plot, close plot to see network layout plot...")
    aux_y = nx.degree_histogram(g)

    aux_x = np.arange(0, len(aux_y)).tolist()

    if normalized:
        for i in range(len(aux_y)):
            aux_y[i] = aux_y[i] / Nodes

    plt.title('\nDegree Distribution (log-log scale)')
    plt.xlabel('Degree\n(log scale)')
    plt.ylabel('Number of Nodes\n(log scale)')
    plt.xscale("log")
    plt.yscale("log")
    plt.plot(aux_x, aux_y, 'o')
    plt.show()


# User input selection for which network drawing algorithm to use
def get_plot_layout():
    print("\nWhich network layout algorithm would you like to see? \n\n1: Fruchterman Reingold"
          "\n2: Circular\n3: Random\n4: Spectral\n5: Spring")
    try:  # Exception handling if user input is not a number
        selection = int(input("\nAlgorithm: "))
    except ValueError:
        print("The input was not a valid integer")
        selection = -1

    while selection > 5 or selection < 1:  # While selection is out of range 1-5
        try:
            selection = int(input("Please enter a numer 1-5: "))
            if selection not in range(1, 6):
                print("Please try again")
                continue
            else:
                # Response is in range of algorithms
                # Ready to exit the loop
                break
        except ValueError:
            print("The input was not a valid integer")
            continue
    return selection


plot_layout = get_plot_layout()

plot_degree_distribution(EdgeList)  # This plot will appear first


# Output the user-selected network drawing
if plot_layout == 1:
    plt.title("Fruchterman Reingold Algorithm")
    nx.draw(EdgeList, with_labels=True, node_size=100, node_color="skyblue",
            pos=nx.fruchterman_reingold_layout(EdgeList), font_size=4)
    plt.show()
elif plot_layout == 2:
    plt.title("Circular Algorithm")
    nx.draw(EdgeList, with_labels=False, node_size=100, node_color="skyblue", pos=nx.circular_layout(EdgeList))
    plt.show()
elif plot_layout == 3:
    plt.title("Random Algorithm")
    nx.draw(EdgeList, with_labels=True, node_size=100, node_color="skyblue", pos=nx.random_layout(EdgeList),
            font_size=4)
    plt.show()
elif plot_layout == 4:
    plt.title("Spectral Algorithm")
    nx.draw(EdgeList, with_labels=True, node_size=100, node_color="skyblue", pos=nx.spectral_layout(EdgeList),
            font_size=4)
    plt.show()
elif plot_layout == 5:
    plt.title("Spring Algorithm")
    nx.draw(EdgeList, with_labels=True, node_size=100, node_color="skyblue", pos=nx.spring_layout(EdgeList),
            font_size=4)
    plt.show()
