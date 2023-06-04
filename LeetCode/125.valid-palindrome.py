#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        lft_ptr , rgt_ptr = 0, len(s) -1
        while lft_ptr < rgt_ptr:
            while lft_ptr < rgt_ptr and not self.alphaNum(s[lft_ptr]):
                lft_ptr += 1
            
            while rgt_ptr > lft_ptr and not self.alphaNum(s[rgt_ptr]):
                rgt_ptr -= 1

            if s[lft_ptr].lower() != s[rgt_ptr].lower():
                return False
            lft_ptr, rgt_ptr = lft_ptr + 1, rgt_ptr - 1
        return True

    def alphaNum(self,c: str):
        return ((ord('A') <= ord(c) <= ord('Z')) or \
                    (ord('a') <= ord(c) <= ord('z')) or \
                        (ord('0') <= ord(c) <= ord('9')))
        
# @lc code=end

solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))