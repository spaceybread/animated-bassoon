"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def sol(self, r, o):
            if r:
                o.append(r.val)
                for n in r.children:
                    self.sol(n, o)
                
        
    def preorder(self, root: 'Node') -> List[int]:
        out = []
        self.sol(root, out)
        return out
        