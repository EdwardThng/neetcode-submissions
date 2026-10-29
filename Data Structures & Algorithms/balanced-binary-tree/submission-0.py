# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.best = 0
        def height(node: TreeNode):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            self.best = max(self.best, abs(left_height - right_height))

            return max(left_height, right_height) + 1
             
        height(root)
        if self.best > 1:
            return False
        return True