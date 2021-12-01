import os, re


def readfile(input):
    with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
        data = f.read()
        f.close()
    return data.splitlines()


def anyways(data):
    ranges = []
    valid = set()
    attrs = []
    p1 = 0

    for i, line in enumerate(data):
        if "-" in line:
            attrs.append(line[:line.find(":")])

            pattern = re.compile("(\d+)-(\d+) or (\d+)-(\d+)")
            p_res = list(map(int, pattern.search(line).groups()))
            ranges.extend(((p_res[0], p_res[1]), (p_res[2], p_res[3])))

        elif "," in line and not "your" in data[i-1]:
            vals = tuple(map(int, line.split(",")))
            bad = False

            for v in vals:
                if not any(v in range(x, y+1) for x, y in ranges):
                    p1 += v
                    bad = True

            if not bad:
                valid.add(vals)
        elif "," in line and "your" in data[i-1]:
            your_ticket = tuple(map(int, line.split(",")))
    
    tickets_res = []
    for vals in valid:
        ticket_fits = []
        for v in vals:
            value_fits = set(int(i // 2) for i, r in enumerate(ranges) if v in range(r[0], r[1]+1))
            ticket_fits.append(value_fits)
        tickets_res.append(ticket_fits)

    p2_order = tickets_res[0]
    for ticket in tickets_res[1:]:
        for i in range(len(p2_order)):
            p2_order[i] = p2_order[i] & ticket[i]

    used = set()
    for i, v in sorted(zip(range(len(p2_order)), p2_order), key=lambda x: len(x[1])):
        p2_order[i] = list(v - used)[0]
        used.update(v)

    p2_order = [attrs[attr_i] for attr_i in p2_order]
    p2_departure_indexes = [i for i, a in enumerate(p2_order) if "departure" in a]
    
    p2 = 1
    for i in p2_departure_indexes:
        p2 *= your_ticket[i]

    print(f"{p1=}")
    print(f"{p2=}")

anyways(readfile("input"))
