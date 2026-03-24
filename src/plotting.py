import os
import matplotlib.pyplot as plt


def plot_shortcut_vs_geodesic(X, source, target, path_nodes, save_path):
    """
    Plot:
    - soft background point cloud
    - straight Euclidean shortcut
    - graph geodesic drawn as consecutive short segments
    """

    fig = plt.figure(figsize=(8.8, 6.6))
    ax = fig.add_subplot(111, projection="3d")

    # --- background manifold ---
    ax.scatter(
        X[:, 0], X[:, 1], X[:, 2],
        s=6,
        alpha=0.16,
        depthshade=False,
        zorder=1
    )

    p = X[source]
    q = X[target]

    # --- Euclidean shortcut: quiet comparison object ---
    ax.plot(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        linewidth=2.0,
        linestyle="--",
        alpha=0.85,
        zorder=3
    )

    # --- graph geodesic path: draw as small consecutive segments ---
    for a, b in zip(path_nodes[:-1], path_nodes[1:]):
        xa = X[a]
        xb = X[b]
        ax.plot(
            [xa[0], xb[0]],
            [xa[1], xb[1]],
            [xa[2], xb[2]],
            linewidth=2.4,
            alpha=0.95,
            solid_capstyle="round",
            zorder=4
        )

    # --- black ring markers ---
    ax.scatter(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        s=170,
        c="black",
        depthshade=False,
        zorder=5
    )
    ax.scatter(
        p[0], p[1], p[2],
        s=62,
        depthshade=False,
        zorder=6
    )
    ax.scatter(
        q[0], q[1], q[2],
        s=62,
        depthshade=False,
        zorder=6
    )

    ax.set_title("Euclidean Shortcut vs Manifold Path", pad=14, fontsize=15)

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
