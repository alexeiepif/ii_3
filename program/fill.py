#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from copy import deepcopy
from typing import Generator

from tree import Problem
from tree import depth_first_recursive_search as dfs

# Flood fill (также известный как seed fill) - это алгоритм,
# определяющий область, связанную с заданным узлом в многомерном массиве.
# Он используется в инструменте заливки "ведро" в программе рисования для
# заполнения соединенных одинаково окрашенных областей другим цветом,
# а также в таких играх, как Go и Minesweeper, для определения того,
# какие фигуры очищены. Когда заливка применяется на изображении для
# заполнения цветом определенной ограниченной области,
#  она также известна как заливка границ.
# Алгоритм заливки принимает три параметра:
# начальный узел, целевой цвет и цвет замены.


class FillProblem(Problem):
    def __init__(
        self,
        initial: tuple[int, int],
        goal: tuple[int, int] | None,
        matrix: list[list[str]],
        target_color: str,
        replacement_color: str,
    ) -> None:
        super().__init__(initial, goal)
        self.matrix = deepcopy(matrix)
        self.target_color = target_color
        self.replacement_color = replacement_color

    def actions(self, state: tuple[int, int]) -> Generator[tuple[int, int], None, None]:
        r, c = state
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            if (
                0 <= r + dr < len(self.matrix)
                and 0 <= c + dc < len(self.matrix[0])
                and self.matrix[r + dr][c + dc] == self.target_color
            ):
                yield (r + dr, c + dc)

    def result(
        self, state: tuple[int, int], action: tuple[int, int]
    ) -> tuple[int, int]:
        self.matrix[action[0]][action[1]] = self.replacement_color
        return action


def solve(
    initial: tuple[int, int],
    goal: tuple[int, int] | None,
    matrix: list[list[str]],
    target_color: str,
    replacement_color: str,
) -> list[list[str]]:
    problem = FillProblem(initial, goal, matrix, target_color, replacement_color)
    dfs(problem)
    return problem.matrix


if __name__ == "__main__":
    matrix = [
        ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
        ["Y", "Y", "Y", "Y", "Y", "Y", "G", "X", "X", "X"],
        ["G", "G", "G", "G", "G", "G", "G", "X", "X", "X"],
        ["W", "W", "W", "W", "W", "G", "G", "G", "G", "X"],
        ["W", "R", "R", "R", "R", "R", "G", "X", "X", "X"],
        ["W", "W", "W", "R", "R", "G", "G", "X", "X", "X"],
        ["W", "B", "W", "R", "R", "R", "R", "R", "R", "X"],
        ["W", "B", "B", "B", "B", "R", "R", "X", "X", "X"],
        ["W", "B", "B", "X", "B", "B", "B", "B", "X", "X"],
        ["W", "B", "B", "X", "X", "X", "X", "X", "X", "X"],
    ]
    print("X-->C")
    start_node = (3, 9)
    target_color = "X"
    replacement_color = "C"

    new_matrix = solve(start_node, None, matrix, target_color, replacement_color)
    for row in new_matrix:
        print(row)
    print("\nG-->V")
    start_node = (0, 3)
    target_color = "G"
    replacement_color = "V"

    new_matrix = solve(start_node, None, matrix, target_color, replacement_color)
    for row in new_matrix:
        print(row)
