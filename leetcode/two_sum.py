from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()

        # for every number, check if its pair is already found
        for i, n in enumerate(nums):
            pair = target - n
            if pair in indices:
                return i, indices[pair]
            # if not, add this number to the found list & continue
            indices[n] = i