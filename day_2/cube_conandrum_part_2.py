class CubeConandrumPartTwo:
    def _power(self, game: str) -> int:
        bag = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game = game.split(':')
        game_id, sets = int(game[0].split(' ')[1]), game[1]
        for cubes in sets.split(';'):
            for cube in cubes.split(','):
                cube_count, cube_color = cube.strip().split()
                bag[cube_color] = max(bag[cube_color], int(cube_count))
        return bag["red"] * bag["green"] * bag["blue"]

    def sum_of_power(self, games) -> int:
        return sum(self._power(game) for game in games)

    def run_tests(self):
        games = [
            ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
            ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
            ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 1560),
            ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 630),
            ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36)
        ]
        for game, expected in games:
            assert self._power(game) == expected, f"Failed test case: {game}"
        assert self.sum_of_power([game[0] for game in games]) == 2286
        print("All tests run successfully !!!")


def main():
    input_file = "input.txt"
    with open(input_file, "r") as input_file:
        content = input_file.read()
        games = content.splitlines()
        result = CubeConandrumPartTwo().sum_of_power(games)
        print(f"Sum of powers: {result}")


if __name__ == "__main__":
    CubeConandrumPartTwo().run_tests()
    main()
