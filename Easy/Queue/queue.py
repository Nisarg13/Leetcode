from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_all_nodes(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            # Print the value of the current node
            print(node.val)

            # Enqueue the next level nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# Example usage:
# Create a sample binary tree
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Call the function to print all nodes
print_all_nodes(root)
