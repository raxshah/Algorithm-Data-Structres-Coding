# problem: maximum subarray
# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = float('-inf')
        max_sum = float('-inf')
        for num in nums:
            max_so_far = max(num,max_so_far+num)
            max_sum = max(max_sum, max_so_far)
        return max_sum

    #using divide and conquer 
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def mid_cross(arrs,left,m,right):
            
            max_left_sum = float('-inf')
            sum_so_far = 0
            for num in range(m,left-1,-1):
                sum_so_far += arrs[num]
                max_left_sum = max(max_left_sum,sum_so_far)
            
            max_right_sum = float('-inf')
            sum_so_far = 0
            for num in range(m+1,right+1,1):
                sum_so_far += arrs[num]
                max_right_sum = max(max_right_sum,sum_so_far)

            return max_left_sum + max_right_sum

        def helper(arrs,left,right):
            #base case
            if left == right:
                return arrs[left]
            
            #dividing point
            m = left + (right-left)//2

            left_sum = helper(arrs,left,m)
            right_sum = helper(arrs,m+1,right)
            mid_sum = mid_cross(arrs,left,m,right)
            
            return max(left_sum,right_sum,mid_sum)
        
        return helper(nums,0,len(nums)-1)
        
obj = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
result = obj.maxSubArray2(arr)
print(result)


# complexity O(n)
# complexity O(nlogn) by divide and conquer