class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if not nums:
            return 0
        
        right = len(nums)-1
        left = 0
        while right >= left:
            if nums[left] == val:
                nums[left]=nums[right]
                right-=1
            else:
                left+=1


        return left
            

