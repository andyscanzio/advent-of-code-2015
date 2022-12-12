import utils

wires = utils.load_input("day07")


def get_value(
    wire: str, wires: dict[str, tuple[str, ...]], cache: dict[str, int]
) -> int:
    if wire in cache:
        return cache[wire]
    if wire.isdigit():
        return int(wire)
    check = wires[wire]
    if len(check) == 1:
        w = check[0]
        if w.isdigit():
            cache[wire] = int(w)
            return cache[wire]
        cache[wire] = get_value(w, wires, cache)
        return cache[wire]
    elif len(check) == 2:
        cache[wire] = ~get_value(check[0], wires, cache) & 0xFFFF
        return cache[wire]
    else:
        match check:
            case left, "AND", right:
                cache[wire] = get_value(left, wires, cache) & get_value(
                    right, wires, cache
                )
                return cache[wire]
            case left, "OR", right:
                cache[wire] = get_value(left, wires, cache) | get_value(
                    right, wires, cache
                )
                return cache[wire]
            case left, "LSHIFT", right:
                cache[wire] = get_value(left, wires, cache) << get_value(
                    right, wires, cache
                )
                return cache[wire]
            case left, "RSHIFT", right:
                cache[wire] = get_value(left, wires, cache) >> get_value(
                    right, wires, cache
                )
                return cache[wire]
            case _:
                pass
    return 0


def part1(text: str) -> int:
    wires: dict[str, tuple[str, ...]] = {}
    cache: dict[str, int] = {}
    for line in text.splitlines():
        match line.split(" "):
            case value, "->", to:
                wires[to] = (value,)
            case left, cmd, right, "->", to:
                wires[to] = (left, cmd, right)
            case cmd, fr, "->", to:
                wires[to] = (fr, cmd)
            case _:
                pass
    return get_value("a", wires, cache)


def part2(text: str) -> int:
    wires: dict[str, tuple[str, ...]] = {}
    cache: dict[str, int] = {}
    for line in text.splitlines():
        match line.split(" "):
            case value, "->", to:
                wires[to] = (value,)
            case left, cmd, right, "->", to:
                wires[to] = (left, cmd, right)
            case cmd, fr, "->", to:
                wires[to] = (fr, cmd)
            case _:
                pass
    wires["b"] = (str(part1(text)),)
    return get_value("a", wires, cache)


if __name__ == "__main__":
    print(part1(wires))
    print(part2(wires))
