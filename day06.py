import utils

lights = utils.load_input("day06")


def part1(text: str) -> int:
    grid = [[0] * 1000 for _ in range(1000)]
    for line in text.splitlines():
        x1, x2, y1, y2 = 0, 0, 0, 0
        state = ""
        match line.split():
            case [s, p1, "through", p2]:
                state = s
                x1, y1 = tuple(map(int, p1.split(",")))
                x2, y2 = tuple(map(int, p2.split(",")))
            case ["turn", s, p1, "through", p2]:
                state = s
                x1, y1 = tuple(map(int, p1.split(",")))
                x2, y2 = tuple(map(int, p2.split(",")))
            case _:
                pass
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if state == "on":
                    grid[x][y] = 1
                elif state == "off":
                    grid[x][y] = 0
                else:
                    grid[x][y] = 1 - grid[x][y]
    return sum(sum(cell for cell in line) for line in grid)


def part2(text: str) -> int:
    grid = [[0] * 1000 for _ in range(1000)]
    for line in text.splitlines():
        x1, x2, y1, y2 = 0, 0, 0, 0
        state = ""
        match line.split():
            case [s, p1, "through", p2]:
                state = s
                x1, y1 = tuple(map(int, p1.split(",")))
                x2, y2 = tuple(map(int, p2.split(",")))
            case ["turn", s, p1, "through", p2]:
                state = s
                x1, y1 = tuple(map(int, p1.split(",")))
                x2, y2 = tuple(map(int, p2.split(",")))
            case _:
                pass
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if state == "on":
                    grid[x][y] += 1
                elif state == "off":
                    grid[x][y] = max(grid[x][y] - 1, 0)
                else:
                    grid[x][y] += 2
    return sum(sum(cell for cell in line) for line in grid)


if __name__ == "__main__":
    print(part1(lights))
    print(part2(lights))
