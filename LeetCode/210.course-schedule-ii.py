#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#
from typing import List
# @lc code=start
class Solution(object):
    def dfs(self, course, prereq, visited, stack):
        if visited[course] == -1:
            return False
        if visited[course] == 1:
            return True
        visited[course] = -1
        for pre in prereq[course]:
            if not self.dfs(pre, prereq, visited, stack):
                return False
        visited[course] = 1
        stack.append(course)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        prereq = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        visited = [0] * numCourses
        stack = []
        for course in range(numCourses):
            if not self.dfs(course, prereq, visited, stack):
                return []
        return stack[::-1]
# @lc code=end

solution = Solution()
print(solution.findOrder(2, [[1,0]]))