class Solution:
    @staticmethod
    def twoSum(nums, target):
        my_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in my_dict.keys():
                return[my_dict[difference], i]
            my_dict[nums[i]] = i