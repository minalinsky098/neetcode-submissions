class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum = target - 1
        left = 0
        right = len(numbers) - 1
        while sum != target:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
        return [left+1, right+1]