from pathlib import Path


def check_expand_bounds(cells, bounds, part2):
    for c in cells:
        if c[0] == bounds["min_x"]:
            bounds["min_x"] -= 1
        if c[0] == bounds["max_x"]:
            bounds["max_x"] += 1

        if c[1] == bounds["min_y"]:
            bounds["min_y"] -= 1
        if c[1] == bounds["max_y"]:
            bounds["max_y"] += 1

        if c[2] == bounds["min_z"]:
            bounds["min_z"] -= 1
        if c[2] == bounds["max_z"]:
            bounds["max_z"] += 1

        if part2:
            if c[2] == bounds["min_w"]:
                bounds["min_w"] -= 1
            if c[2] == bounds["max_w"]:
                bounds["max_w"] += 1


def apply_rules(cells, new_cells, x, y, z, w):
    neighbors = 0
    for zn in range(z-1, z+2):
        for yn in range(y-1, y+2):
            for xn in range(x-1, x+2):
                for wn in range(w-1, w+2):
                    if (xn, yn, zn, wn) in cells:
                        neighbors += 1

    if (x, y, z, w) in cells:
        neighbors -= 1
        if 2 <= neighbors <= 3:
            new_cells.add((x, y, z, w))
        else:
            new_cells.remove((x, y, z, w))
        return

    else:
        if neighbors == 3:
            new_cells.add((x, y, z, w))
            return


def cycle(cells, new_cells, bounds):
    for z in range(bounds["min_z"], bounds["max_z"] + 1):
        for y in range(bounds["min_y"], bounds["max_y"] + 1):
            for x in range(bounds["min_x"], bounds["max_x"] + 1):
                for w in range(bounds["min_w"], bounds["max_w"] + 1):
                    apply_rules(cells, new_cells, x, y, z, w)


def solve(data, part2 = False):
    bounds = {
        "min_x": 0,
        "max_x": len(data[0])-1,
        "min_y": 0,
        "max_y": len(data)-1,
        "min_z": 0,
        "max_z": 0,
        "min_w": 0,
        "max_w": 0
    }

    cells = set()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                cells.add((x, y, 0, 0))

    for _ in range(6):
        new_cells = set(cells)
        check_expand_bounds(cells, bounds, part2)
        cycle(cells, new_cells, bounds)

        cells = new_cells

    return len(cells)

def anyways():
    with open(str(Path(__file__).parent.resolve()) + "/input") as f:
        data = f.read().splitlines()

    p1 = solve(data)
    p2 = solve(data, True)

    print(f"{p1=}")
    print(f"{p2=}")


anyways()
