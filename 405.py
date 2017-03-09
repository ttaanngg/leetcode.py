from string import translate


class Solution(object):
    def translate(self, num):
        assert 0 <= num <= 16
        if num < 10:
            return '%d' % num
        return chr(num - 10 + ord('a'))

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num += 0xffffffff + 1

        result = []
        while num >= 16:
            n = num % 16
            result.append(self.translate(n))
            num //= 16
        result.append(self.translate(num))

        return ''.join(reversed(result))


solution = Solution()
for i in range(-100, 100):
    r = solution.toHex(i)
    print i, hex(i)[2:], r, int(r, base=16)
