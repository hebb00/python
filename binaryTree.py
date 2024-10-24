# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
out =[]

def preTraversal(tree):
    if not tree:
        return
    out.append(tree.val)
    preTraversal(tree.left)
    preTraversal(tree.right)
    
    
    
    
    
if __name__ == "__main__":
    node = TreeNode()
    n=TreeNode()
    nn= TreeNode()
    n.val=9
    nn.val=4
    node.val=5
    node.left=nn
    node.right=n
    preTraversal(node)
    print(out)
