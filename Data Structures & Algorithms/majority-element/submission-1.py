from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore algorithm
        """
        candidate = nums[0]
        count = 0

        for index in range(len(nums)):
            if count == 0:
                candidate = nums[index]

            count += 1 if nums[index] == candidate else -1

        return candidate