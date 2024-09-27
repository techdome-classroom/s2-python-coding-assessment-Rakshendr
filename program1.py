class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {')': '(', '}': '{', ']': '['}
    
        stack = []
        
        for char in s:
            if char in bracket_map.values(): 
                stack.append(char)
            elif char in bracket_map: 
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop() 
                else:
                    return False 
        return not stack  


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_mixed_parentheses(self):
        self.assertFalse(self.solution.isValid("(){"))

if __name__ == '_main_':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


class Solution(object):
    def isValid(self, s):
        stack = [] # create an empty stack to store opening brackets
        for c in s: 
            if c in '([{': 
                stack.append(c) 
            else: 
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False # the string is not valid, so return false
                stack.pop() # otherwise, pop the opening bracket from the stack
        return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                         # so the string is valid, otherwise, there are unmatched opening brackets, so return false