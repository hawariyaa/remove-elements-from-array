# this questions asks us to remove elements from the array that is given us a val
# and we are going to return the number of numbers that are left inside the array
# for example: nums = [0, 1, 1, 2, 2, 3, 4, 5]  val = 1
# return is k = 6
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l