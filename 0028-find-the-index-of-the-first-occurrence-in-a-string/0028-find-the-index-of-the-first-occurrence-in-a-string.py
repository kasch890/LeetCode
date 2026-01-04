class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        h = len(haystack)
        n = len(needle)

        if n>h:
            return -1
        for i in range(1+h-n):
            sub = haystack[i:i+n]
            if sub==needle:
                return i
        return -1