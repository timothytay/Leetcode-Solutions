# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        rootVal = preorder[0]
        left = []
        right = []
        i = 0
        while i < len(inorder) and inorder[i] != rootVal:
            left.append(inorder[i])
            i += 1
        i += 1
        for j in range(i, len(inorder)):
            right.append(inorder[j])
        rightSet = set(right)
        leftSet = set(left)
        leftPre = []
        rightPre = []
        i = 1
        while i < len(inorder) and preorder[i] in leftSet:
            leftPre.append(preorder[i])
            i += 1
        
        for j in range(i, len(preorder)):
            rightPre.append(preorder[j])
        root = TreeNode(rootVal)
        root.left = self.buildTree(leftPre, left)
        root.right = self.buildTree(rightPre, right)
        return root