#find value at given percentile

import math
def find_percentile(arr,per):
    arr.sort()
    vl = (per/100) * (len(arr) - 1)
    f = math.floor(vl)
    c = math.ceil(vl)
    if f == c:
        return arr[f]
    left = arr[f] * (c-vl) 
    right = arr[c] * (vl-f) 

    return left+right

arr = [1,2,3,4,5]
per = 40
print(find_percentile(arr,per))