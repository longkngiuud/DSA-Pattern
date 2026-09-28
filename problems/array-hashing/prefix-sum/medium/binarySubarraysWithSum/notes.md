# Binary Subarrays With Sum

**Problem:** Given a binary array `nums` and integer `goal`, count the number of non-empty subarrays with sum exactly `goal`.

Example: `nums = [1,0,1,0,1]`, `goal = 2` → `4` subarrays.

---

## Approach 1: Prefix Sum + HashMap

**Idea:** `prefix[i] - prefix[j] = goal` means the subarray between `j+1` and `i` sums to `goal`.
Track how many times each prefix sum has occurred; for each new prefix sum, check how many earlier prefix sums equal `prefix - goal`.

```python
def numSubarraysWithSum(nums, goal):
    count = {0: 1}      # prefix_sum -> frequency
    prefix = 0
    result = 0
    for num in nums:
        prefix += num
        result += count.get(prefix - goal, 0)
        count[prefix] = count.get(prefix, 0) + 1
    return result
```

- **Time:** O(n)
- **Space:** O(n)
- Works even if the array weren't binary (general subarray-sum-equals-k technique).

---

## Approach 2: Sliding Window

**Idea:** Since values are only 0/1, sums are monotonic as the window grows, so two pointers work.
Count subarrays with sum `== goal` as `atMost(goal) - atMost(goal - 1)`, where `atMost(k)` = number of subarrays with sum `≤ k`.

```python
def numSubarraysWithSum(nums, goal):
    def atMost(k):
        if k < 0:
            return 0
        left = 0
        window_sum = 0
        count = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum > k:
                window_sum -= nums[left]
                left += 1
            count += right - left + 1   # all subarrays ending at 'right' within window
        return count

    return atMost(goal) - atMost(goal - 1)
```

- **Time:** O(n) (two passes of `atMost`, each O(n))
- **Space:** O(1)
- The `atMost(k) - atMost(k-1)` trick is the standard way to turn a "sum ≤ k" sliding window into an "sum == k" counter — useful whenever values are non-negative.

---

## Which to use

- **Prefix sum + hashmap:** works for any integers (positive or negative), one pass, O(n) space.
- **Sliding window:** faster in practice (no hashing), O(1) space, but **only works when all values are non-negative** (so the window sum is monotonic).
