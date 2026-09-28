
from ast import List


def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    n = len(nums)

    for i in range(n):
        total = 0

        for j in range(i, n):
            total += nums[j]

            if j - i + 1 >= 2 and total % k == 0:
                return True

    return False

# Why we j - i + 1 >= 2? Because we need to check if the length of the subarray is at least 2. The length of the subarray is calculated as j - i + 1, where j is the end index and i is the start index. If this length is greater than or equal to 2, it means we have a valid subarray to check for the sum condition.
# and index start from 0 and elements start from 1, so we need to add 1 to the length of the subarray.