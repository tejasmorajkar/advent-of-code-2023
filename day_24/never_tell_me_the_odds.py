import sympy


class Hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy

    def __repr__(self):
        return "Hailstone{" + f"a={self.a} b={self.b} c={self.c}" + "}"


class HailstoneTrajectoryAnalyzer:
    def __init__(self, input_content, start_limit, end_limit, use_sympy=False):
        # Replace @ with , so that we get sx, sy, sz, vx, vy, vz
        # convert these number strings to int using map and create hailstone objects with these six values
        if use_sympy:
            self.hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in
                               input_content.splitlines()]
        else:
            self.hailstones = [Hailstone(*map(int, line.replace("@", ",").split(","))) for line in
                               input_content.splitlines()]
        self.start_limit = start_limit
        self.end_limit = end_limit
        self.use_sympy = use_sympy

    def count_intersections(self) -> int:
        total_intersections = 0
        # Form pairs of hailstones and check paths
        for idx, hs1 in enumerate(self.hailstones):
            for hs2 in self.hailstones[:idx]:
                a1, b1, c1 = hs1.a, hs1.b, hs1.c
                a2, b2, c2 = hs2.a, hs2.b, hs2.c

                # If parallel paths then skip count
                if a1 * b2 == a2 * b1:
                    continue

                # Find intersection points
                x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
                y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)

                # Check if intersection point lies in test area
                if self.start_limit <= x <= self.end_limit and self.start_limit <= y <= self.end_limit:
                    # Check if intersection not happened in past
                    if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0 for hs in (hs1, hs2)):
                        total_intersections += 1

        return total_intersections

    def count_intersections_using_sympy(self) -> int:
        total_intersections = 0
        for idx, hs1 in enumerate(self.hailstones):
            for hs2 in self.hailstones[:idx]:
                px, py = sympy.symbols("px py")
                answers = sympy.solve([(px - sx) * vy - (py - sy) * vx for sx, sy, _, vx, vy, _ in (hs1, hs2)])
                if not answers:
                    continue
                x, y = answers[px], answers[py]
                if self.start_limit <= x <= self.end_limit and self.start_limit <= y <= self.end_limit:
                    if all((x - sx) * vx >= 0 and (y - sy) * vy >= 0 for sx, sy, _, vx, vy, _ in (hs1, hs2)):
                        total_intersections += 1
        return total_intersections


def test_count_intersections():
    with open("test.txt", "r") as file:
        input_content = file.read()
        part_one_test = HailstoneTrajectoryAnalyzer(input_content, 7, 27)
        actual_intersections = part_one_test.count_intersections()
        assert actual_intersections == 2, (f"Test failed for count of intersections. "
                                           f"Expected 2 but got {actual_intersections}")
        print("Test count_intersections executed successfully!!!")
        part_one_test = HailstoneTrajectoryAnalyzer(input_content, 7, 27, use_sympy=True)
        actual_intersections = part_one_test.count_intersections_using_sympy()
        assert actual_intersections == 2, (f"Test failed for count of intersections using sympy. "
                                           f"Expected 2 but got {actual_intersections}")
        print("Test count_intersections_using_sympy executed successfully!!!")


def count_intersections_main():
    with open("input.txt", "r") as file:
        input_content = file.read()
        part_one_test = HailstoneTrajectoryAnalyzer(input_content, 200000000000000, 400000000000000)
        total_intersections = part_one_test.count_intersections()
        print(total_intersections)


if __name__ == "__main__":
    test_count_intersections()
    count_intersections_main()
