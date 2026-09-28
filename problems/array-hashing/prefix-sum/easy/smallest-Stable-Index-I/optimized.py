def na(nums, k):
    n = len(nums)

    suf = [0] * 100
    suf[n-1] = nums[n-1]

    for i in range(n-2, -1, -1):
        suf[i] = min(nums[i], suf[i+1])

    mx = 0
    for i, x in enumerate(nums):
        mx = max(mx, x)
        if mx - suf[i] <= k:
            return i

    return -1




if __name__ == '__main__':
    nums = [5,0,1,4]
    k = 3
    print(na(nums, k))
