def k_subsequ(k,nums):
    ans = 0
    d = {0: 1}
    acc = 0        
    for i in range(len(nums)):
        acc += nums[i]       
        key = acc % k
        
        if key in d:
            ans += d[key]
            d[key] += 1
        else:
            d[key] = 1
        
    return ans

arr = [5,10,11,9,5]
print(k_subsequ(5,arr))