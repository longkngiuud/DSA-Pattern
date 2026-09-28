class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total = 0
        for i in range(n):
            start = n - i
            end = i + 1
            total_sub = start * end
            odd = total_sub // 2

            if (total_sub % 2) != 0:
                odd += 1

            total += odd * arr[i]

        return total 

