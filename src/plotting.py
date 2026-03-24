def plot_graph_path_panel(X, G, source, target, path_nodes, save_path, max_edges=1200):
    """
    Plot a neighborhood-graph view of the swiss roll with the graph shortest path highlighted.
    """
    import os
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(8.2, 6.2))
    ax = fig.add_subplot(111, projection="3d")

    # Draw a limited number of graph edges in light gray
    edges = list(G.edges())
    edges = edges[:max_edges]

    for i, j in edges:
        xi, xj = X[i], X[j]
        ax.plot(
            [xi[0], xj[0]],
            [xi[1], xj[1]],
            [xi[2], xj[2]],
            color="#bdbdbd",
            linewidth=0.9,
            alpha=0.35,
            zorder=1
        )

    # Very subtle points
    ax.scatter(
        X[:, 0], X[:, 1], X[:, 2],
        s=5,
        alpha=0.18,
        depthshade=False,
        zorder=2
    )

    # Highlight shortest path in red
    for a, b in zip(path_nodes[:-1], path_nodes[1:]):
        xa = X[a]
        xb = X[b]
        ax.plot(
            [xa[0], xb[0]],
            [xa[1], xb[1]],
            [xa[2], xb[2]],
            color="#d62728",
            linewidth=2.4,
            alpha=0.95,
            solid_capstyle="round",
            zorder=4
        )

    p = X[source]
    q = X[target]

    # Black rings
    ax.scatter(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        s=170,
        c="black",
        depthshade=False,
        zorder=5
    )

    # Colored centers
    ax.scatter(
        p[0], p[1], p[2],
        s=62,
        c="#ff7f0e",
        depthshade=False,
        zorder=6
    )
    ax.scatter(
        q[0], q[1], q[2],
        s=62,
        c="#ff7f0e",
        depthshade=False,
        zorder=6
    )

    ax.set_title("Neighborhood Graph and Shortest Path", pad=10, fontsize=13)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.grid(False)

    try:
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor("white")
        ax.yaxis.pane.set_edgecolor("white")
        ax.zaxis.pane.set_edgecolor("white")
    except Exception:
        pass

    ax.view_init(elev=20, azim=-63)

    try:
        ax.set_box_aspect((1.45, 1.2, 0.8))
    except Exception:
        pass

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
