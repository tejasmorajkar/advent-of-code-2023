class EngineSchematicAnalyzer:
    DIRECTIONS = [
        (-1, 0),  # Top
        (-1, 1),  # Top Right
        (0, 1),  # Right
        (1, 1),  # Bottom Right
        (1, 0),  # Bottom
        (1, -1),  # Bottom Left
        (0, -1),  # Left
        (-1, -1),  # Top Left
    ]

    def __init__(self, schematic):
        self.schematic = schematic.splitlines()
        self.processed_locations = set()

    def _is_valid_symbol(self, char) -> bool:
        return not (char.isdigit() or char == ".")

    def _is_adjacent_to_symbol(self, row_idx, col_idx) -> bool:
        for dx, dy in self.DIRECTIONS:
            if (0 <= (row_idx + dx) < len(self.schematic)) and \
                    (0 <= (col_idx + dy) < len(self.schematic[row_idx])) and \
                    self._is_valid_symbol(self.schematic[row_idx + dx][col_idx + dy]):
                return True
        return False

    def _get_full_part_number(self, row_idx, col_idx) -> int:
        part_num = self.schematic[row_idx][col_idx]
        start_idx, end_idx = col_idx - 1, col_idx + 1
        while start_idx >= 0 and self.schematic[row_idx][start_idx].isdigit():
            part_num = self.schematic[row_idx][start_idx] + part_num
            start_idx -= 1
        while end_idx < len(self.schematic[row_idx]) and self.schematic[row_idx][end_idx].isdigit():
            part_num += self.schematic[row_idx][end_idx]
            end_idx += 1
        return int(part_num)

    def sum_part_numbers(self):
        result_sum = 0
        for row_idx, row in enumerate(self.schematic):
            col_idx = 0
            while col_idx < len(row):
                if row[col_idx].isdigit() and (row_idx, col_idx) not in self.processed_locations:
                    part_num = self._get_full_part_number(row_idx, col_idx)
                    self.processed_locations.update(
                        (row_idx, new_col_idx) for new_col_idx in range(col_idx + len(str(part_num))))
                    if any(self._is_adjacent_to_symbol(row_idx, new_col_idx) for new_col_idx in
                           range(col_idx, col_idx + len(str(part_num)))):
                        result_sum += part_num
                        col_idx += len(str(part_num)) - 1
                col_idx += 1
        return result_sum

    def gear_ratio(self, row_idx, col_idx):
        adjacent_num = []
        for dx, dy in self.DIRECTIONS:
            if (0 <= (row_idx + dx) < len(self.schematic)) and \
                    (0 <= (col_idx + dy) < len(self.schematic[row_idx])) and \
                    self.schematic[row_idx + dx][col_idx + dy].isdigit():
                part_num = self._get_full_part_number(row_idx + dx, col_idx + dy)
                if part_num not in adjacent_num:
                    adjacent_num.append(part_num)
        if len(adjacent_num) == 2:
            return adjacent_num[0] * adjacent_num[1]
        return 0

    def sum_gear_ratios(self):
        result_sum = 0
        for row_idx, row in enumerate(self.schematic):
            for col_idx, char in enumerate(row):
                if char == '*':
                    result_sum += self.gear_ratio(row_idx, col_idx)
        return result_sum


def test_sum_part_numbers():
    schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    part_one = EngineSchematicAnalyzer(schematic)
    actual_sum = part_one.sum_part_numbers()
    assert actual_sum == 4361, f"Test for sum of part numbers failed. Expected 4361 got {actual_sum}"
    print("Test for sum of part numbers ran successfully !!!")


def sum_part_numbers_main():
    input_file = "input.txt"
    with open(input_file, "r") as file:
        schematic = file.read()
        part_one = EngineSchematicAnalyzer(schematic)
        result = part_one.sum_part_numbers()
        print(f"Sum of Part numbers for input file: {input_file} is {result}")


def test_sum_gear_ratios():
    schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    part_two = EngineSchematicAnalyzer(schematic)
    actual_sum = part_two.sum_gear_ratios()
    assert actual_sum == 467835, f"Test for sum of gear ratios failed. Expected 467835 got {actual_sum}"
    print("Test for sum of part numbers ran successfully !!!")


def sum_gear_ratios_main():
    input_file = "input.txt"
    with open(input_file, "r") as file:
        schematic = file.read()
        part_two = EngineSchematicAnalyzer(schematic)
        result = part_two.sum_gear_ratios()
        print(f"Sum of gear ratio for input file: {input_file} is {result}")


if __name__ == "__main__":
    test_sum_part_numbers()
    sum_part_numbers_main()
    test_sum_gear_ratios()
    sum_gear_ratios_main()
