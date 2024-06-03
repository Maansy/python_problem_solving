#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        median = int(len(nums) / 2)
        if len(nums) % 2 == 0:
            median_value = (nums[median] + nums[median-1]) / 2
            return median_value
        else:
            median_value = nums[median]
            return median_value
        

# from typing import List
# import numpy as np
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

# s = Solution()
# nums1 = [11,2,4,5]
# nums2 = [2,2,3]
# print(s.findMedianSortedArrays(nums1,nums2))
# @lc code=end

