Pattern: Two pointers

My first Approach: Create a more memory and loop through that

Time Complexity : O(n2) Why? 'cause you create an array --> that causes more time and space

Space Complexity: O(n)

Optimized Approach: Two pointers or Math
Time Complexity : O(n) and O(1)
Space Complexity: O(1) and O(1)

Key idea: \*Two pointers
+Two pointers start at opposite ends. Maintain a running sum for each side. Expand the side with the smaller sum until the two sides meet around the desired middle element.

+We traverse the range until the pointers meet, dynamically adjusting sums based on comparisons. If sumLeft is greater than or equal to sumRight, the sum on the left is ahead, and we must catch up on the right. Hence, we decrement rightValue and add the new element to sumRight. Otherwise, the sum on the right is ahead, so we increment leftValue and add the new element to sumLeft.

- Calculate the total sum of the sequence from 1 to n using the formula (n⋅(n+1)/2),

*Calculate the square root of the total sum and store it in pivot.
*Check if the square of the pivot is equal to the total sum.
*If the square of the pivot is equal to the total sum, return the pivot as the pivot integer x.
*If the square of the pivot is not equal to the total sum, return -1
