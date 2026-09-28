def numberOfSubarrays(nums, goal):
    current_sum = 0
    subarray = 0
    freq = {0: 1}

    for num in nums:

        current_sum += num

        previous_sum = current_sum - goal

        if previous_sum in freq:
            subarray += freq[previous_sum]


        freq[current_sum] = freq.get(current_sum, 0) + 1

    return subarray





if __name__ == "__main__":
    nums = [1,0,1,0,1]
    goal = 2
    print(numberOfSubarrays(nums, goal))
