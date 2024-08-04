# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # start at the root, check for p/q 
        # recurse on left
            # if both pq in left, return (left)
            # if only one of pq, return root
            # if neither, recurse on right
        
        return root