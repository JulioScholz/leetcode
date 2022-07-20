#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tam: int = len(nums)
        if tam == 1:
            return True

        pos: int = 1
        while pos < tam and nums[pos] != 0:
            pos: int = pos + nums[pos]
            if pos >= tam:
                return True

        return False


# @lc code=end
