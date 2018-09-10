class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length):
            target_in_arr = target - nums[i]
            try:
                j = nums[i+1:].index(target_in_arr)
            except ValueError as e:
                print(e)
            else:
                return (i, j+i+1)

if __name__ == "__main__":
    nums = [5, 7, 3, 3, 4]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
