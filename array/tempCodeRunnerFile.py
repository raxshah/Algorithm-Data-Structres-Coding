#find value at given percentile

import math
def find_percentile(candidates,per):
    candidates.sort()
    vl = (per/100) * (len(candidates) - 1)
    f = math.floor(vl)
    c = math.ceil(vl)
    if f == c:
        return candidates[f]
    left = candidates[f] * (c-vl) 
    right = candidates[c] * (vl-f) 

    return left+right

candidates = [1,2,3,4,5]
per = 40
print(find_percentile(candidates,per))