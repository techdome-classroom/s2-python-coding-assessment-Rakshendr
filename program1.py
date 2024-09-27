class Solution(object):
    def isValid(self, s):
        stack = [] # create an empty stack to store opening brackets
        for c in s: # loop through each character in the string
            if c in '([{': # if the character is an opening bracket
                stack.append(c) # push it onto the stack
            else: # if the character is a closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False 
                stack.pop() 
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


