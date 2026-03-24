import os
import matplotlib.pyplot as plt


def plot_shortcut_vs_geodesic(X, source, target, path_nodes, save_path):
    """
    Plot:
    - all swiss roll points
    - straight Euclidean segment between source and target
    - graph shortest path along the manifold
    """

    fig = plt.figure(figsize=(8.4, 6.4))
    ax = fig.add_subplot(111, projection="3d")

    # Background manifold: lighter and quieter
    ax.scatter(
        X[:, 0], X[:, 1], X[:, 2],
        s=7,
        alpha=0.12
    )

    # Selected points
    p = X[source]
    q = X[target]

    # Euclidean shortcut: quieter
    ax.plot(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        linewidth=2.2,
        linestyle="--",
        alpha=0.9
    )

    # Graph geodesic path: main visual object
    path_xyz = X[path_nodes]
    ax.plot(
        path_xyz[:, 0],
        path_xyz[:, 1],
        path_xyz[:, 2],
        linewidth=3.2,
        solid_capstyle="round",
        solid_joinstyle="round"
    )

    # Source and target markers:
    # black ring underlay + smaller colored fill for a cleaner paper look
    ax.scatter(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        s=140,
        c="black",
        depthshade=False,
        zorder=5
    )
    ax.scatter(
        p[0], p[1], p[2],
        s=58,
        depthshade=False,
        zorder=6
    )
    ax.scatter(
        q[0], q[1], q[2],
        s=58,
        depthshade=False,
        zorder=6
    )

    # Cleaner title
    ax.set_title("Euclidean Shortcut vs Manifold Path", pad=14, fontsize=15)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Remove grid and soften panes
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

    # Slightly tighter/calm view
    ax.view_init(elev=20, azim=-63)

    # Make axes box feel less tall/heavy
    try:
        ax.set_box_aspect((1.45, 1.2, 0.8))
    except Exception:
        pass

    # No legend: cleaner paper-like composition
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
