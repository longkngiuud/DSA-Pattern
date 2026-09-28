## Minimum Number of Operations to Move All Balls to Each Box

### Pattern: Prefix Sum / Running Count

### Core Idea

For each target position `i`, we need the total distance of all balls to `i`.

Brute force would calculate:

    sum(abs(i - j))

for every `i`, giving **O(n²)**.

Instead, calculate the contribution from each side separately using two passes.

### Left → Right

When moving the target one position to the right:

- Every ball on the left becomes **1 step farther away**.
- Therefore, if `count` = number of balls seen so far:

  moves += count

`moves` = accumulated operations contributed by balls on the left.

### Right → Left

Do the exact same thing from the other direction:

- Every ball on the right becomes **1 step farther away** when moving left.
- Again:

  moves += count

### Algorithm

1. Initialize `answer = [0] * n`.
2. Scan from left → right:
   - Add current `moves` to `answer[i]`.
   - If `boxes[i] == '1'`, increment `count`.
   - Add `count` to `moves`.
3. Reset `count` and `moves`.
4. Scan from right → left using the same logic.
5. Add the right-side contribution into `answer`.

### Key Insight

Instead of recalculating the distance to every ball:

    abs(i - j)

we notice that moving the target by **one position** changes the total cost by exactly the **number of balls on that side**.

    number of balls → change in cost

Therefore, maintain:

    count = number of balls encountered
    moves = accumulated movement cost

### Complexity

Time: **O(n)**

Space: **O(n)**

### Recognition Pattern

If a problem asks for the cost/distance at **every position**, and moving from one position to the next changes the cost based on the number of elements already seen, consider:

- Prefix sum
- Running count
- Left → Right + Right → Left
