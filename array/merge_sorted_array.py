# problem: merge two sorted arrays
# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """ 
        k = m+n-1
        m = m-1
        n = n-1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
                k -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
                k -= 1
        
        if n >= 0:
            nums1[:n+1] = nums2[:n+1]

#complexity O(m+n)

#call class
ob = Solution()
nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
ob.merge(nums1,m,nums2,n)
print(nums1)