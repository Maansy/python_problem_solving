#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
                print(nums[i], nums[i+1], nums[i+2])
                nums.pop(i)
            else:
                i += 1
        return len(nums)

        
# @lc code=end

    