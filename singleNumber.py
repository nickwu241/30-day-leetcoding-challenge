# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
import functools
import opeerator

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(operator.xor, nums)
