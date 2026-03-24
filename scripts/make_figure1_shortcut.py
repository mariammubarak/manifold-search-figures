from src.manifolds import generate_swiss_roll
from src.graphs import build_knn_graph, pick_far_points, shortest_path_nodes
from src.plotting import plot_shortcut_vs_geodesic


def main():
    # Step 1: generate manifold
    X, t = generate_swiss_roll(
        n_samples=1200,
        noise=0.0,
        random_state=42
    )

    # Step 2: build graph
    G = build_knn_graph(X, n_neighbors=12)

    # Step 3: choose two points
    source, target = pick_far_points(X, i=50, j=900)

    # Step 4: compute graph shortest path
    path_nodes = shortest_path_nodes(G, source, target)

    # Step 5: save figure
    plot_shortcut_vs_geodesic(
        X=X,
        source=source,
        target=target,
        path_nodes=path_nodes,
        save_path="figures/figure1_shortcut.png"
    )

    print("Saved figure to figures/figure1_shortcut.png")


if __name__ == "__main__":
    main()
