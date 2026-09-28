def countPartition(nums):
    n = len(nums)
    count = 0

    total_sum = sum(nums)

    leftSum = 0
    for i in range(n - 1):
        leftSum += nums[i]

        rightSum = total_sum - leftSum

        if (leftSum - rightSum) % 2 == 0:
            count += 1

    return count


if __name__ == '__main__':
    nums = [10,10,3,7,6]
    print(countPartition(nums))
