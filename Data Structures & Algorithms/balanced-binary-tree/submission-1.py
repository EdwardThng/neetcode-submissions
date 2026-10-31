# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.best = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.best = max(self.best, abs(left - right))

            return max(left, right) + 1
        
        height(root)

        if self.best > 1:
            return False
        else:
            return True