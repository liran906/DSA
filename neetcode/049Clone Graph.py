# Clone Graph
# https://neetcode.io/problems/clone-graph
# m

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# wrong solution: cannot retreve pre-created new_nodes.
# will define a new node, messing up the graph.
# class Solution:
#     def cloneGraph(self, node):
#         if node is None:
#             return None
        
#         first_node = Node(node.val)
#         frontier = [(node, first_node)]
#         reached = set()
#         # dfs
#         while frontier:
#             original_node, new_node = frontier.pop()
#             for neighbor in original_node.neighbors:
#                 if neighbor not in reached:
#                     new_neighbor = Node(neighbor.val)
#                     new_node.neighbors.append(new_neighbor)
#                     new_neighbor.neighbors.append(new_node)
#                     frontier.append((neighbor, new_neighbor))
#             reached.add(original_node)
#         return first_node
    
class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        clone = {node:Node(node.val)}
        frontier = [node]
        reached = set()

        while frontier:
            original_node = frontier.pop()
            for neighbor in original_node.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    frontier.append(neighbor)
                if neighbor not in reached:
                    clone[original_node].neighbors.append(clone[neighbor])
                    clone[neighbor].neighbors.append(clone[original_node])
            reached.add(original_node)
        return clone[node]

# don't need a extra reached. the clone will do.
class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        clone = {node:Node(node.val)}
        frontier = [node]

        while frontier:
            original_node = frontier.pop()
            for neighbor in original_node.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    frontier.append(neighbor)
                clone[original_node].neighbors.append(clone[neighbor])
        return clone[node]