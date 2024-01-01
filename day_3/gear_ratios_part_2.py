from typing import List


def part_number_already_used(row: int, col: int, content, used) -> int:
    start_col, end_col = col, col
    while start_col >= 0 and content[row][start_col].isdigit():
        start_col -= 1
    start_col += 1
    while end_col < len(content[row]) and content[row][end_col].isdigit():
        end_col += 1
    end_col -= 1
    if (row, start_col, end_col) not in used:
        return False
    return True


def get_number(row: int, col: int, content, used) -> int:
    start_col, end_col = col, col
    result = 0
    while start_col >= 0 and content[row][start_col].isdigit():
        start_col -= 1
    start_col += 1
    while end_col < len(content[row]) and content[row][end_col].isdigit():
        end_col += 1
    end_col -= 1
    if (row, start_col, end_col) not in used:
        used.add((row, start_col, end_col))
        result = int(content[row][start_col: end_col + 1])
    return result


def get_adjacent_part_number(row: int, col: int, content, used: set) -> int:
    row_num, col_num = -1, -1
    result = 0
    if row - 1 >= 0 and content[row - 1][col].isdigit() and not part_number_already_used(row - 1, col, content, used):
        row_num = row - 1
        col_num = col
    elif row + 1 < len(content) and content[row + 1][col].isdigit() and not part_number_already_used(row + 1, col,
                                                                                                     content, used) > 0:
        row_num = row + 1
        col_num = col
    elif row - 1 >= 0 and col + 1 < len(content[row]) and content[row - 1][col + 1].isdigit() and \
            not part_number_already_used(row - 1, col + 1, content, used) > 0:
        row_num = row - 1
        col_num = col + 1
    elif row + 1 < len(content) and col - 1 >= 0 and content[row + 1][col - 1].isdigit() and \
            not part_number_already_used(row + 1, col - 1, content, used) > 0:
        row_num = row + 1
        col_num = col - 1
    elif col + 1 < len(content[row]) and content[row][col + 1].isdigit() and \
            not part_number_already_used(row, col + 1, content, used) > 0:
        row_num = row
        col_num = col + 1
    elif col - 1 >= 0 and content[row][col - 1].isdigit() and \
            not part_number_already_used(row, col - 1, content, used) > 0:
        row_num = row
        col_num = col - 1
    elif row + 1 < len(content) and col + 1 < len(content[row]) and content[row + 1][col + 1].isdigit() and \
            not part_number_already_used(row + 1, col + 1, content, used) > 0:
        row_num = row + 1
        col_num = col + 1
    elif row - 1 >= 0 and col - 1 >= 0 and content[row - 1][col - 1].isdigit() and \
            not part_number_already_used(row - 1, col - 1, content, used) > 0:
        row_num = row - 1
        col_num = col - 1
    if row_num != -1 and col_num != -1:
        result = get_number(row_num, col_num, content, used)
    return result


def gear_ratio(row: int, col: int, content: List) -> int:
    used = set()
    adjacent_num1 = get_adjacent_part_number(row, col, content, used)
    adjacent_num2 = get_adjacent_part_number(row, col, content, used)
    return adjacent_num1 * adjacent_num2


def sum_gear_ratio(content: List) -> int:
    sum_part = 0
    for row in range(len(content)):
        for col in range(len(content[row])):
            if content[row][col] == "*":
                sum_part += gear_ratio(row, col, content)
    return sum_part


def run_tests():
    input_test_file = "test.txt"
    with open(input_test_file, "r") as input_file:
        content = input_file.read()
        actual_sum = sum_gear_ratio(content.splitlines())
        assert actual_sum == 467835, f"Test case failed! Expected 467835 but got {actual_sum}"
    print("Tests ran successfully !!!")


def main():
    input_test_file = "input.txt"
    with open(input_test_file, "r") as input_file:
        content = input_file.read()
        result = sum_gear_ratio(content.splitlines())
        print(f"Gear ratio: {result}")


if __name__ == "__main__":
    run_tests()
    main()
