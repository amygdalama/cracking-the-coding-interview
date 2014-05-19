import random

class Board(object):
    def __init__(self, size=3):
        self.size = size
        self.board = [[''] * self.size] * self.size
        self.empty = ''

    def __repr__(self):
        format = ' '
        for i in xrange(self.size):
            format += " | ".join(self.board[i])
            if i < self.size - 1:
                format += " \n-----------\n "
        return format

    def get_columns(self):
        return [[self.board[i][j] for i in xrange(self.size)]
                for j in xrange(self.size)]

    def get_diagonals(self):
        return [[self.board[i][i] for i in xrange(self.size)],
                [self.board[i][self.size-i-1] for i in xrange(self.size)]]

    def random_board(self):
        self.board = [[random.choice(['x','o'])
                for i in xrange(self.size)]
                for i in xrange(self.size)]

    def spaces_winner(self, spaces):
        for i, current in enumerate(spaces):
            if current == self.empty or current != spaces[i-1]:
                return None
        return current

    def winner(self):
        for row in self.board:
            winner = self.spaces_winner(row)
            if winner:
                return winner
        for column in self.get_columns():
            winner = self.spaces_winner(column)
            if winner:
                return winner
        for diagonal in self.get_diagonals():
            winner = self.spaces_winner(diagonal)
            if winner:
                return winner
        return None


if __name__ == '__main__':
    board = Board()
    board.random_board()
    print board
    print "And the winner is... %s!" % board.winner()
