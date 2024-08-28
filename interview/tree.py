class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = 0
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0 
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) +1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(10)
root.right.left = TreeNode(15)
root.right.right = TreeNode(20)

print (maxDepth(root))

def is_same_tree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)



root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(10)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(20)


root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(10)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(20)

print (is_same_tree(root1, root2))



