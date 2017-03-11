from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        key_mapper = lambda x: x[1]
        generator = lambda x: sorted((t for t in enumerate(x)), key=key_mapper)
        s_a = generator(A)
        s_b = generator(B)
        s_c = generator(C)
        s_d = generator(D)

        def sum_generator(xl, yl):
            sum_x_y = defaultdict(lambda: 0)
            for x in xl:
                for y in yl:
                    sum_x_y[x[1] + y[1]] += 1
            return sum_x_y

        sum_a_b = sum_generator(s_a, s_b)
        sum_c_d = sum_generator(s_c, s_d)

        counter = 0
        for v in sum_a_b.keys():
            if -v in sum_c_d:
                counter += sum_a_b[v] * sum_c_d[-v]

        return counter
