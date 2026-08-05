class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            print(difference)
            if difference in map.keys():
                print(map.keys())
                return[map.get((difference)), i]
            else:
                map[nums[i]] = i
        print(map)
        return []