class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

test_cases = {"A man, a plan, a canal: Panama":True,
"race a car":False,
" ":True}

solution = Solution()

for case in test_cases:
    assert(solution.isPalindrome(case) == test_cases[case])