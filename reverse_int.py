class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        while True:
            y = int(x/10)
            z = x % 10 if x > 0 else x % -10
            res = z + res*10
            if not y:
                break
            x = y
        return res if res in range(-2**31, 2**31) else 0


sol = Solution()
print(sol.reverse(1534236469))
