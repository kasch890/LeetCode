class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        idx = -1
        while True:
            if words[idx]=="":
                idx -= 1
                continue
            return len(words[idx])

        