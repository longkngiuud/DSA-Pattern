# Pivot Integer

## Problem

Find the pivot integer `x` such that:

```text
1 + 2 + ... + (x - 1) = (x + 1) + ... + n
```

Return `x`, otherwise return `-1`.

Example:

```text
n = 8

1 + 2 + 3 + 4 + 5 = 15
7 + 8             = 15

Therefore:
pivot = 6
```

---

## Brute Force Approach

Try every number as the pivot.

```python
def pivotInteger(n):
    arr = [x for x in range(1, n + 1)]
    size = len(arr)

    for pivot in range(size):
        left = sum(arr[:pivot])
        right = sum(arr[pivot + 1:])

        if left == right:
            return arr[pivot]

    return -1
```

### Why is this brute force?

For every possible pivot, we recalculate the entire left and right sums.

```text
Try pivot 1 → calculate left + right
Try pivot 2 → calculate left + right again
Try pivot 3 → calculate left + right again
...
```

Each iteration can take `O(n)` because `sum()` has to traverse the elements.

There are `n` possible pivots.

Therefore:

```text
Time:  O(n²)
Space: O(n)
```

The main problem is **repeated work**.

---

# 1. Optimized Two-Pointer / Running-Sum Approach

Instead of testing every pivot independently, maintain:

```python
leftValue
rightValue
leftSum
rightSum
```

The idea is to grow the side with the smaller sum.

```python
def pivotInteger(n):
    if n == 1:
        return n

    leftValue = 1
    rightValue = n

    leftSum = leftValue
    rightSum = rightValue

    while leftValue < rightValue:

        if leftSum < rightSum:
            leftValue += 1
            leftSum += leftValue

        else:
            rightValue -= 1
            rightSum += rightValue

        if leftSum == rightSum and leftValue + 1 == rightValue - 1:
            return leftValue + 1

    return -1
```

---

## Core Idea

Think of the array:

```text
1  2  3  4  5  6  7  8
↑                    ↑
L                    R
```

`leftValue` represents the largest number currently included in the left sum.

`rightValue` represents the largest number currently included in the right sum.

The actual pivot is the number **between** them.

---

## Rule 1 — Left sum is smaller

If:

```python
leftSum < rightSum
```

move the left boundary forward:

```python
leftValue += 1
leftSum += leftValue
```

Why?

Because the left side needs more value.

Example:

```text
leftSum  = 6
rightSum = 8
```

Add the next left number:

```text
leftValue = 4
leftSum = 6 + 4 = 10
```

---

## Rule 2 — Right sum is smaller or equal

Otherwise:

```python
else:
    rightValue -= 1
    rightSum += rightValue
```

Move the right boundary backward.

For example:

```text
rightValue = 8
rightSum   = 8
```

Move right boundary:

```text
rightValue = 7
rightSum = 8 + 7 = 15
```

We are building the right sum backwards:

```text
8
8 + 7
8 + 7 + 6
...
```

---

# Full Trace for n = 8

Initial state:

```text
leftValue  = 1
rightValue = 8

leftSum  = 1
rightSum = 8
```

### Step 1

```text
1 < 8
```

Move left:

```text
leftValue = 2
leftSum = 1 + 2 = 3
```

State:

```text
leftValue  = 2
rightValue = 8
leftSum    = 3
rightSum   = 8
```

---

### Step 2

```text
3 < 8
```

Move left:

```text
leftValue = 3
leftSum = 3 + 3 = 6
```

State:

```text
leftValue  = 3
rightValue = 8
leftSum    = 6
rightSum   = 8
```

---

### Step 3

```text
6 < 8
```

Move left:

```text
leftValue = 4
leftSum = 6 + 4 = 10
```

State:

```text
leftValue  = 4
rightValue = 8
leftSum    = 10
rightSum   = 8
```

Now the left sum is bigger.

---

### Step 4

```text
10 < 8 → False
```

Move right:

```text
rightValue = 7
rightSum = 8 + 7 = 15
```

State:

```text
leftValue  = 4
rightValue = 7

leftSum  = 10
rightSum = 15
```

---

### Step 5

Now:

```text
10 < 15
```

Move left:

```text
leftValue = 5
leftSum = 10 + 5 = 15
```

State:

```text
leftValue  = 5
rightValue = 7

leftSum  = 15
rightSum = 15
```

The sums are equal.

Now check:

```python
leftValue + 1 == rightValue - 1
```

```text
5 + 1 == 7 - 1
6     == 6
```

Therefore:

```text
pivot = 6
```

---

# Visual Understanding

At the moment we find the answer:

```text
1  2  3  4  5  [6]  7  8
---------       -------
   LEFT          RIGHT
```

The sums are:

```text
LEFT:
1 + 2 + 3 + 4 + 5 = 15

RIGHT:
7 + 8 = 15
```

The number between the two boundaries is:

```text
6
```

So:

```python
return leftValue + 1
```

---

# Why `leftValue + 1` Is the Pivot

When:

```text
leftValue = 5
rightValue = 7
```

the only number between them is:

```text
6
```

Therefore:

```python
pivot = leftValue + 1
```

We can also see that:

```python
leftValue + 1 == rightValue - 1
```

guarantees that there is exactly **one number between the boundaries**.

---

# Important Mental Model

Do NOT think:

```text
leftValue = pivot
rightValue = pivot
```

Instead think:

```text
leftValue        pivot        rightValue
     ↓             ↓               ↓
1  2  3  4  5     6     7  8
```

The algorithm expands the two sides until:

```text
leftSum == rightSum
```

and the two boundaries have exactly one number between them.

That number is the pivot.

# 2. Math Arithmetic

- with formula: square root of (n x (n + 1)) // 2
- total sum of the whole array : (n x (n + 1)) // 2
- And the pivot is the square root of that total_sum
- if that pivot x pivot == total_sum then return the pivot , otherwise -1

---

# Complexity

We never recalculate a sum from scratch.

Each number is added to either `leftSum` or `rightSum` at most once.

Therefore:

```text
Time:  O(n)
Space: O(1)
```

This is an improvement over the brute-force solution:

```text
Brute Force:
O(n²) time
O(n)  space

Optimized:
O(n)  time
O(1)  space
```

---

# Pattern to Remember

This problem demonstrates:

- Two pointers
- Running sums
- Avoiding repeated calculations
- Greedily moving the side with the smaller sum

The general thought process is:

```text
1. Identify two sides.
2. Maintain the sum of each side.
3. Never recalculate the sums.
4. Move the side with the smaller sum.
5. Stop when the two sums become equal.
```

The important optimization is:

> **Don't repeatedly calculate the same information. Maintain it incrementally.**
