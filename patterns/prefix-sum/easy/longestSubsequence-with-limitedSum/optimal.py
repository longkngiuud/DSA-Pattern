def sub(nums, queries):
    nums.sort()
    n = len(nums)
    m = len(queries)
    ans = [0] * n
    ans[0] = nums[0]
    for i in range(1, n):
        ans[i] = ans[i - 1] + nums[i]

    res = []
    for i in range(m):
        k = binarySearch(ans, queries[i])
        res.append(k)


    return res

def binarySearch(arr, k):
    left = 0
    right = len(arr)

    while left < right:

        mid = (left + right) // 2

        if arr[mid] <= k:
            left = mid + 1
        else:
            right = mid

    return left




if __name__ == '__main__':
    nums =  nums = [4,5,2,1]
    queries = [3,10,21]
    print(sub(nums, queries))
