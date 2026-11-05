from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque([root] if root else [])
        final = []

        while d:
            for _ in range(len(d)):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            final.append(node.val)
        return final