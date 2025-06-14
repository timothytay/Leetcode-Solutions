class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(cur_sum, arr, idx):
            if cur_sum > target:
                return
            elif cur_sum == target:
                ans.append(arr[:])
            else:
                for i in range(idx, len(candidates)):
                    num = candidates[i]
                    cur_sum += num
                    arr.append(num)
                    backtrack(cur_sum, arr, i)
                    cur_sum -= num
                    arr.pop()
        
        backtrack(0, [], 0)

        return ans