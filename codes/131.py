def is_palindorme(s):
    if len(s) < 2:
        return True
    for i in range(len(s) / 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


class Solution(object):
    def partition(self, s):
        result = []
        if not s:
            return result
        if len(s) < 2:
            result.append([s])
            return result
        for i in range(0, len(s)):
            h, t = s[:i + 1], s[i + 1:]
            if is_palindorme(h):
                if not t:
                    result.append([h])
                else:
                    partial_result = self.partition(t)
                    if partial_result:
                        # print 'partial', partial_result
                        result.extend([[h] + partial for partial in partial_result])
        return result


solution = Solution()
print solution.partition("aab")
print solution.partition("bb")
print solution.partition("")
print solution.partition("a")
