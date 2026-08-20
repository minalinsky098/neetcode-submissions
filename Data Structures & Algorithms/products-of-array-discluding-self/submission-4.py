class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        prefix = []
        numlength = len(nums)
        for i in range(numlength):
            prefix.append(total)
            total *= nums[i]
        total = 1
        for i in range(numlength-1,-1,-1):
            prefix[i] *= total
            total *= nums[i]
        return prefix