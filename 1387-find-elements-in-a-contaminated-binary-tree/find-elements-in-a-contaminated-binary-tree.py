# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def fix(self, node):
        x = node.val
        l, r = 2 * x + 1, 2 * x + 2
        if node.left != None:
            self.s.add(l)
            node.left.val = l
            self.fix(node.left)

        if node.right != None:
            self.s.add(r)
            node.right.val = r
            self.fix(node.right)

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.s = set()
        self.s.add(0)
        self.fix(root)

    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)