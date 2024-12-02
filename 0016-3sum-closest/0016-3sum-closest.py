class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if abs(target - closest) > abs(target - (nums[i] + nums[j] + nums[k])):
                    closest = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return closest