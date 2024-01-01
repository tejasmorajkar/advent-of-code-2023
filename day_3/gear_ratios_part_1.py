from typing import List


def is_symbol(s: str) -> bool:
    return s != '.' and not s.isdigit()


def is_part_number(row: int, col: int, content: List) -> bool:
    if (row - 1 >= 0 and is_symbol(content[row - 1][col])) or \
            (row - 1 >= 0 and col + 1 < len(content[row]) and is_symbol(content[row - 1][col + 1])) or \
            (col + 1 < len(content[row]) and is_symbol(content[row][col + 1])) or \
            (row + 1 < len(content) and col + 1 < len(content[row]) and is_symbol(content[row + 1][col + 1])) or \
            (row + 1 < len(content) and is_symbol(content[row + 1][col])) or \
            (row + 1 < len(content) and col - 1 >= 0 and is_symbol(content[row + 1][col - 1])) or \
            (col - 1 >= 0 and is_symbol(content[row][col - 1])) or \
            (row - 1 >= 0 and col - 1 >= 0 and is_symbol(content[row - 1][col - 1])):
        return True
    return False


def sum_part_numbers(content: List) -> int:
    sum_part, num = 0, ""
    row = 0
    while row < len(content):
        col = 0
        while col < len(content[row]):
            if content[row][col].isdigit() and is_part_number(row, col, content):
                start, end = col, col
                while start >= 0 and content[row][start].isdigit():
                    start -= 1
                start += 1
                while end < len(content[row]) and content[row][end].isdigit():
                    end += 1
                end -= 1
                num = int(content[row][start: end + 1])
                col = end + 1
                sum_part += num
            else:
                col += 1
        row += 1
    return sum_part


def run_tests():
    input_test_file = "test.txt"
    with open(input_test_file, "r") as input_file:
        content = input_file.read()
        actual_sum = sum_part_numbers(content.splitlines())
        assert actual_sum == 4361, f"Test case failed! Expected 4361 but got {actual_sum}"
    print("Tests ran successfully !!!")


def main():
    input_test_file = "input.txt"
    with open(input_test_file, "r") as input_file:
        content = input_file.read()
        sum_part_num = sum_part_numbers(content.splitlines())
        print(f"Sum of part numbers: {sum_part_num}")


if __name__ == "__main__":
    run_tests()
    main()
