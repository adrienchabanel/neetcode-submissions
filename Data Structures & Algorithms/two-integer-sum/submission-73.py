class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_of_nums = {}

        for i, n in enumerate(nums):
            indices_of_nums.setdefault(n, []).append(i)

        for n in indices_of_nums:
            solution = target - n

            i = indices_of_nums[n][-1]
            indices_of_nums[n].pop()

            if solution in indices_of_nums and indices_of_nums[solution]:
                return [
                    min(indices_of_nums[solution][-1], i),
                    max(indices_of_nums[solution][-1], i)
                ]