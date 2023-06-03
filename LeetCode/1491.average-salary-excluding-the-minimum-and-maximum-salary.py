#
# @lc app=leetcode id=1491 lang=python
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#
from typing import List

# @lc code=start
class Solution(object):
    def average(self, salary: List[int]) -> float:
        """
        :type salary: List[int]
        :rtype: float
        """
        avg_salary = (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2) 
        return avg_salary
        
# @lc code=end

get_avg = Solution()
print(get_avg.average([1000,6000,3000,2500]))