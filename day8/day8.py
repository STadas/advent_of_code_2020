import os


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return data.splitlines()


def anyways(data, ind = 0, out = True):
	global p1, p2
	if ind == 0:
		p1 = 0
		p2 = 0

	acc = 0
	inds = set()
	i = 0
	local_data = list(data)
	if ind != 0: local_data[ind] = "nop 0"
	while i < len(local_data):
		# if i % 1000 == 0: print(len(inds), i)
		if i in inds:
			if out and p1 == 0:
				p1 = acc
				print("part1", p1)
			if (p1 != 0 and p2 != 0) or not out:
				return

		inds.add(i)
		intcode, val = local_data[i].split()
		if intcode == "acc":
			acc += int(val)
		elif intcode == "jmp":
			if p2 == 0 and out and int(val) < 0:
				anyways(data, i, False)
			i += int(val) - 1
		elif intcode == "nop": pass
		i += 1
	p2 = acc
	print("part2", p2)


anyways(readfile("input"))
print("--- bb ---")
anyways(readfile("bb"))
# print("too slow, dont bother")