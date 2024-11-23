from tree import Problem
from tree import depth_first_recursive_search as dfs

# Вам дана матрица символов размером M × N. Ваша задача — найти и вывести
# список всех возможных слов, которые могут быть сформированы
# из последовательности соседних символов в этой матрице.
# При этом слово может формироваться во всех восьми возможных направлениях
# (север, юг, восток, запад,
# северо-восток, северо-запад, юго-восток, юго-запад),
# и каждая клетка может быть использована в слове только один раз.


class WordsProblem(Problem):
    def __init__(self, initial, goal, board, word):
        super().__init__(initial, goal)
        self.board = board
        self.word = word
        self.visited = set()

    def actions(self, state):
        r, c = state[0]
        letters = state[1]
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]
        for dr, dc in directions:
            if (
                0 <= r + dr < len(self.board)
                and 0 <= c + dc < len(self.board[0])
                and (self.board[r + dr][c + dc] == self.word[len(letters)])
                and (r + dr, c + dc) not in self.visited
            ):
                self.visited.add((r + dr, c + dc))
                yield (r + dr, c + dc)

    def result(self, state, action):
        r, c = action
        n_state = (action, state[1] + self.board[r][c])
        return n_state

    def is_goal(self, state):
        return state[1] == self.word


def solve(board, dictionary):
    words = set()
    problem = WordsProblem(None, None, board, None)
    for word in dictionary:
        problem.visited = set()
        initial_letter = word[0]
        goal = word
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == initial_letter:
                    initial = ((i, j), initial_letter)
                    problem.initial = initial
                    problem.goal = goal
                    problem.word = word
                    word = dfs(problem)
                    if word:
                        words.add(word.state[1])
    return words


if __name__ == "__main__":
    board = [["М", "С", "Е"], ["Р", "А", "Т"], ["Л", "О", "Н"]]
    dictionary = ["МАРС", "СОН", "ЛЕТО", "ТОН"]
    words = solve(board, dictionary)
    print(words)

    print("\n")
    board = [
        ["Д", "О", "М", "У", "К"],
        ["Е", "Л", "Я", "Р", "А"],
        ["Ш", "К", "А", "Ф", "Т"],
        ["С", "Т", "О", "Л", "Ы"],
    ]
    dictionary = ["ДОЛЯ", "ШТОК", "РУКА", "ФЛОТ", "ДЫМ", "СТУЛ"]
    words = solve(board, dictionary)
    print(words)