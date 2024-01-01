class TrebuchetPartOne:
    def _calibrate_value(self, line: str) -> int:
        digits = [ch for ch in line if ch.isdigit()]
        if not digits:
            return 0
        first, last = digits[0], digits[-1] if len(digits) > 1 else digits[0]
        return int(first + last)

    def sum_calibration_values(self, lines) -> int:
        return sum(self._calibrate_value(line) for line in lines)

    def run_test_cases(self):
        part1_input = [
            ("1abc2", 12),
            ("pqr3stu8vwx", 38),
            ("a1b2c3d4e5f", 15),
            ("treb7uchet", 77)]
        for line, expected in part1_input:
            assert self._calibrate_value(line) == expected, f"Test case failed for {line}"
        assert self.sum_calibration_values([line for line, _ in part1_input]) == 142, f"Test case failed for sum"


def run_test_cases():
    TrebuchetPartOne().run_test_cases()
    print("All tests passed successfully")


def main():
    with open("input.txt", 'r') as input_file:
        content = input_file.read()
        lines = content.splitlines()
        print(f"Sum: {TrebuchetPartOne().sum_calibration_values(lines)}")


if __name__ == '__main__':
    run_test_cases()
    main()
