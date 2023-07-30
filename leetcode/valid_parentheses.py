class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack to track left brackets
        # loop through chars:
            # if new_char is left bracket
                # s.push(new_char)
            # else if s.peek() is new_char's left bracket
                # s.pop()
            # else return false

        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
                continue
            elif not stack or \
                stack[-1] == '(' and char != ')' or\
                stack[-1] == '{' and char != '}' or\
                stack[-1] =='[' and char != ']':
                return False
            stack.pop()
        return not stack

test_cases = {"()":True,
"()[]{}":True,
"(]":False}

solution = Solution()

for case in test_cases:
    assert(solution.isValid(case) == test_cases[case])