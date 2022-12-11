import utils

words = utils.load_input("day05")


def is_nice_part1(word: str) -> bool:
    if "ab" in word or "cd" in word or "pq" in word or "xy" in word:
        return False
    if sum(word.count(vowel) for vowel in "aeiou") > 2:
        for idx, letter in enumerate(word[:-1]):
            if word[idx + 1] == letter:
                return True
    return False


def is_nice_part2(word: str) -> bool:
    first_rule = False
    second_rule = False
    for idx in range(len(word) - 2):
        if word[idx : idx + 2] in word[idx + 2 :]:
            first_rule = True
        if word[idx] == word[idx + 2]:
            second_rule = True
    return first_rule and second_rule


def part1(text: str) -> int:
    return sum(is_nice_part1(word) for word in text.splitlines())


def part2(text: str) -> int:
    return sum(is_nice_part2(word) for word in text.splitlines())


if __name__ == "__main__":
    print(part1(words))
    print(part2(words))
