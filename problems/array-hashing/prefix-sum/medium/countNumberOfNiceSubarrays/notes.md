# Count Number of Nice Subarrays

**Problem:** Given an array `nums` and integer `k`, count the number of subarrays with exactly `k` odd numbers.

Example: `nums = [1,1,2,1,1]`, `k = 3` → `2` subarrays (`[1,1,2,1]`, `[1,2,1,1]`).

**Key trick:** Map each element to `1` if odd, `0` if even. Now this is _identical_ to "Binary Subarrays With Sum" with `goal = k`.

---

## Approach 1: Prefix Sum + HashMap

**Idea:** `prefix[i]` = count of odd numbers seen so far. Subarray `(j, i]` is nice if `prefix[i] - prefix[j] = k`.

```python
def numberOfSubarrays(nums, k):
    count = {0: 1}      # prefix_odd_count -> frequency
    prefix = 0
    result = 0
    for num in nums:
        prefix += num % 2          # 1 if odd, 0 if even
        result += count.get(prefix - k, 0)
        count[prefix] = count.get(prefix, 0) + 1
    return result
```

- **Time:** O(n)
- **Space:** O(n)

---

## Approach 2: Sliding Window

**Idea:** Count of odds in a window only increases as the window grows, so `atMost(k)` is monotonic → two pointers work.
`exactly(k) = atMost(k) - atMost(k - 1)`

```python
def numberOfSubarrays(nums, k):
    def atMost(k):
        if k < 0:
            return 0
        left = 0
        odd_count = 0
        count = 0
        for right in range(len(nums)):
            odd_count += nums[right] % 2
            while odd_count > k:
                odd_count -= nums[left] % 2
                left += 1
            count += right - left + 1
        return count

    return atMost(k) - atMost(k - 1)
```

- **Time:** O(n)
- **Space:** O(1)

---

## Which to use

- Same trade-off as Binary Subarrays With Sum: hashmap works generally, sliding window is O(1) space and relies on the "odd count" being non-negative and monotonic (always true here).
- Recognizing that **"exactly k odds" = "binary subarray sum = k"** after the odd/even → 1/0 mapping is the core insight — same pattern, different disguise.
