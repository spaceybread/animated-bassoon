# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def fi(self, s, d):
        pattern = rf"{'-' * d}(\d+)"
        matches = re.findall(pattern, s)
        return list(map(int, matches))

    def recoverFromPreorder(self, t: str) -> Optional[TreeNode]:
        st, i = [], 0
        
        while i < len(t):
            d = 0
            while i < len(t) and t[i] == '-':
                d += 1
                i += 1
            
            start = i
            while i < len(t) and t[i].isdigit():
                i += 1
            
            val = int(t[start:i])
            node = TreeNode(val)
            
            if d == len(st):
                if st:
                    st[-1].left = node
            else: 
                st = st[:d]
                st[-1].right = node
            
            st.append(node)
        
        return st[0]
        