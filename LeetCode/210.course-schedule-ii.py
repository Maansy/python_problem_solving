#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
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
        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            visited[course] = 1
            stack.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return stack[::-1]
        
# @lc code=end

