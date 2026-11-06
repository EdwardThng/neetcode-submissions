# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, max_so_far):
            if not node:
                return 0
            if node.val >= max_so_far:
                self.res += 1
                max_so_far = node.val
            if node.left:
                dfs(node.left, max_so_far)
            if node.right:
                dfs(node.right, max_so_far)
            return self.res

        if not root:
            return self.res
        
        dfs(root, root.val)

        return self.res
        
