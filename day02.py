import utils

boxes = utils.load_input("day02")


def part1(text: str) -> int:
    boxes = [tuple(map(int, box.split("x"))) for box in text.split("\n")]
    return sum(
        2 * (l * h + l * w + w * h) + min(l * h, l * w, w * h) for (l, h, w) in boxes
    )


def part2(text: str) -> int:
    boxes = [tuple(map(int, box.split("x"))) for box in text.split("\n")]
    return sum(2 * (l + h + w - max(l, h, w)) + l * h * w for (l, h, w) in boxes)


if __name__ == "__main__":
    print(part1(boxes))
    print(part2(boxes))
