def del_array_three(array_row: list) -> list:
    result = []
    count_del = 0
    result.append(array_row[:3])
    while count_del != 2:
        array_row = array_row[3:]
        result.append(array_row[:3])
        count_del += 1
    return result


def map_sudoku(count_row: list) -> list:
    """
    Функция принимает на вход двумерный список строк судоку и возвращает
    двумерный список, где каждый список - это 1 блок из 9 судоку
    """
    map_sudoku_array = []
    for item_row in count_row:
        map_sudoku_array.append(del_array_three(item_row))
    return map_sudoku_array


def print_map_sudoku(map_array_sudoku: list) -> None:
    for item_row in map_array_sudoku:
        print(item_row)


def sudoku_solver_column_row(map_for_solver: list) -> dict:
    """
    Функция принимает на вход 9 списков внутри одного списка (двумерный список),
    в каждом списке еще 3 списка и словарь из собранных строк и колонок для проверки
    """
    Dict_result = {}
    row_numbers = []
    row = []
    column = []
    result_map_sudoku_row = [] #лежат строки row
    result_map_sudoku_column = [] #лежат колонки column
    str_number = ""
    pointer = 0
    for row_item in map_for_solver:
        for element_row_item in row_item:
            row_numbers.append("".join(element_row_item))
        for item in range(len(row_numbers)):
            str_number += row_numbers[item]
        row.append(str_number)
        result_map_sudoku_row.append(row)
        row_numbers = []
        row = []
        str_number = ""
    while pointer != 9:
        for item_row in result_map_sudoku_row:
            column.append(item_row[0][pointer])
        result_map_sudoku_column.append("".join(column))
        column = []
        pointer += 1
    Dict_result[1] = result_map_sudoku_row
    Dict_result[2] = result_map_sudoku_column
    return Dict_result


def sudoku_solver_block(map_for_solver: list, dict_solver: dict) -> list:
    """
    Функция принимает на вход карту судоку и словарь в котором содержатся 2 списка:
    1. Список из цифр строки key = 1
    2. Список из цифр колонки key = 2
    возвращает словарь, который состоит списка цифр блока 3x3
    """
    block_element = []
    time_element_block = []
    cout_element_block = 0
    for pointer in range(0, 3, 1):
        for item in map_for_solver:
            if cout_element_block != 3:
                time_element_block.append(item[pointer])
                cout_element_block += 1
            else:
                block_element.append(time_element_block)
                time_element_block = []
                cout_element_block = 0
    dict_solver[3] = block_element
    return dict_solver


def main():
    """
    Функция в которой выполняется программа
    """
    sudoku_row = [["5","3",".",".","7",".",".",".","."],
                  ["6",".",".","1","9","5",".",".","."],
                  [".","9","8",".",".",".",".","6","."],
                  ["8",".",".",".","6",".",".",".","3"],
                  ["4",".",".","8",".","3",".",".","1"],
                  ["7",".",".",".","2",".",".",".","6"],
                  [".","6",".",".",".",".","2","8","."],
                  [".",".",".","4","1","9",".",".","5"],
                  [".",".",".",".","8",".",".","7","9"]]
    return map_sudoku(sudoku_row)


if __name__ == "__main__":
    print(sudoku_solver_block(main()))
    #print(sudoku_solver_column_row(main()))
    #print_map_sudoku(main())

