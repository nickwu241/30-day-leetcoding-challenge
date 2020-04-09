# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def handle_backspace(char_arr, i):
            accumulated_backspaces = 0
            while True:
                if i >= 0 and char_arr[i] == '#':
                    accumulated_backspaces += 1
                elif accumulated_backspaces > 0:
                    accumulated_backspaces -= 1
                else:
                    return i
                i -= 1
                
        s_i = len(S) - 1
        t_i = len(T) - 1
        while True:
            s_i = handle_backspace(S, s_i)
            t_i = handle_backspace(T, t_i)
            if s_i < 0 or t_i < 0:
                return s_i < 0 and t_i < 0
            if S[s_i] != T[t_i]:
                return False
            s_i -= 1
            t_i -= 1
