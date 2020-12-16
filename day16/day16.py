import os, re


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return data.splitlines()


def anyways(data):
	ranges = []
	valid = []
	attrs = 0
	p1 = 0
	for i, line in enumerate(data):
		if "-" in line:
			attrs += 1
			pattern = re.compile("([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)")
			res = pattern.search(line)
			min1, max1, min2, max2 = [int(num) for num in res.groups()]
			ranges.extend([[min1, max1], [min2, max2]])
		elif "," in line and data[i-1][:4] != "your":
			vals = [int(n) for n in line.split(",")]
			bad = False
			for num in vals:
				if not any(num in range(x, y+1) for x, y in ranges):
					bad = True
					p1 += num
			if not bad and vals not in valid:
				valid.append(vals)
	print("part1", p1)
	print("part2", "looks tedious as hell cba")


anyways(readfile("input"))