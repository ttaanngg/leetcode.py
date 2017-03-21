class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        is_negative = num < 0
        num = abs(num)
        result = []

        while num > 0:
            num, r = divmod(num, 7)
            result.append(str(r))

        return (('-' if is_negative else '') + ''.join(reversed(result))) or '0'


solution = Solution()
print solution.convertToBase7(-7)
print solution.convertToBase7(0)
print solution.convertToBase7(100)
