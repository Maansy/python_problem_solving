#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
from typing import List
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
            if len(path) == 4:
                return
            for i in range(1, 4):
                if start + i > len(s):
                    break
                if i > 1 and s[start] == '0':
                    break
                if int(s[start:start+i]) > 255:
                    break
                path.append(s[start:start+i])
                backtrack(start+i, path)
                path.pop()
        res = []
        backtrack(0, [])
        return res
        
# @lc code=end
s = Solution()
print(s.restoreIpAddresses("25525511135"))
