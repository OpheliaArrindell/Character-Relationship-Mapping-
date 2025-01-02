import json

import matplotlib.pyplot as plt
import networkx as nx

# -----------------------------------------------------------------------------------------------------------------------
# load characters from JSON file
with open("characters.json", encoding="utf8") as fh:
    characters = json.load(fh)

# -----------------------------------------------------------------------------------------------------------------------
# Visualizing Relationships (Network Graph)
G = nx.Graph()  # Create a new graph

# Add nodes (characters)
for character in characters:
    G.add_node(character)

# Add edges (relationships)
for character, details in characters.items():
    # print(character)
    for related_character, relationship in details['relationships'].items():
        G.add_edge(character, related_character, relationship=relationship)

# Plot the network of relationships
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title("Character Relationship Network")
plt.show()

# -----------------------------------------------------------------------------------------------------------------------
# Tracking Emotional Evolution Over Chapters
# We'll plot emotional conflict levels over the chapters for a specific character

# Plot emotional evolution for Bella_Buckerfield
Bella_Buckerfield_conflict = [characters["Bella_Buckerfield"]["evolution"]["1"]["conflict_level (Alex)"],
                  characters["Bella_Buckerfield"]["evolution"]["Sinking_Boat"]["conflict_level (Alex)"]]

# Plotting conflict levels for Bella_Buckerfield with Alex over chapters
plt.figure(figsize=(8, 6))
plt.plot([1, 2], Bella_Buckerfield_conflict, marker='o', color='r', label="Bella_Buckerfield's conflict with Alex")
plt.xlabel('Chapter')
plt.ylabel('Conflict Level')
plt.title('Bella_Buckerfield\'s Emotional Conflict with Alex')
plt.xticks([1, 2])
plt.legend()
plt.show()

# -----------------------------------------------------------------------------------------------------------------------
# Track and Visualize Motivations and Internal Conflicts

# For character growth, let's plot Bella_Buckerfield's motivation and internal conflict over chapters
Bella_Buckerfield_motivation = [characters["Bella_Buckerfield"]["evolution"]["1"]["motivation"],
                    characters["Bella_Buckerfield"]["evolution"]["Sinking_Boat"]["motivation"]]

# Create a bar plot for Bella_Buckerfield's motivations across different chapters
plt.figure(figsize=(10, 6))
plt.bar([1, 2], [len(mot) for mot in Bella_Buckerfield_motivation], tick_label=["Chapter 1", "Chapter 2"], color='b')
plt.xlabel('Chapter')
plt.ylabel('Motivation Length')
plt.title('Bella_Buckerfield\'s Motivation Evolution')
plt.show()

