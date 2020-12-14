import os
from itertools import product


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return data.splitlines()


def anyways(data):
	mem = {}
	mask = {}
	for line in data:
		line = line.split()
		if line[0] == "mask":
			maskstr = line[2]
			mask = {}
			for i, m in enumerate(maskstr):
				if m != "X": mask[i] = m
		else:
			memaddr = int(line[0][line[0].find('[') + 1:line[0].find(']')])
			binary = list(format(int(line[2]), "036b"))
			for m in mask:
				binary[m] = mask[m]
			binary = "".join(binary)
			mem[memaddr] = int(binary, 2)
	print("part1", sum(mem.values()))
	mem = {}
	mask = ""
	for line in data:
		line = line.split()
		if line[0] == "mask":
			mask = line[2]
		else:
			memaddr = list(format(int(line[0][line[0].find('[') + 1:line[0].find(']')]), "036b"))
			val = int(line[2])
			for i, m in enumerate(mask):
				if m != "0": memaddr[i] = m
			memaddr = "".join(memaddr)
			combos = product((0, 1), repeat=memaddr.count("X"))
			addrlist = [int(memaddr.replace("X", "{}").format(*n), 2) for n in combos]
			for addr in addrlist:
				mem[addr] = int(val)
	print("part2", sum(mem.values()))
	

anyways(readfile("input"))
