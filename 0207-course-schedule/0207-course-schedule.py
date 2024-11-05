from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjList = {}
        for course, prereq in prerequisites:
            if course not in adjList:
                adjList[course] = []
            if prereq not in adjList:
                adjList[prereq] = []
            adjList[course].append(prereq)

        visited = {}
        def dfs(node, visit):
            if node in visit:
                if visit[node] == 1:
                    return False
                if visit[node] == 2:
                    return True
            visit[node] = 1
            for neighbor in adjList[node]:
                if not dfs(neighbor, visit):
                    return False
            visit[node] = 2
            return True

        for course in range(numCourses):
            if course not in adjList:
                continue
            if not dfs(course, visited):
                return False
            
        return True
        
        
