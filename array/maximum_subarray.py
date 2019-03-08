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

#complexity O(n)