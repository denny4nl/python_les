class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    yield i, j


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 22
    sol = Solution()
    print(list(sol.twoSum(nums, target)))
    for i in sol.twoSum(nums, target):
        print(i)
