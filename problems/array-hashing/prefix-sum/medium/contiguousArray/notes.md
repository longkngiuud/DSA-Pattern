# Contiguous Array (LeetCode 525) — Hashmap Prefix-Sum Approach: Two Solutions Compared

Both solutions solve the problem of finding the **longest subarray with an equal number of 0s and 1s**, using the same core trick — turning "equal count of 0s and 1s" into "two equal prefix sums" — but they differ in how they track that sum and how they handle the edge case where the whole prefix is already balanced.

## The core idea (shared by both)

If you treat every `1` as `+1` and every `0` as `-1`, then a subarray `nums[j+1..i]` has equal 0s and 1s exactly when the running sum at `i` equals the running sum at `j`. So:

1. Keep a running "balance" as you scan.
2. Store the **first** index at which each balance value occurred.
3. If you see that balance again at index `i`, the subarray between the first occurrence and `i` is balanced — check if it's the longest one so far.

## Solution 1 — separate `zero`/`one` counters + special case

```python
from ast import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        diff_index = {}  # diff -> index = count[1] - count[0] -> index
        res = 0

        for i, num in enumerate(nums):
            if num == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in diff_index:
                diff_index[one - zero] = i

            if one == zero:
                res = one + zero
            else:  # one - zero in diff_index
                idx = diff_index[one - zero]
                res = max(res, i - idx)

        return res
```

- Tracks `zero` and `one` counts separately; the effective balance is `one - zero`.
- **No sentinel** for balance `0`. Instead it special-cases it: whenever `one == zero`, the whole prefix `nums[0..i]` is balanced, so `res = one + zero` (i.e. `i + 1`) directly — no map lookup needed.
- For any other balance, it looks up the first index where that balance occurred and computes the length.

## Solution 2 — single running `count` + sentinel `{0: -1}`

```python
from ast import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = {}
        diff[0] = -1
        count = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in diff:
                ans = max(ans, i - diff[count])
            else:
                diff[count] = i

        return ans
```

- Tracks one `count` variable (`+1` for `1`, `-1` for `0`) — same value as `one - zero`.
- Pre-seeds the map with `diff[0] = -1`. This is the classic trick: it represents "balance 0 occurred at the imaginary index before the array starts."
- Because of that sentinel, the "whole prefix is balanced" case is handled automatically by the normal lookup (`i - (-1) = i + 1`), so **no special case is needed anywhere** in the loop.

## Key differences

| Aspect                  | Solution 1                                                                                | Solution 2                                             |
| ----------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Balance tracking        | Two counters (`zero`, `one`)                                                              | One counter (`count`)                                  |
| Handling balance = 0    | Explicit `if one == zero` branch                                                          | Handled by sentinel `{0: -1}` in the map               |
| Code complexity         | Slightly more verbose, extra branch                                                       | Cleaner, single unified case                           |
| Insert-then-check order | Inserts current diff into map _before_ checking the special case (redundant but harmless) | Only inserts when the count is new (in the `else`)     |
| Time complexity         | O(n)                                                                                      | O(n)                                                   |
| Space complexity        | O(n)                                                                                      | O(n)                                                   |
| Correctness             | Correct — the special case exactly compensates for not having a sentinel                  | Correct — sentinel removes the need for a special case |

They are **algorithmically identical**; Solution 2 is just the more idiomatic version because the `{0: -1}` sentinel eliminates a branch.

## Step-by-step trace (both, on the same input)

`nums = [0, 1, 0, 1, 1, 0]`

### Solution 2 (`count`, `diff = {0: -1}`)

| i   | num | count | in diff? | action             | ans   |
| --- | --- | ----- | -------- | ------------------ | ----- |
| 0   | 0   | -1    | no       | diff[-1]=0         | 0     |
| 1   | 1   | 0     | yes (-1) | ans=max(0, 1-(-1)) | 2     |
| 2   | 0   | -1    | yes (0)  | ans=max(2, 2-0)    | 2     |
| 3   | 1   | 0     | yes (-1) | ans=max(2, 3-(-1)) | 4     |
| 4   | 1   | 1     | no       | diff[1]=4          | 4     |
| 5   | 0   | 0     | yes (-1) | ans=max(4, 5-(-1)) | **6** |

### Solution 1 (`zero`, `one`, `diff = one-zero`)

| i   | num | zero | one | diff | one==zero?             | res   |
| --- | --- | ---- | --- | ---- | ---------------------- | ----- |
| 0   | 0   | 1    | 0   | -1   | no → idx=0             | 0     |
| 1   | 1   | 1    | 1   | 0    | **yes** → res=one+zero | 2     |
| 2   | 0   | 2    | 1   | -1   | no → idx=0             | 2     |
| 3   | 1   | 2    | 2   | 0    | **yes** → res=one+zero | 4     |
| 4   | 1   | 2    | 3   | 1    | no → idx=4             | 4     |
| 5   | 0   | 3    | 3   | 0    | **yes** → res=one+zero | **6** |

Both land on **6** — the entire array is balanced (three 0s at indices 0, 2, 5 and three 1s at indices 1, 3, 4), confirming the two approaches are equivalent, just structured differently.

## Takeaway

- The prefix-sum-with-hashmap pattern here is the same one used for "subarray sum equals k" problems.
- Solution 2's `{0: -1}` sentinel is the more elegant, reusable pattern — worth internalizing, since it removes an entire conditional branch that Solution 1 needs.
