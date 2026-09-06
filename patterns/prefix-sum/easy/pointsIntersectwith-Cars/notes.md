# Points That Intersect With Cars

## Problem

Given intervals `[start, end]` representing cars, return the number of **distinct integer points covered by at least one car**.

If multiple cars cover the same point, that point is counted **only once**.

---

## 1. Brute Force

### Idea

For every car, visit every integer point between `start` and `end` and mark it as covered.

```python
covered = set()

for start, end in nums:
    for point in range(start, end + 1):
        covered.add(point)

return len(covered)
```

### How it works

For:

```text
nums = [[1, 3], [2, 5]]
```

We visit:

```text
Car 1 → 1, 2, 3
Car 2 → 2, 3, 4, 5
```

The set removes duplicates:

```text
{1, 2, 3, 4, 5}
```

Answer:

```text
5
```

### Complexity

If there are `n` cars and an interval can contain `k` points:

```text
Time:  O(n * k)
Space: O(k)
```

The problem's coordinates are small, so this can work, but we can solve the problem more efficiently using a line sweep.

---

# 2. Optimal — Line Sweep + Difference Array

## Key Insight

Instead of visiting **every point inside every interval**, focus on **where the coverage changes**.

For an interval:

```text
[start, end]
```

there are two events:

```text
start     → a car enters  → +1
end + 1   → a car leaves  → -1
```

For:

```text
[1, 3]
```

the events are:

```text
point:   1       4
         +1      -1
```

We use `end + 1` because `end` itself is still covered.

---

## Difference Array

Store the events in `diff`:

```python
diff[start] += 1
diff[end + 1] -= 1
```

For:

```text
nums = [[1, 3], [2, 5]]
```

the events become:

```text
point:     0   1   2   3   4   5   6
change:    0  +1  +1   0  -1   0  -1
```

---

## Sweep From Left to Right

Maintain the number of currently active cars:

```python
active = 0

for i in range(1, 101):
    active += diff[i]
```

This is a prefix sum of the difference array.

It gives:

```text
point:     0   1   2   3   4   5   6
active:    0   1   2   2   1   1   0
```

`active` means:

> How many cars currently cover this point?

---

## Count Distinct Covered Points

The problem asks for points covered by **at least one** car.

Therefore:

```python
if active > 0:
    answer += 1
```

We do **not** add `active`, because that would count overlapping cars multiple times.

For example:

```text
active = [0, 1, 2, 2, 1, 1, 0]
```

We count:

```text
0 → don't count
1 → count
2 → count
2 → count
1 → count
1 → count
0 → don't count
```

Answer:

```text
5
```

---

## Complete Solution

```python
class Solution:
    def numberOfPoints(self, nums):
        diff = [0] * 102

        # Create events
        for start, end in nums:
            diff[start] += 1
            diff[end + 1] -= 1

        active = 0
        answer = 0

        # Sweep from left to right
        for i in range(1, 101):
            active += diff[i]

            if active > 0:
                answer += 1

        return answer
```

---

# Why Is This Line Sweep?

The general line sweep pattern is:

```text
1. Create events
2. Process events from left → right
3. Maintain the current state
4. Calculate the answer
```

For this problem:

```text
Car starts       → +1 event
Car ends         → -1 event
                      ↓
                active cars
                      ↓
               active > 0?
                      ↓
                count point
```

The difference array is simply a convenient way to store the events because the coordinate range is only `1..100`.

---

# Important Recognition Pattern

When I see many intervals:

```text
[start, end]
[start, end]
[start, end]
...
```

I should ask:

> **"Can I process what changes at the boundaries instead of visiting everything inside each interval?"**

If yes, consider:

```text
Difference Array
Line Sweep
Prefix Sum
```

### Mental Model

```text
Brute Force:
interval → visit every point

Line Sweep:
interval → create boundary events
          ↓
       sweep →
          ↓
   maintain active state
          ↓
       calculate
```

**Brute force looks at the contents of the intervals.**

**Line sweep looks at the changes caused by the intervals.**
