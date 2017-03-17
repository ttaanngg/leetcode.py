class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        length = len(words)
        for i in range(length):
            words[i] = words[i].ljust(length, ' ')
        for i in range(length):
            for j in range(length):
                if words[i][j] != words[j][i]:
                    return False
        return True


solution = Solution()
print solution.validWordSquare(["abcd", "bnrt", "crm", "dt"])
