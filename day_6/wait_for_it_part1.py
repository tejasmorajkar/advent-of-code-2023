def parse_input(input_content: str) -> list:
    times, distances = (list(map(int, input_content.splitlines()[0].split(":")[1].split())),
                        list(map(int, input_content.splitlines()[1].split(":")[1].split())))
    records = [(times[idx], distances[idx]) for idx in range(len(times))]
    return records


def calculate_ways_to_break_each_record(time: int, dist: int) -> int:
    t = 1
    ways = 0
    while t < time:
        if t * (time - t) > dist:
            ways += 1
        elif ways > 0:
            break
        t += 1
    return ways


def multiply_ways_to_break_each_record(input_contents: str) -> int:
    records = parse_input(input_contents)
    ways = [calculate_ways_to_break_each_record(time, dist) for time, dist in records]
    result = 0
    for way in ways:
        if result:
            result = result * way
        else:
            result = way
    return result


def test_multiply_ways_to_break_each_record():
    input_content = """Time:      7  15   30
Distance:  9  40  200"""
    actual_result = multiply_ways_to_break_each_record(input_content)
    assert actual_result == 288, (f"Test for multiplying ways to break records failed."
                                  f" Expected 288 but got {actual_result}")
    print("Test 'test_multiply_ways_to_break_each_record' passed successfully !!!")


def test_multiply_ways_to_break_each_record_main():
    with open("input.txt", "r") as file:
        input_contents = file.read()
        result = multiply_ways_to_break_each_record(input_contents)
        print(result)


if __name__ == "__main__":
    test_multiply_ways_to_break_each_record()
    test_multiply_ways_to_break_each_record_main()
