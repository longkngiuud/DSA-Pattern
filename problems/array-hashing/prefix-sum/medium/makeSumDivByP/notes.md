# 1590. Make Sum Divisible by P — Minimum Subarray to Remove

## Goal

Remove the **shortest** subarray so the remaining sum is divisible by `p`.
Return `-1` if impossible (only if removing the _whole array_ is required).

## Key idea

Let `target = total_sum % p`.

- If `target == 0` → already divisible, answer is `0`.
- Otherwise, find the shortest subarray whose sum `% p == target`.
  Removing it leaves a sum divisible by `p`.

## Why subarray sum ≡ target

```
subarray_sum = current_sum - prefix[j]   (mod p)
we need subarray_sum % p == target
=> prefix[j] % p == (current_sum - target) % p   <-- "needed"
```

So for each index `i`, compute `needed = (current_sum - target) % p` and check
if that remainder was seen before (in `mod_map`). If yes, subarray length =
`i - mod_map[needed]`.

⚠️ Order matters: it's `current_sum - target`, NOT `target - current_sum`
(mod isn't symmetric — flipping gives the wrong bucket).

## Python `%` note

Python's `%` always returns non-negative for a positive modulus, so
`(x - y) % p` and `(x - y + p) % p` are equivalent in Python. The `+ p` is
just a defensive habit from languages like C++/Java where negative `%` stays
negative — harmless here, but redundant.

## mod_map trick

- `mod_map = {0: -1}` handles the case where the needed prefix is "before
  the array starts" (i.e., subarray from index 0).
- Store `current_sum % p → index` as you go, always overwrite with the
  latest index (keeps subarrays as short as possible).

## Complexity

- Time: O(n)
- Space: O(min(n, p)) for the mod map

## Edge cases

- If required subarray length == `n` (whole array), that's invalid → return `-1`.
- `target == 0` before the loop even starts → return `0` immediately.
