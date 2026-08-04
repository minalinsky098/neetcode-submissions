class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        highest = 0
        for i in nums:
            if i==1:
                count+=1
            else:
                highest = max(highest, count)
                count = 0
            print(f"Count: {count}, Highest: {highest}")
        highest = max(highest, count)
        return highest


        