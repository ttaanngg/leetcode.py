class SnakeGame(object):
    def __init__(self, width, height, food):
        # init code
        self.width = width
        self.height = height
        self.food = [tuple(item) for item in food]
        self.body = [(0, 0)]
        self.filled = {(0, 0), }
        self.finished = False

    def eat_food(self):
        self.food = self.food[1:]

    def has_food(self, pos):
        return self.food and self.food[0] == pos

    def safe_pos(self, pos):
        return 0 <= pos[0] < self.height and 0 <= pos[1] < self.width

    def trans(self, pre, direction):
        if direction == 'U':
            return pre[0] - 1, pre[1],
        elif direction == 'D':
            return pre[0] + 1, pre[1],
        elif direction == 'L':
            return pre[0], pre[1] - 1,
        elif direction == 'R':
            return pre[0], pre[1] + 1,
        assert 1 == 2

    def move(self, direction):
        if self.finished:
            return -1

        head = self.trans(self.body[0], direction)

        # check the new position is valid
        if (head in self.filled and head != self.body[-1]) or not self.safe_pos(head):
            self.finished = True
            return -1

        self.body.insert(0, head)

        if not self.has_food(head):
            self.body = self.body[:-1]
        else:
            self.eat_food()
        self.filled = {p for p in self.body}
        return self.score

    @property
    def score(self):
        return len(self.body) - 1


game = SnakeGame(3, 3, [[2, 0], [0, 0], [0, 2], [0, 1], [2, 2], [0, 1]])
#
for m in [["D"], ["D"], ["R"], ["U"], ["U"], ["L"], ["D"], ["R"], ["R"], ["U"], ["L"], ["L"], ["D"], ["R"], ["U"]]:
    print(game.move(m[0]))


# for _ in range(5):
#     print game.move('R')
#     game.output_status()
