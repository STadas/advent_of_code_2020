import os


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()

		f.close()
	return data.split("\n\n")


def anyways(data):
	p1 = 0
	p2 = 0
	for line in data:
		people = len(line.splitlines())
		line = line.replace("\n", "")
		s = set(line)
		p1 += len(s)
		for c in s:
			if line.count(c) == people: p2 += 1
	
	print("part1", p1)
	print("part2", p2)


anyways(readfile("input"))