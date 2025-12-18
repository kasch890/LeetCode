class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars_stack = []
        for letter in s:
            #if it is an opening bracket, append it to the stack
            if letter=="(" or letter=="["or letter=="{":
                chars_stack.append(letter)
                continue
            #if it is a closing bracket, check that the top of the stack is the 
            #matching opening bracket and pop it, continuing to the next letter
            else:
                if not chars_stack:
                    return False
                current_open = chars_stack.pop()
                if current_open=="(" and letter==")":
                    continue
                elif current_open=="[" and letter=="]":
                    continue
                elif current_open=="{" and letter=="}":
                    continue
                else:
                    return False
        #if character left in stack - unclosed pair
        if chars_stack:
            return False
        return True           

        
