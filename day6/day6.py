import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/input', 'r') as f:
	data = f.read()
	f.close()

p1 = 0
p2 = 0
for line in data.split("\n\n"):
	people = len(line.splitlines())
	line = line.replace("\n", "")
	unique = set(line)
	p1 += len(unique)
	p2 += sum(line.count(c) == people for c in unique)

print("part1", p1)
print("part2", p2)