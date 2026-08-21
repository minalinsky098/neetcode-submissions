class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq = dict()
        left = 0
        right = 0
        if not nums:
            return 0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                seq[i] = 1
                j = i + 1 
                while j in nums:
                    seq[i] += 1
                    j += 1
        print(max(seq.values()))
        return max(seq.values())
