# Sliding Window

## What it is

Keep a **window** (a contiguous range `[left, right]`) over an array/string and **slide it** instead of recomputing from scratch.
Turns nested-loop **O(n·k)** / **O(n²)** into **O(n)** by adding the new element and removing the old one.

## When to use

- Problem asks about a **contiguous subarray / substring**
- Keywords: _longest, shortest, maximum, minimum, at most K, exactly K, contains all, no repeats_
- A running value (sum, count, frequency map) can be **updated incrementally**

## Type 1: Fixed size (window length = k)

Build the first window, then slide: add `nums[i]`, remove `nums[i-k]`.

```python
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]   # add new, drop old
        best = max(best, window_sum)
    return best
```

## Type 2: Dynamic size (window grows/shrinks)

Expand `right` every step. **Shrink `left` while the window is invalid.** Update the answer when valid.

```python
def dynamic_window(s):
    left = 0
    state = {}                      # sum / count / freq map
    best = 0
    for right in range(len(s)):
        # 1. add s[right] to state
        while INVALID(state):       # 2. shrink until valid again
            # remove s[left] from state
            left += 1
        best = max(best, right - left + 1)   # 3. update answer
    return best
```

- **Longest** window: update answer _after_ the while loop
- **Shortest** window: update answer _inside_ the loop while the window is valid, then shrink

## Complexity

- Time: **O(n)**. Each pointer moves forward at most n times, so `left` and `right` together make at most 2n moves
- Space: **O(1)** for sums/counters, **O(k)** or **O(alphabet)** for a hash map

## Common pitfalls

- Forgetting to **remove** the outgoing element from the state
- Shrinking with `if` instead of `while`
- Negative numbers break sum-based windows (shrinking no longer reduces the sum), so use prefix sum + hash map instead
- Off-by-one: window length is `right - left + 1`
- "Exactly K" = `atMost(K) - atMost(K-1)`

## Practice (easy to hard)

**Fixed:** Maximum Average Subarray I, Maximum Number of Vowels in a Substring of Given Length, Permutation in String, Find All Anagrams in a String
**Dynamic:** Longest Substring Without Repeating Characters, Minimum Size Subarray Sum, Max Consecutive Ones III, Longest Repeating Character Replacement, Fruit Into Baskets, Minimum Window Substring
**Related:** Sliding Window Maximum (monotonic deque), Sliding Window Median (two heaps)
