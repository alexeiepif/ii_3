#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tree import Problem
from tree import depth_first_recursive_search as dfs

# Дана матрица символов размером M×N. Необходимо найти длину самого длинного
# пути в матрице, начиная с заданного символа. Каждый следующий символ в пути
# должен алфавитно следовать за предыдущим без пропусков.
# Разработать функцию поиска самого длинного пути в матрице символов,
# начиная с заданного символа. Символы в пути должны следовать в алфавитном
# порядке и быть последовательными. Поиск возможен во всех восьми направлениях.


class LenProblem(Problem):
    def __init__(self, initial, goal, matrix, start):
        super().__init__(initial, goal)
        self.matrix = matrix
        self.max_len = 0
        self.start = start

    def actions(self, state):
        sw = False
        r, c = state
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
                0 <= r + dr < len(self.matrix)
                and 0 <= c + dc < len(self.matrix[0])
                and (
                    ord(self.matrix[r + dr][c + dc]) - ord(self.matrix[r][c])
                    == 1
                )
            ):
                yield (r + dr, c + dc)
                sw = True

        if not sw:
            k = ord(self.matrix[r][c]) - ord(self.start)
            if k > self.max_len:
                self.max_len = k

    def result(self, state, action):
        return action


def solve(start, matrix):
    problem = LenProblem(None, None, matrix, start)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == start:
                problem.initial = (i, j)
                dfs(problem)
    return problem.max_len + 1


if __name__ == "__main__":
    matrix = [
        ["D", "E", "H", "X", "B"],
        ["A", "O", "G", "P", "E"],
        ["D", "D", "C", "F", "D"],
        ["E", "B", "E", "A", "S"],
        ["C", "D", "Y", "E", "N"],
    ]

    start = "C"
    res = solve(start, matrix)
    print(res, "start = 'C'")

    matrix = [
        ["A", "B", "C", "H", "E", "F"],
        ["P", "Q", "A", "S", "T", "G"],
        ["L", "B", "W", "V", "U", "H"],
        ["N", "M", "L", "K", "K", "I"],
    ]

    start = "S"
    res = solve(start, matrix)
    print(res, "start = 'S'")
