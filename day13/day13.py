import os
from math import gcd


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return data.splitlines()


def anyways(data):
	a = int(data[0])
	times = data[1].split(",")
	earliest = a*2
	busid = 0
	for tstr in times:
		if tstr.isnumeric():
			t = int(tstr)
			while t < a:
				t += int(tstr)
			if t < earliest:
				earliest = t
				busid = int(tstr)
	print("part1", (earliest - a) * busid)

	times_dict = {}
	for i in range(len(times)):
		if times[i] != "x":
			times_dict[i] = int(times[i])
	n = 1
	step = 1
	for i in times_dict:
		bid = times_dict[i]
		while (n + i) % bid != 0:
			n += step
		step *= bid
	print("part2", n)


anyways(readfile("input"))