import os
import matplotlib.pyplot as plt


def plot_shortcut_vs_geodesic(X, source, target, path_nodes, background_edges, save_path):
    """
    Plot:
    - faint local graph structure in the background
    - subtle point cloud
    - straight Euclidean shortcut
    - highlighted graph geodesic path
    """

    fig = plt.figure(figsize=(8.8, 6.6))
    ax = fig.add_subplot(111, projection="3d")

    # --- faint local graph structure ---
    for i, j in background_edges:
        xi, xj = X[i], X[j]
        ax.plot(
            [xi[0], xj[0]],
            [xi[1], xj[1]],
            [xi[2], xj[2]],
            linewidth=1.0,
            alpha=0.22,
            zorder=1
        )

    # --- subtle point cloud ---
    ax.scatter(
        X[:, 0], X[:, 1], X[:, 2],
        s=5,
        alpha=0.22,
        depthshade=False,
        zorder=2
    )

    p = X[source]
    q = X[target]

    # --- Euclidean shortcut: quiet comparison object ---
    ax.plot(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        linewidth=2.2,
        linestyle="--",
        alpha=0.95,
        zorder=4
    )

    # --- graph geodesic path: main route through the manifold ---
    path_xyz = X[path_nodes]
    ax.plot(
        path_xyz[:, 0],
        path_xyz[:, 1],
        path_xyz[:, 2],
        linewidth=2.8,
        alpha=0.98,
        solid_capstyle="round",
        solid_joinstyle="round",
        zorder=5
    )

    # --- black ring + colored fill markers ---
    ax.scatter(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        s=170,
        c="black",
        depthshade=False,
        zorder=6
    )
    ax.scatter(
        p[0], p[1], p[2],
        s=62,
        depthshade=False,
        zorder=7
    )
    ax.scatter(
        q[0], q[1], q[2],
        s=62,
        depthshade=False,
        zorder=7
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
