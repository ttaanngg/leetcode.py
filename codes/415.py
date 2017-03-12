import itertools


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num2:
            num2 = "0"
        if not num1:
            num1 = "0"

        if len(num1) > 5 and len(num2) > 5:
            a, b, c, d = num1[:-5], num2[:-5], num1[-5:], num2[-5:]
            return self.addStrings(
                self.addStrings(
                    self.multiply(a, b) + '0' * 10,
                    self.multiply(c, d)
                ),
                self.addStrings(
                    self.multiply(num1[:-5], num2[-5:]),
                    self.multiply(num2[:-5], num1[-5:]),
                ) + '0' * 5,
            )
        return str(int(num1) * int(num2))

    def addStrings(self, num1, num2):
        z = itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0')
        res, carry, zero2 = [], 0, 2 * ord('0')
        for i in z:
            cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
            res.append(str(cur_sum % 10))
            carry = cur_sum // 10
        return ('1' if carry else '') + ''.join(res[::-1])


solution = Solution()
print solution.multiply("9190480321878126938104987136278563827164781624786138276481784961783264781634" * 4,
                        10 * "3232132421321345321431242314124123213123121313211")
