class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        """
        first = int(a,2)
        second= int(b,2)

        sum = first + second

        return bin(sum)[2:]
