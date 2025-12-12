class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort(key=len)
        min_len = len(strs[0])
        prefix=""
        i=0
        while i<min_len:
            curr_letter= strs[0][i]
            for item in strs:
                if item[i]==curr_letter:
                    continue
                else:
                    return prefix
            prefix+=curr_letter
            i+=1
        return prefix

