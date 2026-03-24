import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    img_a = mpimg.imread("figures/figure1_shortcut.png")
    img_b = mpimg.imread("figures/figure1b_graph.png")

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    axes[0].imshow(img_a)
    axes[0].axis("off")
    axes[0].text(
        0.02, 0.98, "A",
        transform=axes[0].transAxes,
        fontsize=18,
        fontweight="bold",
        va="top",
        ha="left"
    )

    axes[1].imshow(img_b)
    axes[1].axis("off")
    axes[1].text(
        0.02, 0.98, "B",
        transform=axes[1].transAxes,
        fontsize=18,
        fontweight="bold",
        va="top",
        ha="left"
    )

    plt.tight_layout()
    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/figure1_two_panel.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print("Saved figure to figures/figure1_two_panel.png")


if __name__ == "__main__":
    main()
