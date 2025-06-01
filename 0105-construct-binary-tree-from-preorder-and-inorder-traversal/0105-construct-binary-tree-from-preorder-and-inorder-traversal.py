# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIndex = 0
        self.inMap = {val : pos for pos, val in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None

            rootVal = preorder[self.preIndex]
            root = TreeNode(rootVal)

            self.preIndex += 1

            root.left = build(left, self.inMap[rootVal] - 1)
            root.right = build(self.inMap[rootVal] + 1, right)

            return root

        return build(0, len(inorder) - 1)
