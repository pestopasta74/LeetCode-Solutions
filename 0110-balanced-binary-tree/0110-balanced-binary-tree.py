# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # If the subtree is not balanced, return -1 to mark it as unbalanced
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            # Return the height of the subtree rooted at the current node
            return max(left_height, right_height) + 1
        
        return height(root) != -1
