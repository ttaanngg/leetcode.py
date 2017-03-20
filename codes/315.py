class Solution(object):
    def countSmaller(self, nums):
        counter = [0] * len(nums)

        def merge_sort(seq):
            length = len(seq)
            if length <= 1:
                return seq

            left, right = merge_sort(seq[:length / 2]), merge_sort(seq[length / 2:])

            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                l = left[i]
                r = right[j]
                if r[1] < l[1]:
                    counter[l[0]] += (j + 1)
                    result.append(right[j])
                    j += 1
                else:
                    result.append(left[i])
                    i += 1
            result = result + left[i:] + right[j:]

            return result

        zipper = list(enumerate(nums))
        merge_sort(zipper)
        return counter


solution = Solution()
print(solution.countSmaller([5, 2, 6, 1]))
