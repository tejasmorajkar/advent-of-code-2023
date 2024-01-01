class CubeConandrumPartOne:
    def is_game_possible(self, game: str, bag: dict) -> int:
        game = game.split(':')
        game_id, sets = int(game[0].split(' ')[1]), game[1]
        for cubes in sets.split(';'):
            for cube in cubes.split(','):
                cube_count, cube_color = cube.strip().split()
                if bag[cube_color] < int(cube_count):
                    return 0
        return game_id

    def sum_possible_games(self, games, bag) -> int:
        return sum(self.is_game_possible(game, bag) for game in games)

    def run_tests(self):
        bag = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        games = [
            ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
            ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 2),
            ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 0),
            ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 0),
            ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 5)
        ]
        for game, expected in games:
            assert (self.is_game_possible(game, bag)) == expected, f"Failed testcase for game: {game}"
        assert self.sum_possible_games([game for game, _ in games], bag) == 8, (f"Test failed for Sum of possible "
                                                                                f"games")
        print("All tests ran successfully!!!")


def main():
    input_file_path = "input.txt"
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    with open(input_file_path, "r") as input_file_path:
        content = input_file_path.read()
        games = content.splitlines()
        result = CubeConandrumPartOne().sum_possible_games(games, bag)
        print(f"Sum of possible games: {result}")


if __name__ == "__main__":
    CubeConandrumPartOne().run_tests()
    main()
