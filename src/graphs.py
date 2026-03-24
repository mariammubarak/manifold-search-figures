import networkx as nx
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
    G = G.to_undirected()
    return G


def pick_far_points(X, i=50, j=900):
    """
    Pick two point indices to visualize.
    """
    return i, j


def shortest_path_nodes(G, source, target):
    """
    Compute the shortest path in the weighted graph.
    """
    return nx.shortest_path(G, source=source, target=target, weight="weight")


def sample_background_edges(G, max_edges=900):
    """
    Take a subset of undirected graph edges for background drawing,
    so the manifold feels structured without becoming too cluttered.
    """
    edges = list(G.edges())
    if len(edges) <= max_edges:
        return edges
    return edges[:max_edges]
