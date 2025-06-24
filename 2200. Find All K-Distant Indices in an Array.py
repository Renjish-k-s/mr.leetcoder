class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        pos=[]
        out=[]
        p=0
        l=len(nums)
        for i in range(len(nums)):
            if nums[i]==key:
                pos.append(i)
        print(pos)
        for i in range(l):
            if p>=len(pos):
                break
            if abs(i-pos[p]) <= k:
                out.append(i)               
            if (pos[p]+k)==i:
                p+=1
            
        return out

        