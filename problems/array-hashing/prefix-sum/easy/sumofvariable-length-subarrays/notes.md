29/08/2026

Pattern:
--> Prefix Sum

My first approach:
--> Nested loops

Time:
---> O(n²) --> Why is it so slow? For every i:
Calculate sum for start to i, the problem is that you've repeatedly adding elements

Space:
--> O(1)

Better approach:
---> Prefix Sum

Time:
---> O(n) --> Why is it so fast ? --> Once you calculate all prefix sums,
then every range sum becomes O(1) , so build prefix sum O(n), calculate n ranges O(n)
total O(n)

Space:
---> O(n)

Key idea:
--> For every index i, calculate the sum of the subarray that ends at i, starting from max(0, i - nums[i]).

How to recognize Prefix Sum problems:
--> Strong signals

"sum of elements from index L to R"

"sum between two indices"

"range sum"

"subarray sum"

"sum of every subarray"

"sum of elements before/after this index"

"multiple queries asking for sums

How to identify the same pattern in other questions?:
1.Am I dealing with a contiguous section of an array?
2.Do I need the SUM of that section?
3.Do I need to calculate many different ranges? like sum(0, 1), sum(3, 4),...
