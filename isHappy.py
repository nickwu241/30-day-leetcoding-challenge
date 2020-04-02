# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            sum_of_squares = sum(int(digit) ** 2 for digit in str(n))
            if sum_of_squares == 1:
                return True

            if sum_of_squares in seen:
                # Detected a cycle
                return False
            
            seen.add(sum_of_squares)
            n = sum_of_squares
