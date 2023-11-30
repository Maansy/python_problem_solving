#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#

# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            if i*(i+1)/2 > n:
                break
            if (n - i*(i+1)/2) % i == 0:
                count += 1
        return count
# @lc code=end

