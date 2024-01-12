def parse_input(input_content: str) -> list:
    input_content = input_content.splitlines()
    times, distances = list(map(int, line.split(":")[1].split()) for line in input_content)
    records = [(time, distance) for time, distance in zip(times, distances)]
    return records


def calculate_ways_to_break_each_record(records: list) -> int:
    result = 1
    for time, dist in records:
        ways = 0
        for hold in range(time):
            if hold * (time - hold) > dist:
                ways += 1
        result *= ways
    return result


def test_multiply_ways_to_break_each_record():
    input_content = """Time:      7  15   30
Distance:  9  40  200"""
    actual_result = calculate_ways_to_break_each_record(parse_input(input_content))
    assert actual_result == 288, (f"Test for multiplying ways to break records failed."
                                  f" Expected 288 but got {actual_result}")
    print("Test 'test_multiply_ways_to_break_each_record' passed successfully !!!")


def test_multiply_ways_to_break_each_record_main():
    with open("input.txt", "r") as file:
        input_content = file.read()
        result = calculate_ways_to_break_each_record(parse_input(input_content))
        print(result)


if __name__ == "__main__":
    test_multiply_ways_to_break_each_record()
    test_multiply_ways_to_break_each_record_main()
