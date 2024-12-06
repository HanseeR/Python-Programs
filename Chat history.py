import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Creating a flow diagram using matplotlib
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')

# Define box properties
box_style = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#d0e1f9", linewidth=1.5)
arrow_style = dict(arrowstyle="-|>", color="black", lw=1.5)

# Box positions and text
boxes = [
    {"pos": (0.5, 0.9), "text": "International Collaboration", "size": (0.3, 0.05)},
    {"pos": (0.5, 0.75), "text": "National-Level Policy Framework", "size": (0.35, 0.05)},
    {"pos": (0.5, 0.6), "text": "Public-Private Partnerships\n(PPP) and Funding", "size": (0.35, 0.1)},
    {"pos": (0.5, 0.45), "text": "Regional/State-Level Initiatives\n& Pilot Projects", "size": (0.4, 0.1)},
    {"pos": (0.5, 0.3), "text": "Skill Development Centers\nand Digital Infrastructure", "size": (0.4, 0.1)},
    {"pos": (0.5, 0.15), "text": "Local Educational Institutions\nand Community Engagement", "size": (0.4, 0.1)}
]

# Draw boxes and add text
for box in boxes:
    rect = mpatches.FancyBboxPatch(
        (box["pos"][0] - box["size"][0] / 2, box["pos"][1] - box["size"][1] / 2),
        box["size"][0],
        box["size"][1],
        **box_style
    )
    ax.add_patch(rect)
    ax.text(
        box["pos"][0],
        box["pos"][1],
        box["text"],
        ha="center",
        va="center",
        fontsize=10
    )

# Draw arrows
for i in range(len(boxes) - 1):
    start = boxes[i]["pos"]
    end = boxes[i + 1]["pos"]
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=arrow_style
    )

# Title
ax.set_title("Bottom-Up Approach for Skill Collaboration & Integration", fontsize=14, weight='bold')

plt.tight_layout()
plt.show()