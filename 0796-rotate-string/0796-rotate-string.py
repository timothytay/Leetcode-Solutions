class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        twoS = 2 * s
        return twoS.find(goal) != -1