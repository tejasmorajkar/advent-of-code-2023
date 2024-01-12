def parse_input(input_content: str) -> tuple:
    times, distances = (list(map(int, input_content.splitlines()[0].split(":")[1].split())),
                        list(map(int, input_content.splitlines()[1].split(":")[1].split())))
    time, distance = "", ""
    for idx in range(len(times)):
        time += str(times[idx])
        distance += str(distances[idx])
    return int(time), int(distance)


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


def test_calculate_ways_to_break_each_record():
    input_content = """Time:      7  15   30
Distance:  9  40  200"""
    time, dist = parse_input(input_content)
    actual_result = calculate_ways_to_break_each_record(time, dist)
    assert actual_result == 71503, (f"Test for multiplying ways to break records failed."
                                    f" Expected 71503 but got {actual_result}")
    print("Test 'test_multiply_ways_to_break_each_record' passed successfully !!!")


def calculate_ways_to_break_each_record_main():
    with open("input.txt", "r") as file:
        input_contents = file.read()
        time, dist = parse_input(input_contents)
        ways = calculate_ways_to_break_each_record(time, dist)
        print(ways)


if __name__ == "__main__":
    test_calculate_ways_to_break_each_record()
    calculate_ways_to_break_each_record_main()
