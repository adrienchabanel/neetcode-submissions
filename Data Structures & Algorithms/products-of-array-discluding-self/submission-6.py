class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        zero_cnt = 0
        prod = 1
        for numbers in nums:
            if numbers != 0:
                prod *= numbers
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return res
        elif zero_cnt == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = prod
        else:
            for i in range(len(nums)):
                res[i] = prod//nums[i]
        return res
        
                
