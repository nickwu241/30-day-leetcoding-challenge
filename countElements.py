# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/
from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        return sum(counts for num, counts in counter.items() if num+1 in counter)
