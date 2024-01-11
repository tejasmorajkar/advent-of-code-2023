class Card:
    def __init__(self, card_line: str):
        self._set_winning_numbers(card_line)
        self._set_input_card_numbers(card_line)

    def _set_winning_numbers(self, card_line):
        self.winning_numbers = set()
        for num in card_line.split("|")[0].strip().split():
            self.winning_numbers.add(num)

    def _set_input_card_numbers(self, card_line):
        self.input_card_numbers = []
        for num in card_line.split("|")[1].strip().split():
            self.input_card_numbers.append(num)


class ScratchcardAnalyzer:
    def __init__(self, input_content: str):
        self.cards = [Card(line.split(":")[1]) for line in input_content.splitlines()]

    def _get_matching_count(self, card: Card):
        matching_count = 0
        for num in card.input_card_numbers:
            if num in card.winning_numbers:
                matching_count += 1
        return matching_count

    def sum_of_points(self) -> int:
        total_points = 0
        for card in self.cards:
            matching_count = self._get_matching_count(card)
            if matching_count > 0:
                current_points = pow(2, matching_count - 1)
                total_points += current_points
        return total_points

    def total_scratchcards(self) -> int:
        cards_freq = dict()
        for idx, card in enumerate(self.cards):
            card_num = idx + 1
            matching_count = self._get_matching_count(card)
            if card_num in cards_freq:
                cards_freq[card_num] += 1
            else:
                cards_freq[card_num] = 1
            for _ in range(cards_freq[card_num]):
                for next_card_num in range(card_num + 1, card_num + 1 + matching_count):
                    if next_card_num in cards_freq:
                        cards_freq[next_card_num] += 1
                    else:
                        cards_freq[next_card_num] = 1
        return sum([value for value in cards_freq.values()])


def test_sum_of_points():
    with open("test.txt", "r") as input_file:
        input_content = input_file.read()
        part_one = ScratchcardAnalyzer(input_content)
        actual_sum = part_one.sum_of_points()
        assert actual_sum == 13, f"Test for sum of points failed. Expected 13 but got {actual_sum}"
        print("Test for sum of points executed successfully!!!")


def sum_of_points_main():
    with open("input.txt", "r") as input_file:
        input_content = input_file.read()
        part_one = ScratchcardAnalyzer(input_content)
        result = part_one.sum_of_points()
        print(f"Sum of points for input file is {result}")


def test_total_scratchcards():
    input_content = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    part_two = ScratchcardAnalyzer(input_content)
    actual_total = part_two.total_scratchcards()
    assert actual_total == 30, f"Test for get total scratchcards failed. Expected 30 but got {actual_total}"
    print("Test for get total scratchcards executed successfully!!!")


def total_scratchcards_main():
    with open("input.txt", "r") as input_file:
        input_content = input_file.read()
        part_two = ScratchcardAnalyzer(input_content)
        result = part_two.total_scratchcards()
        print(f"Total scratchcards input file is {result}")


if __name__ == "__main__":
    test_sum_of_points()
    sum_of_points_main()
    test_total_scratchcards()
    total_scratchcards_main()
