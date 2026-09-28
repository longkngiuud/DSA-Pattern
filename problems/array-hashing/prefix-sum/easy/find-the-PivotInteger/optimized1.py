# Two pointer approach
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

print(pivotInteger(8))
