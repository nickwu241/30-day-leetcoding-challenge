# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3293/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Tuple

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.depth(root)[1]
    
    def depth(self, root: TreeNode) -> Tuple[int, int]:
        if not root:
            return (0, 0)
        left_depth, left_max_diameter = self.depth(root.left)
        right_depth, right_max_diameter = self.depth(root.right)
        current_depth = max(left_depth, right_depth) + 1
        current_diameter = left_depth + right_depth
        max_diameter = max(current_diameter, left_max_diameter, right_max_diameter)
        return (current_depth, max_diameter)
