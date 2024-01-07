import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import heapq

graph = {
    'A': {'B': 2, 'C': 3, 'E': 5},
    'B': {'D': 4, 'E': 2},
    'C': {'F': 1, 'G': 3},
    'D': {'B': 1, 'E': 3},
    'E': {'A': 1, 'B': 2, 'D': 3},
    'F': {'C': 1, 'G': 2},
    'G': {'C': 3, 'F': 2}
}

def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = set()

    while heap:
        (cost, current) = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            return cost

        for neighbor, weight in graph[current].items():
            heapq.heappush(heap, (cost + weight, neighbor))

    return float('inf')

G = nx.Graph(graph)
pos = nx.circular_layout(G)
fig, ax = plt.subplots()
plt.title("Interactive Graph")

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_family='sans-serif')

nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
edge_labels = nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): graph[u][v] for u, v in G.edges()}, font_color='red')

start_node = 'A'
end_node = 'G'
shortest_path = []

def on_button_click(event):
    global start_node, end_node, shortest_path
    start_node = input("Enter start node: ").upper()
    end_node = input("Enter end node: ").upper()

    if start_node in G and end_node in G:
        shortest_path = nx.shortest_path(G, source=start_node, target=end_node)
        print(f"Shortest path: {shortest_path}")
        for u, v in zip(shortest_path[:-1], shortest_path[1:]):
            print(f"Weight from {u} to {v}: {graph[u][v]}")

button_ax = plt.axes([0.81, 0.01, 0.1, 0.05])
button = Button(button_ax, 'Change Path')
button.on_clicked(on_button_click)

plt.axis('off')
plt.show()