def numSubarraysWithSum(nums, goal):
    def at_most(k):

        left, current_sum, total_sum = 0, 0, 0
        if k < 0:
            return 0

        for right, x in enumerate(nums):
            current_sum += x

            while current_sum > k:
                current_sum -= nums[left]
                left += 1
            
            total_sum += right - left + 1
        return total_sum


    return at_most(goal) - at_most(goal - 1)