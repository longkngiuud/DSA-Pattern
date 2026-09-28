# Prefix/Suffix Contribution Pattern

## Recognition Clue

Think **Prefix/Suffix Contribution** when:

- You need an answer for **every index**
- Other elements contribute to that index
- The contribution depends on **distance/position**
- You can calculate contributions from the **left and right separately**

### Key question

> **"For each index, can I calculate the contribution from the left and the right independently?"**

If yes → think **two directional passes**.

---

## Core Pattern

```text
Every index
    ↓
Left contribution  → Left → Right
Right contribution → Right → Left
    ↓
Combine
    ↓
Answer
```

---

## Example: Minimum Operations to Move Balls

For:

```python
boxes = "001011"
```

Each `'1'` is a ball.

For every box, calculate the total distance from all balls.

Instead of checking every ball for every box (`O(n²)`):

```text
Left → Right
    ↓
calculate left contribution

Right → Left
    ↓
calculate right contribution
```

### Forward pass

```python
count = 0
moves = 0

for i in range(n):
    ans[i] += moves

    if boxes[i] == '1':
        count += 1

    moves += count
```

- `count` = number of balls seen so far
- `moves` = contribution from those balls

### Backward pass

Do the same from right → left to calculate the right contribution.

---

## Important Connection

This is related to **Prefix + Suffix**:

```text
Prefix/Suffix Max/Min
→ store information about each side

Prefix/Suffix Contribution
→ calculate accumulated cost from each side
```

Both use the same fundamental idea:

> **Break the problem into LEFT and RIGHT contributions.**

---

## Complexity

Brute force:

```text
O(n²)
```

Two directional passes:

```text
Time:  O(n)
Space: O(n)
```

---

## Mental Trigger

> **"Every index needs a result based on contributions from elements on both sides."**

Think:

```text
LEFT  → forward pass
RIGHT → backward pass
```

Then ask:

> **"Can I maintain the contribution incrementally instead of recalculating it?"**

If yes → likely an **O(n) prefix/suffix contribution** solution.

---

## Review Rule

Don't memorize the exact code.

Remember:

```text
Answer for every index
        ↓
Separate left/right contribution
        ↓
Forward + backward pass
        ↓
Maintain contribution incrementally
        ↓
O(n)
```
