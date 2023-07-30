# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # idea: just swap left & right, recurse
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

