
def leftRightDifference(nums):
    n = len(nums)
    ans = [0] * n

    leftSum = 0
    for i in range(n):
        ans[i] = leftSum
        leftSum += nums[i]

    rightSum = 0
    for i in range(n-1, -1, -1):
        ans[i] = abs(ans[i] - rightSum)
        rightSum += nums[i]

    return ans

if __name__ == "__main__":
    nums = [10, 4, 8, 3]
    print(leftRightDifference(nums))

'''
You are given a 0-indexed integer array nums of size n.

Define two arrays leftSum and rightSum where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.'''

'''
Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105'''