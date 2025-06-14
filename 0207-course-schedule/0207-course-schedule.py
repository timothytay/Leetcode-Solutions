class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            
        
        def cycle(node, adj_list, seen, good):
            if node in good:
                return False
            if node in seen:
                return True
            seen.add(node)
            for nei in adj_list[node]:
                if cycle(nei, adj_list, seen, good):
                    return True
            seen.remove(node)
            good.add(node)
            return False

        for course in adj_list.keys():
            if cycle(course, adj_list, set(), set()):
                return False
        return True