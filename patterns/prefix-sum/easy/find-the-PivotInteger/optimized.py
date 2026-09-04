# Math approach
import math
def pivotInteger(n):
    sum_int = n*(n + 1) // 2
    pivot = int(math.sqrt(sum_int))

    if pivot * pivot == sum_int:
        return pivot

    else:
        return -1



print(pivotInteger(1))
