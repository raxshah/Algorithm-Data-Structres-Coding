class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False
        
        
        left = list()
        right = list()
        left_min = float('inf')
        right_min = float('inf')
        
        for num in nums:
            left.append(left_min)            
            left_min = min(left_min, num)
        
        for num in reversed(nums):
            right.append(right_min)            
            right_min = min(right_min, num)
        
        right.reverse()
        print(left)
        print(right)
        for i in range(len(nums)):
            if left[i] < right[i] and right[i] < nums[i]:
                return True
        return False
        
arr = [3,5,0,3,4]
print(Solution().find132pattern(arr))