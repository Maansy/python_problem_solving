#
# @lc app=leetcode id=421 lang=python
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.root = {}
        for num in nums:
            node = self.root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        ans = 0
        for num in nums:
            node = self.root
            cur = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if 1 - bit in node:
                    cur |= (1 << i)
                    node = node[1 - bit]
                else:
                    node = node[bit]
            ans = max(ans, cur)
        return ans
# @lc code=end

