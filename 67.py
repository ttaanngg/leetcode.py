class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        partial_result_b = []
        rest = 0
        for pair in zip(reversed(a), reversed(b)):
            add = rest + int(pair[0]) + int(pair[1])
            if add == 3:
                partial_result_b.append('1')
                rest = 1
            elif add == 2:
                partial_result_b.append('0')
                rest = 1
            elif add == 1:
                partial_result_b.append('1')
                rest = 0
            else:
                partial_result_b.append('0')
        partial_result_b.reverse()

        min_length = min(len(a), len(b))
        partial_result_a = [c for c in a[:len(a) - min_length] + b[:len(b) - min_length]]

        for i in range(len(partial_result_a) - 1, -1, -1):
            add = rest + int(partial_result_a[i])
            if add == 2:
                partial_result_a[i] = '0'
                rest = 1
            elif add == 1:
                partial_result_a[i] = '1'
                rest = 0
                break
            else:
                break

        if rest == 1:
            partial_result_a = ['1'] + partial_result_a

        return ''.join(partial_result_a + partial_result_b),


solution = Solution()

for i in range(0, 10):
    for j in range(0, 10):
        expect = bin(i + j)[2:]
        get = ''.join(solution.addBinary(bin(i)[2:], bin(j)[2:]))
        if not expect == get:
            print i, j, expect, get
