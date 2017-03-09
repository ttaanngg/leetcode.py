class Solution(object):
    def updateBoard(self, board, click):
        board = [list(row) for row in board]
        click = (click[0], click[1],)
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        def valid_p(p):
            return 0 <= p[0] < len(board) and 0 <= p[1] < len(board[0])

        def not_mine(p):
            if not valid_p(p):
                return -1
            return 0 if board[p[0]][p[1]] == 'M' else 1

        def count(p):
            is_mine = lambda x: 1 if not not_mine(x) else 0
            return sum([
                is_mine((p[0] - 1, p[1],)),
                is_mine((p[0] - 1, p[1] + 1,)),
                is_mine((p[0] - 1, p[1] - 1,)),
                is_mine((p[0], p[1] - 1,)),
                is_mine((p[0], p[1] + 1,)),
                is_mine((p[0] + 1, p[1] - 1,)),
                is_mine((p[0] + 1, p[1],)),
                is_mine((p[0] + 1, p[1] + 1,)),
            ])

        visited = set()

        def travel(p):
            if not valid_p(p):
                return
            if p in visited:
                return
            v = count(p)
            visited.add(p)
            if v:
                board[p[0]][p[1]] = '{}'.format(v)
            else:
                board[p[0]][p[1]] = 'B'
                travel((p[0] - 1, p[1],))
                travel((p[0] - 1, p[1] + 1,))
                travel((p[0] - 1, p[1] - 1,))
                travel((p[0], p[1] - 1,))
                travel((p[0], p[1] + 1,))
                travel((p[0] + 1, p[1] - 1,))
                travel((p[0] + 1, p[1],))
                travel((p[0] + 1, p[1] + 1,))

        # if board[click[0]][click[1]] == 'E':
        travel(click)
        return board


solution = Solution()
board = solution.updateBoard(
    ["EEEEE", "EEMEE", "EEEEE", "EEEEE"],
    [3, 0],
)

for row in board:
    print row
