import os
import matplotlib.pyplot as plt


def plot_shortcut_vs_geodesic(X, source, target, path_nodes, save_path):
    """
    Plot:
    - all swiss roll points
    - straight Euclidean segment between source and target
    - graph shortest path along the manifold
    """

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")

    # Background point cloud: softer and quieter
    ax.scatter(
        X[:, 0], X[:, 1], X[:, 2],
        s=10,
        alpha=0.18
    )

    # Source and target points
    p = X[source]
    q = X[target]

    ax.scatter(
        p[0], p[1], p[2],
        s=120,
        label="source",
        depthshade=False
    )
    ax.scatter(
        q[0], q[1], q[2],
        s=120,
        label="target",
        depthshade=False
    )

    # Straight Euclidean shortcut
    ax.plot(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        linewidth=2.8,
        linestyle="--",
        label="Euclidean shortcut"
    )

    # Graph geodesic path
    path_xyz = X[path_nodes]
    ax.plot(
        path_xyz[:, 0],
        path_xyz[:, 1],
        path_xyz[:, 2],
        linewidth=3.8,
        label="Graph geodesic path"
    )

    # Cleaner title
    ax.set_title("Euclidean Shortcut vs Manifold Path", pad=18, fontsize=16)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Soften 3D panes/grid feel
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

    # Better viewing angle
    ax.view_init(elev=24, azim=-58)

    # Smaller, cleaner legend
    ax.legend(
        loc="upper right",
        frameon=True,
        fontsize=11
    )

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
