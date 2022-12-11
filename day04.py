from hashlib import md5
from itertools import count

mine = "ckczppom"


def part1(text: str) -> int:
    for coin in count(1):
        digest = md5(f"{text}{coin}".encode()).hexdigest()
        if digest[:5] == "00000":
            return coin
    return -1


def part2(text: str) -> int:
    for coin in count(1):
        digest = md5(f"{text}{coin}".encode()).hexdigest()
        if digest[:6] == "000000":
            return coin
    return -1


if __name__ == "__main__":
    print(part1(mine))
    print(part2(mine))
