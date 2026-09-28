# Sweep Line + Difference Array

- Difference array -> Prefix Sum -> active(points_on_line)

## Recognition Clue

Think **Sweep Line** when:

- Input contains **intervals/ranges** `[start, end]`
- Something changes when an interval **starts or ends**
- Need to know **coverage / active intervals / overlap** at each position or time

### Key question

> **"Does the state only change at interval boundaries?"**

If yes → think **Sweep Line**.

---

## Core Pattern

For an inclusive interval:

```text
[start, end]
```

record:

```text
+1 at start
-1 at end + 1
```

Then sweep left → right with a prefix sum:

```python
active += diff[i]
```

`active` = number of currently active intervals.

Example:

```text
[1,3]

+1 at 1
-1 at 4

active:
1  1  1  0
```

So:

```text
active > 0 → point is covered
```

---

## Mental Model

```text
Intervals
   ↓
Boundary changes
   ↓
+1 / -1 events
   ↓
Sweep left → right
   ↓
Prefix sum
   ↓
Current active intervals
```

### Small coordinates

```text
Difference Array + Prefix Sum
```

### Large coordinates

```text
Events + Sorting + Sweep Line
```

---

## Review Rule

If I **recognize the pattern but forget the implementation**:

1. Try to reconstruct it.
2. Check my `review_notes.md`.
3. Close the notes.
4. Implement it myself.

**Don't immediately look at the LeetCode solution.**

> Goal: remember **how to recognize and reconstruct the pattern**, not memorize individual solutions.
