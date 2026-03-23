
import networkx as nx
import numpy as np
from sklearn.neighbors import kneighbors_graph


def build_knn_graph(X, n_neighbors=10):
    """
    Build a weighted kNN graph from point cloud X.
    Edge weights are Euclidean distances in ambient space.
    """
    A = kneighbors_graph(
        X,
        n_neighbors=n_neighbors,
        mode="distance",
        include_self=False
    )

    G = nx.from_scipy_sparse_array(A)

    # Make sure graph is undirected
    G = G.to_undirected()

    return G


def pick_far_points(X, i=50, j=900):
    """
    Pick two point indices to visualize.
    You can change these later if needed.
    """
    return i, j


def shortest_path_nodes(G, source, target):
    """
    Compute the shortest path in the weighted graph.
    """
    return nx.shortest_path(G, source=source, target=target, weight="weight")
