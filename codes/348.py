# coding=utf-8
class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.length = n
        self.board = [[0] * n for _ in range(n)]
        self.row_indicator = [0] * n
        self.col_indicator = [0] * n
        self.winner = 0

    def check(self):  # this is an O(n) function
        for i in self.row_indicator:
            if i == self.length:
                return 1
            elif i == -self.length:
                return 2
        for i in self.col_indicator:
            if i == self.length:
                return 1
            elif i == -self.length:
                return 2

        total = 0
        for i in range(self.length):
            total += self.board[i][i]
        if total == self.length:
            return 1
        elif total == -self.length:
            return 2

        total = 0
        for i in range(self.length):
            total += self.board[i][self.length - 1 - i]
        if total == self.length:
            return 1
        elif total == -self.length:
            return 2

        return 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.winner:
            return self.winner

        if player == 1:
            self.board[row][col] = 1
            self.row_indicator[row] += 1
            self.col_indicator[col] += 1
        else:
            self.board[row][col] = -1
            self.row_indicator[row] -= 1
            self.col_indicator[col] -= 1

        check_result = self.check()
        if check_result:
            self.winner = check_result
        return self.winner

    def visualize(self):
        def mapper(x):
            if x == 1:
                return 'O'
            elif x == -1:
                return 'X'
            return '·'

        print '\n'.join(''.join(map(mapper, row)) for row in self.board)
        print


obj = TicTacToe(2)

for step in [[0, 1, 1], [1, 1, 2], [1, 0, 1]]:
    print apply(obj.move, step)
