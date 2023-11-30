#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import List, Optional
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.dfs(root, targetSum, [], res)
        return res
    
    def dfs(self, root, targetSum, path, res):
        if not root:
            return
        if not root.left and not root.right and root.val == targetSum:
            path.append(root.val)
            res.append(path[:])
            path.pop()
            return
        path.append(root.val)
        self.dfs(root.left, targetSum - root.val, path, res)
        self.dfs(root.right, targetSum - root.val, path, res)
        path.pop()
# @lc code=end

