import networkx as nx
import matplotlib.pyplot as plt

# Original grid
G = nx.Graph()

edges = [
    ("Substation A", "Substation B"),
    ("Substation B", "Substation C"),
    ("Substation A", "Substation D"),
    ("Substation D", "Substation C")
]

G.add_edges_from(edges)

# Store positions so graph doesn't jump around
pos = nx.spring_layout(G, seed=42)

# Fault line
fault_edge = ("Substation B", "Substation C")

# Remove faulted line
G.remove_edge(*fault_edge)

# Alternative path
path = nx.shortest_path(
    G,
    "Substation A",
    "Substation C"
)

print("Alternative Path Found:")
print(path)

# Draw normal network
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000
)

# Draw failed line in RED
nx.draw_networkx_edges(
    nx.Graph([fault_edge]),
    pos,
    edge_color="red",
    width=3
)

plt.title("Self-Healing Smart Grid")

plt.show()