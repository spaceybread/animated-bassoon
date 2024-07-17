# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], d: List[int]) -> List[TreeNode]:
        s, res = set(d), [] 

        def dfs(root, flag):
            if not root: 
                return None
            
            tod = (root.val in s)
            root.left = dfs(root.left, tod)
            root.right = dfs(root.right, tod)

            if not tod and flag:
                res.append(root)
            
            return None if tod else root
        
        dfs(root, True)

        return res
