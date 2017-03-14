class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def calc(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            return a / b

        op_stack = []
        v_stack = []
        v_buf = []
        for c in s:
            if c.isdigit():
                v_buf.append(c)
            elif c.isspace():
                continue
            else:
                v_stack.append(int(''.join(v_buf)))
                v_buf = []
                while op_stack and op_stack[-1] in ('*', '/'):
                    op = op_stack.pop()
                    b = v_stack.pop()
                    a = v_stack.pop()
                    v_stack.append(calc(a, b, op))
                op_stack.append(c)
        if v_buf:
            v_stack.append(int(''.join(v_buf)))
        if op_stack and op_stack[-1] in ('*', '/'):
            b = v_stack.pop()
            a = v_stack.pop()
            op = op_stack.pop()
            v_stack.append(calc(a, b, op))

        for i in range(len(op_stack)):
            v_stack[0] = calc(v_stack[0], v_stack[i + 1], op_stack[i])

        if v_stack:
            return v_stack[0]
        return 0


solution = Solution()
print solution.calculate("3+2*2")
print solution.calculate("1-1+1")
print solution.calculate("1+1-1")
print solution.calculate("1")
