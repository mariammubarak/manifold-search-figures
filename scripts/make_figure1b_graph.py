from src.manifolds import generate_swiss_roll
from src.graphs import build_knn_graph, pick_far_points, shortest_path_nodes
from src.plotting import plot_graph_path_panel


def main():
    X, t = generate_swiss_roll(
        n_samples=1200,
        noise=0.0,
        random_state=42
    )

    G = build_knn_graph(X, n_neighbors=12)

    source, target = pick_far_points(X, i=50, j=900)
    path_nodes = shortest_path_nodes(G, source, target)

    plot_graph_path_panel(
        X=X,
        G=G,
        source=source,
        target=target,
        path_nodes=path_nodes,
        save_path="figures/figure1b_graph.png",
        max_edges=1200
    )

    print("Saved figure to figures/figure1b_graph.png")


if __name__ == "__main__":
    main()
