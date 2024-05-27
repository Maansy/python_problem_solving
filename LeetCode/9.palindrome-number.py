#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        x = str(x)
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] != x[right]:
                print(x[left], x[right])
                return False
            left += 1
            right -= 1
        return True
    
# class Soulution2:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]
    
# class Solution3:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         if x == 0:
#             return True
#         if x % 10 == 0:
#             return False
#         x = str(x)
#         left = 0
#         right = len(x) - 1
#         while left < right:
#             if x[left] != x[right]:
#                 print(x[left], x[right])
#                 return False
#             left += 1
#             right -= 1
#         return True
    
    
    
# # @lc code=end
# s = Solution3()
# print(s.isPalindrome(1212))