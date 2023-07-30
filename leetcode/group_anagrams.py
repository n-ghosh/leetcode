from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1: O(n^2)
        # for each str, dbl loop look for its pair in the list

        # 2: O(n)
        # for each str, add frozenset(str) to a dict of str:index pairs. 
        # Unless it's already in the dict, then remove it and pair them
        # issue: input str contains duplicates "eyes", "yes"
        groups_anagrams = []
        map_strs = dict() 
        for s in strs:
            s_unordered = frozenset(s)
            if len(s_unordered) == len(s):
                if s_unordered not in map_strs:
                    map_strs[s_unordered] = len(groups_anagrams)
                    groups_anagrams.append([s])
                else:
                    groups_anagrams[map_strs[s_unordered]].append(s)
            else:
                s_sorted = ''.join(sorted(s))
                if s_sorted not in map_strs:
                    map_strs[s_sorted] = len(groups_anagrams)
                    groups_anagrams.append([s])
                else:
                    groups_anagrams[map_strs[s_sorted]].append(s)
        return groups_anagrams
    
test_cases = [["eat","tea","tan","ate","nat","bat"],
              ["eyes", "yes", "yees", "sey", "bat"],
[""],
["a"]]
case_sols = [ [["bat"],["nat","tan"],["ate","eat","tea"]],
             [["eyes", "yees"], ["yes", "sey"], ["bat"]],
             [[""]],
             [["a"]],
]
solution = Solution()

for i, case in enumerate(test_cases):
    sol = solution.groupAnagrams(case)
    if not (sol == case_sols[i]):
        print(case, '-?>', sol)