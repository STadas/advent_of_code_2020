import os, resource, sys


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return set(int(l) for l in data.splitlines())


def mmmyesrecursive(num, data):
	if num in data:
		if num in mem.keys():
			return mem[num]
		mem[num] = mmmyesrecursive(num - 1, data) + \
			mmmyesrecursive(num - 2, data) + \
			mmmyesrecursive(num - 3, data)
		return mem[num]
	else: return 0


def anyways(data):
	data.add(0)
	data.add(max(data) + 3)
	checked = set()
	ichij = 0
	sanj = 0
	for num in data:
		if num - 1 in data and num - 1 not in checked:
			ichij += 1
			checked.add(num - 1)
		elif num - 2 in data and num - 2 not in checked:
			checked.add(num - 2)
		elif num - 3 in data and num - 3 not in checked:
			sanj += 1
			checked.add(num - 3)
	print("part1", ichij * sanj)

	print("part2", mmmyesrecursive(max(data), data))
		

mem = {0: 1}
anyways(readfile("input"))
print("--- bb ---")
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
mem = {0: 1}
anyways(readfile("bb"))