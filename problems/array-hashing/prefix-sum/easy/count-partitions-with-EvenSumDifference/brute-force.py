class Solution(object):
    def countPartitions(self, nums):
        n = len(nums)
        count = 0


        leftSum = 0
        for i in range(n-1):
            leftSum += nums[i]


            rightSum = 0
            for j in range(i + 1, n):
                rightSum += nums[j]

            total = leftSum - rightSum

            if total % 2 == 0 :
                count += 1


        return count
        
         