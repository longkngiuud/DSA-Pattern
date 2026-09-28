# 3903. Smallest Stable Index I

## Problem

Given an integer array `nums` and an integer `k`.

For every index `i`, define its **instability score**:

```text
max(nums[0..i]) - min(nums[i..n-1])
```

An index `i` is **stable** if:

```text
max(nums[0..i]) - min(nums[i..n-1]) <= k
```

Return the **smallest stable index**.

If no stable index exists, return `-1`.

---

# Example

```text
nums = [5, 0, 1, 4]
k = 3
```

For each index:

```text
i = 0
max([5]) - min([5,0,1,4])
= 5 - 0
= 5

i = 1
max([5,0]) - min([0,1,4])
= 5 - 0
= 5

i = 2
max([5,0,1]) - min([1,4])
= 5 - 1
= 4

i = 3
max([5,0,1,4]) - min([4])
= 5 - 4
= 1
```

Since `1 <= 3`, index `3` is stable.

```text
Answer = 3
```

---

# 1. Brute Force Approach

For every index `i`:

1. Find the maximum from `0` to `i`.
2. Find the minimum from `i` to `n - 1`.
3. Calculate the instability score.
4. If it is `<= k`, return `i`.

```python
def stable_index(nums, k):
    n = len(nums)

    for i in range(n):
        left_max = max(nums[0:i+1])
        right_min = min(nums[i:n])

        if left_max - right_min <= k:
            return i

    return -1
```

## Why is this slow?

For every index, we scan parts of the array again.

For example:

```text
i = 0 → scan array
i = 1 → scan array
i = 2 → scan array
...
```

There is a lot of repeated work.

### Time Complexity

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

---

# 2. Key Observation

Look carefully at the two parts of the formula:

```text
max(nums[0..i])
min(nums[i..n-1])
```

The first part is a **prefix**.

The second part is a **suffix**.

Therefore, we can preprocess them.

```text
                    i
                    ↓
nums = [5, 0, 1, 4]
        └────┘      └────┘
       PREFIX       SUFFIX

max(nums[0..i])    min(nums[i..n-1])
```

We can create:

```text
prefix_max[i]
suffix_min[i]
```

Then each index can be checked in `O(1)`.

---

# 3. What Is a Prefix?

A prefix is the part of an array from the beginning up to some index.

For:

```text
nums = [5, 0, 1, 4]
```

the prefixes are:

```text
i = 0 → [5]

i = 1 → [5, 0]

i = 2 → [5, 0, 1]

i = 3 → [5, 0, 1, 4]
```

We need:

```text
max(nums[0..i])
```

So we create:

```text
prefix_max
```

For this example:

```text
prefix_max = [5, 5, 5, 5]
```

Because:

```text
prefix_max[0] = max(5) = 5

prefix_max[1] = max(5,0) = 5

prefix_max[2] = max(5,0,1) = 5

prefix_max[3] = max(5,0,1,4) = 5
```

---

# 4. What Is a Suffix?

A suffix is the part of an array from some index to the end.

For:

```text
nums = [5, 0, 1, 4]
```

the suffixes are:

```text
i = 0 → [5, 0, 1, 4]

i = 1 → [0, 1, 4]

i = 2 → [1, 4]

i = 3 → [4]
```

We need:

```text
min(nums[i..n-1])
```

So we create:

```text
suffix_min
```

For this example:

```text
suffix_min = [0, 0, 1, 4]
```

Because:

```text
suffix_min[3] = min(4) = 4

suffix_min[2] = min(1,4) = 1

suffix_min[1] = min(0,1,4) = 0

suffix_min[0] = min(5,0,1,4) = 0
```

---

# 5. Why Do We Build suffix_min Right-to-Left?

This is an important property of suffix arrays.

We want:

```text
suffix_min[i] = min(nums[i:])
```

But:

```text
nums[i:] = nums[i] + nums[i+1:]
```

Therefore:

```text
suffix_min[i] = min(nums[i], suffix_min[i+1])
```

So we need `suffix_min[i+1]` first.

That means we process from **right to left**.

Example:

```text
nums = [5, 0, 1, 4]
```

Start with the last element:

```text
suffix_min[3] = 4
```

Then:

```text
suffix_min[2] = min(nums[2], suffix_min[3])
             = min(1, 4)
             = 1
```

Then:

```text
suffix_min[1] = min(nums[1], suffix_min[2])
             = min(0, 1)
             = 0
```

Then:

```text
suffix_min[0] = min(nums[0], suffix_min[1])
             = min(5, 0)
             = 0
```

Result:

```text
suffix_min = [0, 0, 1, 4]
```

---

# 6. Your Optimized Solution

Your solution:

```python
def na(nums, k):
    n = len(nums)

    suf = [0] * 100
    suf[n-1] = nums[n-1]

    for i in range(n-2, -1, -1):
        suf[i] = min(nums[i], suf[i+1])

    mx = 0
    for i, x in enumerate(nums):
        mx = max(mx, x)

        if mx - suf[i] <= k:
            return i

    return -1
```

The important thing is that you actually don't need a separate `prefix_max` array.

You only need:

```text
suffix_min
```

because you can calculate the prefix maximum while scanning from left to right.

---

# 7. Why We Don't Need prefix_max[]

Instead of creating:

```python
prefix_max = [0] * n
```

you maintain one variable:

```python
mx = 0
```

At every index:

```python
mx = max(mx, x)
```

Therefore:

```text
mx
```

always represents:

```text
max(nums[0..i])
```

Example:

```text
nums = [5, 0, 1, 4]

i = 0
mx = max(0, 5) = 5

i = 1
mx = max(5, 0) = 5

i = 2
mx = max(5, 1) = 5

i = 3
mx = max(5, 4) = 5
```

So we effectively have a prefix maximum without storing the whole array.

This reduces the extra space.

---

# 8. Full Optimized Solution

A slightly cleaner version of your solution:

```python
def stable_index(nums, k):
    n = len(nums)

    # Build suffix minimum
    suf = [0] * n
    suf[n - 1] = nums[n - 1]

    for i in range(n - 2, -1, -1):
        suf[i] = min(nums[i], suf[i + 1])

    # Scan from left to right
    mx = 0

    for i, x in enumerate(nums):
        mx = max(mx, x)

        if mx - suf[i] <= k:
            return i

    return -1
```

---

# 9. Trace the Optimized Solution

```text
nums = [5, 0, 1, 4]
k = 3
```

First build:

```text
suf = [0, 0, 1, 4]
```

Now scan from left to right.

### i = 0

```text
x = 5

mx = max(0, 5)
   = 5

instability = mx - suf[0]
             = 5 - 0
             = 5
```

```text
5 > 3
```

Not stable.

---

### i = 1

```text
x = 0

mx = max(5, 0)
   = 5

instability = 5 - suf[1]
             = 5 - 0
             = 5
```

Not stable.

---

### i = 2

```text
x = 1

mx = max(5, 1)
   = 5

instability = 5 - suf[2]
             = 5 - 1
             = 4
```

Not stable.

---

### i = 3

```text
x = 4

mx = max(5, 4)
   = 5

instability = 5 - suf[3]
             = 5 - 4
             = 1
```

```text
1 <= 3
```

Stable!

Return:

```text
3
```

---

# 10. Why This Is Correct

At every index `i`:

```python
mx
```

contains:

```text
max(nums[0..i])
```

and:

```python
suf[i]
```

contains:

```text
min(nums[i..n-1])
```

Therefore:

```python
mx - suf[i]
```

is exactly the instability score defined by the problem.

So:

```python
if mx - suf[i] <= k:
```

correctly checks whether `i` is stable.

Because we scan:

```python
for i in range(n):
```

from left to right, the **first** stable index we find is automatically the **smallest** stable index.

---

# 11. Why Can We Return Immediately?

The problem asks for:

```text
the smallest stable index
```

So we check:

```text
0 → 1 → 2 → 3 → ...
```

As soon as we find:

```text
instability <= k
```

we know that no smaller index can be the answer, because we already checked them.

Therefore:

```python
return i
```

is correct.

If we finish the entire array without finding one:

```python
return -1
```

---

# 12. Complexity

### Brute Force

```text
For each index:
    find max → O(n)
    find min → O(n)

n indices

Total = O(n²)
```

### Optimized

Build suffix minimum:

```text
O(n)
```

Scan array while maintaining `mx`:

```text
O(n)
```

Total:

```text
O(n)
```

Extra space:

```text
O(n)
```

because of `suf`.

---

# 13. Can We Do O(1) Extra Space?

Yes.

We could avoid storing the suffix array by scanning from the right and somehow combine the information, but for this problem the cleanest solution is the suffix array + running prefix maximum.

The `O(n)` space solution is already optimal enough for the constraints:

```text
n <= 100
```

The important algorithmic improvement is going from:

```text
O(n²)
```

to:

```text
O(n)
```

---

# 14. Pattern Recognition

This problem is a good example of **prefix/suffix preprocessing**.

When you see a formula like:

```text
max(nums[0..i]) - min(nums[i..n-1])
```

immediately break it into:

```text
max(nums[0..i])     → PREFIX
min(nums[i..n-1])   → SUFFIX
```

Then ask:

> Can I preprocess these values so I don't repeatedly scan the array?

Here the answer is yes.

General pattern:

```text
nums[0..i]      → prefix information
nums[i..n-1]    → suffix information
```

Examples of prefix information:

```text
prefix_sum
prefix_max
prefix_min
prefix_product
```

Examples of suffix information:

```text
suffix_sum
suffix_max
suffix_min
suffix_product
```

---

# 15. Important Difference: Prefix vs Suffix

Remember:

### Prefix

Starts from the **beginning**:

```text
nums[0..i]
```

Usually built:

```text
left → right
```

Example:

```python
prefix_max[i] = max(prefix_max[i - 1], nums[i])
```

### Suffix

Starts at `i` and goes to the **end**:

```text
nums[i..n-1]
```

Usually built:

```text
right → left
```

Example:

```python
suffix_min[i] = min(nums[i], suffix_min[i + 1])
```

---

# 16. The Core Idea

The most important thing to remember from this problem is:

```text
For every index i:

LEFT SIDE                  RIGHT SIDE
nums[0..i]                 nums[i..n-1]
     ↓                           ↓
  prefix                    suffix
     ↓                           ↓
  maximum                     minimum
```

So:

```text
instability(i)
=
prefix maximum
-
suffix minimum
```

Instead of repeatedly calculating:

```python
max(nums[0:i+1])
min(nums[i:n])
```

we preprocess the suffix minimum and maintain the prefix maximum while scanning.

Final structure:

```python
# Preprocess the right side
suffix_min = ...

# Scan the left side
mx = 0

for i in range(n):
    mx = max(mx, nums[i])

    if mx - suffix_min[i] <= k:
        return i

return -1
```

### Pattern to put in your memory

> **If a problem asks for something about `nums[0..i]` and something else about `nums[i..n-1]` for every index, think PREFIX + SUFFIX preprocessing.**
