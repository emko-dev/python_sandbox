# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        
        largest_values = []
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()
            if level == len(largest_values):
                largest_values.append(node.val)
            else:
                largest_values[level] = max(largest_values[level], node.val)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return largest_values
