import utils

floors = utils.load_input("day01")


def part1(text: str) -> int:
    return sum(1 if floor == "(" else -1 for floor in text)


def part2(text: str) -> int:
    floor = 0
    for idx, char in enumerate(text):
        floor += 1 if char == "(" else -1
        if floor < 0:
            return idx + 1
    return -1


if __name__ == "__main__":
    print(part1(floors))
    print(part2(floors))
