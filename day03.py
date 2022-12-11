import utils

directions = utils.load_input("day03")


def new_pos(pos: tuple[int, int], dir: str) -> tuple[int, int]:
    x, y = pos
    match dir:
        case "<":
            return x - 1, y
        case ">":
            return x + 1, y
        case "^":
            return x, y + 1
        case _:
            return x, y - 1


def part1(text: str) -> int:
    pos: tuple[int, int] = (0, 0)
    houses: set[tuple[int, int]] = {pos}
    for direction in text:
        pos = new_pos(pos, direction)
        houses.add(pos)
    return len(houses)


def part2(text: str) -> int:
    pos_santa: tuple[int, int] = (0, 0)
    pos_robot: tuple[int, int] = (0, 0)
    houses: set[tuple[int, int]] = {pos_santa, pos_robot}
    for idx, direction in enumerate(text):
        if idx % 2 == 0:
            pos_santa = new_pos(pos_santa, direction)
            houses.add(pos_santa)
        else:
            pos_robot = new_pos(pos_robot, direction)
            houses.add(pos_robot)
    return len(houses)


if __name__ == "__main__":
    print(part1(directions))
    print(part2(directions))
