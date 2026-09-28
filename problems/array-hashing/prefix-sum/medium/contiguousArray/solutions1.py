
from ast import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        diff_index = {} #diff -> index = count[1] - count[0] -> index
        res = 0

        for i, num in enumerate(nums):
            if num == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in diff_index:
                diff_index[one - zero] = i

            if one == zero:
                res = one + zero

            else: # one - zero in diff_index
                idx = diff_index[one - zero]
                res = max(res, i - idx)

        return res


        