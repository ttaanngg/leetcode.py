class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def rec(s, expect=4):
            if len(s) < expect or 3 * expect < len(s) or expect < 1:
                return []

            if expect == 1:
                if s[0] == '0' and len(s) != 1:
                    return []
                elif not (0 <= int(s) <= 255):
                    return []
                else:
                    return [s]

            result = []
            for i in range(3):
                h = int(s[:i + 1])
                if 0 <= h <= 255:
                    result.extend([str(h) + '.' + seg for seg in rec(s[i + 1:], expect - 1)])
                    if h == 0:
                        break
            return result

        return rec(s)


solution = Solution()
print solution.restoreIpAddresses("172162541")
