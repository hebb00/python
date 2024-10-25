# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
out =[]

def preTraversal(root):
    if not root:
        return []
    st = [root]
    while st:
        node = st.pop()
        out.append(node.val)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return out
        
        
        
    

    
    
    
    
    
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
