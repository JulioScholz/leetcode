#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        soma: int = 0
        tam: int = len(s)
        for i in range(0, tam):
            c: str = s[i]
            if c == "I":
                if i + 1 < tam and (s[i + 1] == "V" or s[i + 1] == "X"):
                    soma -= 1
                else:
                    soma += 1
            elif c == "V":
                soma += 5
            elif c == "X":
                if i + 1 < tam and (s[i + 1] == "L" or s[i + 1] == "C"):
                    soma -= 10
                else:
                    soma += 10
            elif c == "L":
                soma += 50
            elif c == "C":
                if i + 1 < tam and (s[i + 1] == "D" or s[i + 1] == "M"):
                    soma -= 100
                else:
                    soma += 100
            elif c == "D":
                soma += 500
            elif c == "M":
                soma += 1000
        return soma


# @lc code=end
