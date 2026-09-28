def subarraysOdd(nums, k):
    current_sum = 0
    subarray = 0
    freq = {0 : 1}

    for num in nums:
        current_sum += num % 2

        previous_sum = current_sum - k

        if previous_sum in freq:
            subarray += freq[previous_sum]


        freq[current_sum] = freq.get(current_sum, 0) + 1

    return subarray



if __name__ == "__main__":
    nums = [1,1,2,1,1]
    k = 3

    print(subarraysOdd(nums, k))
