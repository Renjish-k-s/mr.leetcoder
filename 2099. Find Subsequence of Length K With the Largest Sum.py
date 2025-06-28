class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tar=len(nums)-k
        for i in range(tar):
            nums.remove(min(nums))
        return nums
        