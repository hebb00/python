# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """


    if not root:
        return []
    st=[root]
    out=[]
    if not root:
        return []
    while st:
        node = st.pop()
        if node:
            out.append(node.val)
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)


    
    return out[::-1]
    
        
        

if __name__ == '__main__':
    node = TreeNode()
    n=TreeNode()
    nn= TreeNode()
    j=TreeNode()
    j.val=3
    n.val=9
    nn.val=4
    nn.left=j
    node.val=5
    node.left=nn
    node.right=n
    
    print(postorderTraversal(node))
    