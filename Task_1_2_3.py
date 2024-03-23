class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current.val

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current.val


def sum_value_nodes(node):
    if node is None:
        return 0
    return node.val + sum_value_nodes(node.left) + sum_value_nodes(node.right)

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)


print(root)
print(f"Max: {max_value_node(root)}")
print(f"Min: {min_value_node(root)}")
print(f"Sum: {sum_value_nodes(root)}")
