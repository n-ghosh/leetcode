class Solution:
    def longestPalindrome(self, s: str) -> str:
        table = []
        for i in range(len(s) + 2):
            table.append([])
            for j in range(len(s) + 2):
                table[i].append(0)

        longest = 0
        idx_max = -1
        for i, c1 in enumerate(s):
            for j in range(len(s)): 
                if c1 == s[j]:
                    if table[i][j] == table[i][j+2]:
                        table[i+1][j+1] = 1 + 2 * table[i][j]

                        if table[i+1][j+1] > longest:
                            longest = table[i+1][j+1]
                            idx_max = i
                        # print(f"true for {i}:{j}:{c1}")
                    else: 
                        table[i+1][j+1] = 1
                # print(f"length {longest}, idx_max {idx_max}")
        return s[idx_max - longest//2:idx_max+longest//2+1]
