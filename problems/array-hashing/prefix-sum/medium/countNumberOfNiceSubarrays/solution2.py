def numberOfSubarrays(nums, k):
    def at_most(k):
        current_sum, left, subarray = 0, 0, 0

        if k < 0:
            return 0

        for right, x in enumerate(nums):
            current_sum += x % 2

            while current_sum > k:
                current_sum -= nums[left] % 2
                left += 1

            subarray += right - left + 1
        return subarray

    exact_k = at_most(k) - at_most(k - 1)
    return exact_k