# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_max = total = float('-inf')
        for num in nums:
            total = max(total + num, num)
            running_max = max(running_max, total)
        return running_max
