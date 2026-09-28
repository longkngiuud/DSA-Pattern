def subarraySum(nums):
    n = len(nums)
    prefix_sum = [float("inf")] * n
    prefix_sum[0] = nums[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    ans = 0
    for i in range(n):
        start = max(0, i - nums[i])

        if start == 0:
            ans += prefix_sum[i]

        else:
            ans += prefix_sum[i] - prefix_sum[start - 1]



    return ans
if __name__ == '__main__':
    nums = [2, 3, 1]
    print(subarraySum(nums))
