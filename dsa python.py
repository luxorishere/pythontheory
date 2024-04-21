class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                return [nums_dict[complement], i]
            else:
                nums_dict[nums[i]] = i

