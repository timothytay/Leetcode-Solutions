class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = {}
        for i in range(len(position)):
            times[position[i]] = (target - position[i]) / speed[i]
        position.sort(reverse=True)
        fleets = 0
        max_time = 0
        for p in position:
            if max_time < times[p]:
                fleets += 1
                max_time = times[p]
            
        return fleets