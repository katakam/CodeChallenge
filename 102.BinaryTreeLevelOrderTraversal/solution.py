# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        levelOrder = []
        queue = deque([[0, root]])
        while queue:
            level, node = queue.popleft()
            if level == len(levelOrder):
                levelOrder.append([node.val])
            else:
                levelOrder[level].append(node.val)
            if node.left:
                queue.append([level+1, node.left])
            if node.right:
                queue.append([level+1, node.right])
        return levelOrder
