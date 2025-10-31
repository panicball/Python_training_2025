# Todo:
# 1. provide any grid input DONE
# 2. provide any keyword input
# 3. count the occurrences of the keyword Done

# import copy
import os
# if __name__ == "__main__":
movements = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]

# grid = [
#     ['F', 'C', 'f', 'b'],
#     ['B', 'G', 'A', 'S'],
#     ['I', 'b', 'b', 'T'],
#     ['C', 'A', 'T', 'k']
# ]

# grid = [
#     ['F', 'C', 'G', 'T'],
#     ['B', 'G', 'A', 'T'],
#     ['I', 'T', 'A', 'Q'],
#     ['S', 'E', 'R', 'T']
# ]
# keyword = "CAT"


grid = [
    ['M','M','M','S','X','X','M','A','S','M'],
    ['M','S','A','M','X','M','S','M','S','A'],
    ['A','M','X','S','X','M','A','A','M','M'],
    ['M','S','A','M','A','S','M','S','M','X'],
    ['X','M','A','S','A','M','X','A','M','M'],
    ['X','X','A','M','M','X','X','A','M','A'],
    ['S','M','S','M','S','A','S','X','S','S'],
    ['S','A','X','A','M','A','S','A','A','A'],
    ['M','A','M','M','M','X','M','M','M','M'],
    ['M','X','M','X','A','X','M','A','S','X']
]
keyword = "XMAS"

# is failo
# if os.path.isfile('grid.txt'):
#     with open('grid.txt', 'r') as file:
#         grid = [list(line.strip()) for line in file.readlines()]


rows = len(grid)
cols = len(grid[0])
len_of_keyword = len(keyword)
visited_coordinates = []
number_of_words_found = 0

# print(f"auguste rows->{rows}, cols->{cols}")

for row_index, row in enumerate(grid):
    for column_index, column in enumerate(row):
        # print(f"auguste grid[{row_index}][{column_index}] -> {grid[row_index][column_index]}")
        if grid[row_index][column_index] == keyword[0]:
            print(f"auguste rado pirma raide {keyword[0]} in location ({row_index},{column_index})")

            for i, j in movements:
                whole_word = []
                # new_grid = copy.deepcopy(grid)
                word_coordinates = []
                for k in range(len_of_keyword):
                    # jei nenaudoju  + k * i ar j -> neislaikau zodzio vienoje tieseje
                    new_row = row_index + k * i  # starting point yra first letter + k judesiu  i kryptimi (in order to keep word in one line)
                    new_col = column_index + k * j

                    # if new_row <= rows and new_row <= cols and grid[new_row][new_col] == keyword[k]:
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == keyword[k]:
                        whole_word.append(grid[new_row][new_col])
                        word_coordinates.append((new_row, new_col))
                        print(f"auguste (k={k}) rado raide {keyword[k]} in location ({new_row},{new_col}) -> {grid[new_row][new_col]}")
                    # elif new_row <= rows and new_col <= cols and grid[new_row][new_col] != keyword[k]:
                    # elif 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != keyword[k]:
                    #     print(f"hi")
                    #     new_grid[new_row][new_col] = '*'
                    #     print(grid[new_row][new_col])
                    #     print(new_grid[new_row][new_col])

                if whole_word == list(keyword):
                    print(f"auguste rado zodi {keyword} nuo ({row_index},{column_index}) kryptimi ({i},{j})")
                    visited_coordinates.extend(word_coordinates)
                    number_of_words_found += 1
                    # naudojant .append susiformuoja list of lists [[]], tuomet feilina toliau
                    # visited_coordinates.append(word_coordinates)


for row_index, row in enumerate(grid):
    for column_index, column in enumerate(row):
        # print(f"auguste grid[{row_index}][{column_index}] -> {grid[row_index][column_index]}")
        if (row_index, column_index) not in visited_coordinates:
            grid[row_index][column_index] = '*'

print("Modified grid with unmatched letters marked:")
for row in grid:
    print(''.join(row))

print(f"Total occurrences of the keyword '{keyword}': {number_of_words_found}")

print("---------------------------------------------------------------------------")

# grid = [
#     ['F', 'C', 'G', 'T'],
#     ['B', 'G', 'A', 'T'],
#     ['I', 'T', 'A', 'Q'],
#     ['S', 'E', 'R', 'T']
# ]
# keyword = "CAT"

# for row in grid:  # judu per kiekviena 2x2 matricos eilute
#     print(f"auguste tavo eilute -> {row}")
#     for letter in row:  # judu per kiekviena eilutes raide
#         if letter == keyword[0]:  # jei eilutes raide nera same as pirmoji raktazodio - praleidziu
#             print(f"auguste rado pirma raide -> {letter}")
#             # tau reik pasiimti koordinates sios raides ir tada prie jos sumuoti 8 kryptis
#             first_letter_row_index = grid.index(row)
#             first_letter_column_index = row.index(letter)
#
#             print(f"auguste first_letter_row_index -> {first_letter_row_index}")
#             print(f"auguste first_letter_column_index -> {first_letter_column_index}")
#             # for i, j in movements:
#             #     for k in range(len(keyword)):
#             #         new_row = first_letter_row_index + k * i  # starting point yra first letter + k judesiu  i kryptimi (in order to keep word in one line)
#             #         new_col = first_letter_column_index + k * j
#             #
#             #         if grid[new_row][new_col] == keyword[k]:
#             #             print(f"auguste rado raide {keyword[k]} in direction ({i},{j}) in location ({new_row},{new_col})")
#             #         else:
#             #             break
#
#             iteration = 0
#             for i, j in movements:
#                 iteration += 1
#                 # print(f"auguste iteracija {iteration}, letter {grid[i][j]} in direction ({i},{j})")
#                 if grid[first_letter_row_index+i][first_letter_column_index+j] == keyword[1]:
#                     print(f"auguste (2) rado raide {keyword} in direction {grid[first_letter_row_index+i][first_letter_column_index+j]} in location ({first_letter_row_index+i},{first_letter_column_index+j})")
#
#                     for k, l in movements:
#                         if grid[first_letter_row_index+i+k][first_letter_column_index+j+l] == keyword[2]:
#                             print(f"auguste (3) rado zodi {keyword} in direction {grid[first_letter_row_index+i+k][first_letter_column_index+j+l]} in location ({first_letter_row_index+i+k},{first_letter_column_index+j+l})")




