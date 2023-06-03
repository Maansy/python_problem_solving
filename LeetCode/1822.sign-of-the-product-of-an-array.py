#
# @lc app=leetcode id=1822 lang=python
#
# [1822] Sign of the Product of an Array
#
from typing import List
import math
# @lc code=start
class Solution(object):
    def signFunc(self, num: int):
        return 1 if num > 1 else -1 if num < 0 else 0

    def arraySign(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        product = math.prod(nums)
        signfunc = self.signFunc(product)

        return f'the product of all values is {product}, and signFunc({product}) = {signfunc}'
         
# @lc code=end
get_values = Solution()
print(get_values.arraySign([1,2,-3]))