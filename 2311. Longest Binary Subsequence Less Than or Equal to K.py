class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        while s:
            if int(s,2)<=k:
                break
            else:
                index=s.find('1')
                if index!=-1:
                    s=s[:index]+s[index+1:]
        return len(s)