from typing import List


def parse_input(input_text: str) -> List:
    plays = []
    for line in input_text.splitlines():
        hand, bid = line.split()
        plays.append((hand, int(bid)))
    return plays


# print(parse_input("""32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""))
# exit(0)

def classify_hand_type(hand: str) -> int:
    char_freq = [hand.count(char) for char in hand]
    if 5 in char_freq:
        return 7
    elif 4 in char_freq:
        return 6
    elif 3 in char_freq:
        if 2 in char_freq:
            return 5
        return 4
    elif char_freq.count(2) == 4:
        return 3
    elif char_freq.count(2) == 2:
        return 2
    return 1


# print(classify_hand_type("T55J5"))
# exit(0)


def joker_replacements(hand: str) -> list:
    if hand == "":
        return [""]
    return [
        prefix_char + suffix_char
        for prefix_char in ("23456789TKQA" if hand[0] == "J" else hand[0])
        for suffix_char in joker_replacements(hand[1:])
    ]


# print(joker_replacements("T55J5"))
# exit(0)


def maximize_hand_type(hand: str) -> int:
    return max(classify_hand_type(hand) for hand in joker_replacements(hand))


# print(maximize_hand_type("T55J5"))
# exit(0)


def get_rank(hand: str) -> tuple:
    letter_mapping = {
        'T': 'A',
        'J': '0',
        'Q': 'C',
        'K': 'D',
        'A': 'E'
    }
    return maximize_hand_type(hand), "".join([letter_mapping.get(char, char) for char in hand])


# print(get_rank("T55J5"))
# exit(0)


def calculate_total_winnings(plays: List) -> int:
    plays.sort(key=lambda play: get_rank(play[0]))
    total = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        total += (rank * bid)
    return total


def test_camel_cards_part2():
    with (open("test.txt", "r") as input_file):
        input_text = input_file.read()
        plays = parse_input(input_text)
        actual_result = calculate_total_winnings(plays)
        assert actual_result == 5905, (f"Test for calculating total winnings failed!!! "
                                       f"Expected 5905, but got {actual_result}")


def camel_cards_part2_main():
    with (open("input.txt", "r") as input_file):
        input_text = input_file.read()
        plays = parse_input(input_text)
        result = calculate_total_winnings(plays)
        print(result)


if __name__ == "__main__":
    test_camel_cards_part2()
    camel_cards_part2_main()
