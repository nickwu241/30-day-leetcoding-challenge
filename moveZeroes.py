# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        target_i = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[target_i], nums[i] = nums[i], nums[target_i]
                target_i += 1
        return nums
