class TrebuchetPartTwo:
    WORD_TO_DIGIT_MAP = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    def _calibrate_value_for_words(self, line: str) -> int:
        positions = [
            (idx, digit)
            for word, digit in self.WORD_TO_DIGIT_MAP.items()
            for idx in range(len(line)) if line.startswith(word, idx)
        ]
        positions.extend((idx, ch) for idx, ch in enumerate(line) if ch.isdigit())
        if not positions:
            return 0
        positions.sort(key=lambda x: x[0])
        first, last = positions[0][1], positions[-1][1] if len(positions) > 1 else positions[0][1]
        return int(first + last)

    def sum_calibration_values_for_words(self, lines) -> int:
        return sum(self._calibrate_value_for_words(line) for line in lines)

    def run_test_cases(self):
        part2_input = [
            ("two1nine", 29),
            ("eightwothree", 83),
            ("abcone2threexyz", 13),
            ("xtwone3four", 24),
            ("4nineeightseven2", 42),
            ("zoneight234", 14),
            ("7pqrstsixteen", 76),
            ("no_digits", 0)]
        for line, expected in part2_input:
            assert self._calibrate_value_for_words(line) == expected, f"Test case failed for line: {line}"

        assert self.sum_calibration_values_for_words([line for line, _ in part2_input]) == 281, (f"Test case failed "
                                                                                                 f"for sum")


def run_test_cases():
    TrebuchetPartTwo().run_test_cases()
    print("All tests passed successfully")


def main():
    with open("input.txt", 'r') as input_file:
        content = input_file.read()
        lines = content.splitlines()
        print(f"Sum: {TrebuchetPartTwo().sum_calibration_values_for_words(lines)}")


if __name__ == '__main__':
    run_test_cases()
    main()
