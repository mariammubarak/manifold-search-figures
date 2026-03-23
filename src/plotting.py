
import os
import matplotlib.pyplot as plt
import numpy as np


def plot_shortcut_vs_geodesic(X, source, target, path_nodes, save_path):
    """
    Plot:
    - all swiss roll points
    - straight Euclidean segment between source and target
    - graph shortest path along the manifold
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Background point cloud
    ax.scatter(
        X[:, 0], X[:, 1], X[:, 2],
        s=8,
        alpha=0.35
    )

    # Source and target points
    p = X[source]
    q = X[target]

    ax.scatter(p[0], p[1], p[2], s=80, label="source")
    ax.scatter(q[0], q[1], q[2], s=80, label="target")

    # Straight Euclidean shortcut
    ax.plot(
        [p[0], q[0]],
        [p[1], q[1]],
        [p[2], q[2]],
        linewidth=2.5,
        linestyle="--",
        label="Euclidean shortcut"
    )

    # Graph geodesic path
    path_xyz = X[path_nodes]
    ax.plot(
        path_xyz[:, 0],
        path_xyz[:, 1],
        path_xyz[:, 2],
        linewidth=3,
        label="Graph geodesic path"
    )

    ax.set_title("Euclidean Shortcut vs Manifold Path")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.legend()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
