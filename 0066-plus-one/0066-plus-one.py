class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = ""
        result=[]
        for num in digits:
            number+=str(num)
        
        
        increment = int(number)+1
        for dig in str(increment):
            result.append(int(dig))

        return result


        