import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/input', 'r') as f:
	data = f.read()
	f.close()

with open(os.path.dirname(os.path.abspath(__file__)) + '/bb', 'r') as f:
	bb = f.read()
	f.close()


def anyways(data):
	p1 = 0
	p2 = 0
	for line in data.splitlines():
		counts, char, passw = line.split()
		min_pos, max_pos = [*map(int, counts.split("-"))]
		char = char[0]
		c = passw.count(char)
		if c >= min_pos and c <= max_pos: p1 += 1
		if (char == passw[min_pos - 1]) ^ (char == passw[max_pos - 1]): p2 += 1
	
	print("part1", p1)
	print("part2", p2)


anyways(data)
print("--- bb ---")
anyways(bb)