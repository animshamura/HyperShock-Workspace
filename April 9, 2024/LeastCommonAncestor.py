class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def BinaryTree(elements, index=1):
    if index < len(elements):
        if elements[index] is None:
            return None
        
        root = TreeNode(elements[index])
        root.left = BinaryTree(elements, 2 * index )
        root.right = BinaryTree(elements, 2 * index + 1)
        return root
    return None

def LCA(root, node1, node2):
    if root is None: return None
    if root.key == node1 or root.key == node2:
        return root

    left_lca = LCA(root.left, node1, node2)
    right_lca = LCA(root.right, node1, node2)
    
    if left_lca and right_lca: return root
    
    return left_lca if left_lca is not None else right_lca

# Constructing a sample binary tree
elements = [None, 1, 2, 3, 4, 5, 6, 7,8,None,9,None,10]  
root = BinaryTree(elements)

lca = LCA(root, 7, 10)
print(f"Least Common Ancestor of 7 and 10 is {lca.key}")  

lca = LCA(root, 4, 6)
print(f"Least Common Ancestor of 4 and 6 is {lca.key}")  
  
