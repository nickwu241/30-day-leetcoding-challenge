# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = defaultdict(list)
        ascii_value_a = ord('a')
        for s in strs:
            clist = [0]*26
            for c in s:
                clist[ord(c) - ascii_value_a] += 1
            anagram_groups[tuple(clist)].append(s)
        return list(anagram_groups.values())
