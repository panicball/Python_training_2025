import os

movements = [(-1, -1),
             (-1, 0),
             (-1, 1),
             (0, -1),
             (0, 1),
             (1, -1),
             (1, 0),
             (1, 1)]

# test data for development
# grid = [
#     ['M','M','M','S','X','X','M','A','S','M'],
#     ['M','S','A','M','X','M','S','M','S','A'],
#     ['A','M','X','S','X','M','A','A','M','M'],
#     ['M','S','A','M','A','S','M','S','M','X'],
#     ['X','M','A','S','A','M','X','A','M','M'],
#     ['X','X','A','M','M','X','X','A','M','A'],
#     ['S','M','S','M','S','A','S','X','S','S'],
#     ['S','A','X','A','M','A','S','A','A','A'],
#     ['M','A','M','M','M','X','M','M','M','M'],
#     ['M','X','M','X','A','X','M','A','S','X']
# ]

keyword = "XMAS"

if os.path.isfile('grid.txt'):
    with open('grid.txt', 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

rows = len(grid)
cols = len(grid[0])
len_of_keyword = len(keyword)
visited_coordinates = []
number_of_words_found = 0

for row_index, row in enumerate(grid):
    for column_index, column in enumerate(row):
        if grid[row_index][column_index] == keyword[0]:
            for i, j in movements:
                whole_word = []
                word_coordinates = []
                for k in range(len_of_keyword):

                    new_row = row_index + k * i
                    new_col = column_index + k * j

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == keyword[k]:
                        whole_word.append(grid[new_row][new_col])
                        word_coordinates.append((new_row, new_col))

                if whole_word == list(keyword):
                    visited_coordinates.extend(word_coordinates)
                    number_of_words_found += 1

for row_index, row in enumerate(grid):
    for column_index, column in enumerate(row):
        if (row_index, column_index) not in visited_coordinates:
            grid[row_index][column_index] = '*'

print("Modified grid with unmatched letters marked:")
for row in grid:
    print(''.join(row))

print(f"Total occurrences of the keyword '{keyword}': {number_of_words_found}")
