import sys, os, re
input = os.path.dirname(os.path.abspath(__file__)) + '/input'

with open(input, 'r') as f:
	data = f.read()
	f.close()

res1 = 0
res2 = 0

for l in data.splitlines():
	counts, char, passw = l.split()
	min_pos, max_pos = [*map(int, counts.split("-"))]
	char = char[0]
	c = passw.count(char)
	if c >= min_pos and c <= max_pos: res1 += 1
	if (char == passw[min_pos - 1]) ^ (char == passw[max_pos - 1]): res2 += 1

print("part1", res1)
print("part2", res2)