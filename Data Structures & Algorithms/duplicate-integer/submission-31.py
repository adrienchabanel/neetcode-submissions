class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ''' Chaba'''
        return True if len(set(nums)) != len(nums) else False