class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp1 = nums[:-1]
        dp2 = nums[1:]

        for i in range(len(dp1)-3, -1, -1):
            dp1[i] = dp1[i] + max(dp1[i+2], dp1[i+3] if i + 3 < len(dp1) else 0)

        for i in range(len(dp2)-3, -1, -1):
            dp2[i] = dp2[i] + max(dp2[i+2], dp2[i+3] if i + 3 < len(dp1) else 0)

        return max(dp1[0] if dp1 else 0, dp1[1] if len(dp1) > 1 else 0, dp2[0] if dp2 else 0, dp2[1] if len(dp2) > 1 else 0)