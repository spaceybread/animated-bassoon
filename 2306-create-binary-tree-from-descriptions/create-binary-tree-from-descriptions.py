# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, desc: List[List[int]]) -> Optional[TreeNode]:
        chi, nodes = set(), {}

        for p, c, isLeft in desc:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            if isLeft:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            chi.add(c)

        for d in desc:
            if d[0] not in chi:
                return nodes[d[0]]