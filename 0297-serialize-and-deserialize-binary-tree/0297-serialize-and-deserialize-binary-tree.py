# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def toString(root, arr):
            if not root:
                arr.append('N')
            else:
                arr.append(str(root.val))
                toString(root.left, arr)
                toString(root.right, arr)
        
        arr = []
        toString(root, arr)
        return ' '.join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        listedData = data.split(" ")
        self.index = 0
        def toTree(listedData):
            val = listedData[self.index]
            if val == 'N':
                self.index += 1
                return None
            node = TreeNode(int(val))
            self.index += 1
            node.left = toTree(listedData)
            node.right = toTree(listedData)
            return node
        return toTree(listedData)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))