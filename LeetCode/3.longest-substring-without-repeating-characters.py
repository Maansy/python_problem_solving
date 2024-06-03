#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         substring = ''
#         for i in range(len(s)+1):
#             print(s[i])
#             for j in range(len(s[i+1:]) + 1):
#                 print(s[j])
#                 if s[i] == s[j]:
#                     substring += s[i]
#         # print(substring) 
             

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_length = 0
        for i in range(len(s)):
            if s[i] not in substring:
                substring += s[i]
                max_length = max(max_length, len(substring))
            else:
                remove = substring.index(s[i])
                substring = substring[remove+1:] + s[i]
        return max_length
    
s = Solution()
print(s.lengthOfLongestSubstring('ahamed'))
# @lc code=end

