# common functions
import os


def read_from_file(file_path: str = os.getcwd()) -> list[list[str]]:
    if os.path.isfile('grid.txt'):
        with open('grid.txt', 'r') as file:
            grid = [list(line.strip()) for line in file.readlines()]
    return grid


def grid_modification(input_grid: list[list[str]], coordinates: list[tuple[int, int]]):
    for row_index, row in enumerate(input_grid):
        for column_index, column in enumerate(row):
            if (row_index, column_index) not in coordinates:
                input_grid[row_index][column_index] = '*'
    return input_grid


def list_to_string(input_grid: list[list[str]]):
    print("Modified grid with unmatched letters marked:")
    print('\n'.join([''.join(row) for row in input_grid]))
