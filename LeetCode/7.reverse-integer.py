#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = 1 if x > 0 else -1

        x = abs(x)
        reversed_x = 0
        while x:
            print(f'x: {x}, reversed_x: {reversed_x}')
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        reversed_x *= sign

        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x
        
# @lc code=end

s = Solution()
print(s.reverse(123))  # Output: 321
print(s.reverse(-123))  # Output: -321
print(s.reverse(120))  # Output: 21
print(s.reverse(0))  # Output: 0
print(s.reverse(1534236469))  # Output: 0