class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_nums={}
        for number in nums:
            count_nums[number] = count_nums.get(number,0) + 1
            if count_nums[number] > 1:
                return True
        return False