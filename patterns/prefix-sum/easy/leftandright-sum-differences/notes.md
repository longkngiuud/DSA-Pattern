29/08/2026
Question asks:
"What is the sum of everything before/after each index?"

Think:
→ left running sum
← right running sum

Usually O(n)

Key idea:

For every index i, you want:

| sum of elements LEFT of i - sum of elements RIGHT of i |

             i
             ↓

[10, 4, 8, 3]

i = 0: left = 0 right = 4+8+3 = 15
i = 1: left = 10 right = 8+3 = 11
i = 2: left = 10+4=14 right = 3
i = 3: left = 22 right = 0

|0 - 15| = 15
|10 - 11| = 1
|14 - 3 | = 11
|22 - 0 | = 22
