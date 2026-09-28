
from ast import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = {}
        diff[0] = -1
        count = 0
        ans = 0


        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in diff:
                ans = max(ans, i - diff[count])
            else:
                diff[count] = i



        return ans


       