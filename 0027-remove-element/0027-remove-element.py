class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # move along nums and find occurence of val
        # swap occurence of val with last value as long as the last value is not val
        # perhaps two pointers?
        # one pointer on the left, finding values nums
        # another pointer on the right, pointing to the rightmost value which is not nums
        # this way we can swap them effectively
        # then, when left and right pointer meet, we have taken care of everything 
        # in between 
        # which means k should be where the pointers meet, perhaps off by 1 or 2
        # I would like to simulate the procedure with an example to test that

        # some edge cases might be: empty list, no occurences of val, all occurences are val
        # val already at the back of array and first k elements are already not val
        # first elements are val consecutively

        # normal example might be: val = 2 [1, 2, 4, 2, 5]
        # left pointer at index 0, right at index 4
        # move left to index 1
        # find val
        # swap with 5
        # array becomes [1, 5, 4, 2, 2]
        # left at 2, right at 3
        # right has val, so move to 2
        # 2 is the end 
        # so k should be the location they meet + 1
        
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[r] == val:
                r -= 1
                continue
            elif nums[l] == val:
                nums[l] = nums[r]
                nums[r] = val
                r -= 1
            l += 1
        k = 0
        while k < len(nums) and nums[k] != val:
            k += 1
        return k
