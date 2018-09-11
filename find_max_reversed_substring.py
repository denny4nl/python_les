class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_left_right_index(num):
            if num == 0:
                return [(0, 0)]
            return [(i, num-i) for i in range(0, num+1)]

        left_index = 0
        right_index = 0
        length = len(s)
        num = 0
        while True:
            for left_index, right_index in get_left_right_index(num):
                ordered_s = s[left_index:length - right_index]
                reserved_s = ordered_s[::-1]
                if ordered_s == reserved_s:
                    return ordered_s
            else:
                if num == length - 1:
                    return s[0]
            num += 1

s = 'cbbd'
sol = Solution()
print(sol.longestPalindrome(s))
