from itertools import cycle
import math


class PathAnalyzer:
    def __init__(self, input_file: str):
        self.instructions = ""
        self.network = {}
        self._parse_input(input_file)

    def _parse_input(self, file: str):
        with open(file, "r") as file:
            self.instructions, _, *rest = file.read().splitlines()
            # print(f"Instructions: {self.instructions}")
            for line in rest:
                label, neighbours = line.strip().split(" = ")
                self.network[label] = neighbours.strip()[1:-1].split(", ")
            # print(self.network)

    def count_steps_part1(self) -> int:
        curr = "AAA"
        step_count = 0

        for direction in cycle(self.instructions):
            curr = self.network[curr][0] if direction == "L" else self.network[curr][1]
            step_count += 1
            if curr == "ZZZ":
                break
        return step_count

    def count_steps_part2(self) -> int:
        start_positions = [pos for pos in self.network.keys() if pos.endswith("A")]
        cycles = []
        for start_position in start_positions:
            curr = start_position
            step_count = 0
            from itertools import cycle
            for direction in cycle(self.instructions):
                if curr.endswith("Z"):
                    break
                curr = self.network[curr][0] if direction == "L" else self.network[curr][1]
                step_count += 1
            cycles.append(step_count)
        # print(cycles)
        lcm = math.lcm(*cycles)
        return lcm


def test_count_steps_part1():
    actual_result = PathAnalyzer("part1_test1.txt").count_steps_part1()
    assert actual_result == 2, f"Test failed. Expected 2, but got {actual_result}"
    actual_result = PathAnalyzer("part1_test2.txt").count_steps_part1()
    assert actual_result == 6, f"Test failed. Expected 6, but got {actual_result}"
    print("Test for count steps part 1 passed successfully!!!")


def test_count_steps_part2():
    actual_result = PathAnalyzer("part2_test.txt").count_steps_part2()
    assert actual_result == 6, f"Test failed. Expected 6, but got {actual_result}"
    print("Test for count steps part 2 passed successfully!!!")


def count_steps_part1_main():
    result = PathAnalyzer("input.txt").count_steps_part1()
    print(result)


def count_steps_part2_main():
    result = PathAnalyzer("input.txt").count_steps_part2()
    print(result)


if __name__ == "__main__":
    test_count_steps_part1()
    count_steps_part1_main()
    test_count_steps_part2()
    count_steps_part2_main()
