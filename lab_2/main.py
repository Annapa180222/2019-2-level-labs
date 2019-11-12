"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    if type(num_rows) == int and type(num_cols) == int:
        return [[0] * num_cols for i in range(num_rows)]
    else:
        return []


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if type(edit_matrix) == tuple:
        new_m = list(edit_matrix)
    if len(new_m)==0:
         return new_m
    if type(add_weight) == int and type(remove_weight) == int:
        for i in range(1,len(new_m)):
            new_m[i][0] = new_m[i - 1][0] + remove_weight
            new_m[0][0]=0
            i = i+1
        for j in range(1,len(new_m[0])):
            new_m[0][j] = new_m[0][j - 1] + add_weight
            j = j+1
        return new_m
    else:
        return new_m



def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    new_m = list(edit_matrix)
    if original_word == None or target_word == None:
        return new_m
    if type(edit_matrix) == tuple and type(add_weight) == int and type(remove_weight) == int and type(substitute_weight) == int:
        for i in range(1, len(new_m)):
            for j in range(1, len(new_m[0])):
                ad = new_m[i][j-1]+add_weight
                re = new_m[i-1][j]+remove_weight
                if original_word[i-1] == target_word[j-1]:
                    su = new_m[i-1][j-1]
                else:
                    su = new_m[i - 1][j - 1] + substitute_weight
                new_m[i][j] = minimum_value((ad, re, su))
        return new_m
    else:
        return new_m


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    error = -1
    if type(original_word) == str and type(target_word) == str and type(add_weight) == int and type(remove_weight) == int and type(substitute_weight) == int:
        num_rows = len(original_word)+1
        num_cols = len(target_word)+1
        new_mtr = generate_edit_matrix(num_rows, num_cols)
        matrix = initialize_edit_matrix(tuple(new_mtr), add_weight, remove_weight)
        return fill_edit_matrix(tuple(matrix), add_weight, remove_weight, substitute_weight, original_word, target_word)[num_rows-1][num_cols-1]
    else:
        return error



def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    save_file = open(path_to_file,'w')
    for string in edit_matrix:
        row = ''
        for el in string:
            row = str(el)+','
            save_file.write(row)
        save_file.write('\n')
    save_file.close(row)


def load_from_csv(path_to_file: str) -> list:
    new_file = open(path_to_file)
    matrix = []
    for string in new_file:
        line_with_z = string.split(',')
        line =[]
        for el in line_with_z:
            line.append(int(el))
        matrix.append(line)
    return matrix



