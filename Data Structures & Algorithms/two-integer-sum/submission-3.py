class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of_num = {num: index for index, num in enumerate(nums)}
        for index, num in enumerate(nums):
            complement = target - num
            complement_index = index_of_num.get(complement, None)
            if complement_index and index != complement_index:
                return [index, complement_index]