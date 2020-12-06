import os


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	# return set(int(line, 2) for line in data.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0").splitlines())
	return list(int(line, 2) for line in data.translate(data.maketrans({"B":"1", "F":"0", "R":"1", "L":"0"})).splitlines())


def anyways(data):
	print("part1", max(data))

	data.sort()
	for i in range(len(data)):
		if data[i] - 1 > data[i - 1]:
			print("part2", data[i] - 1)
			break
		

anyways(readfile("input"))
print("--- bb ---")
try:
	anyways(readfile("bigboy"))
except FileNotFoundError:
	print("(>100MB) unzip it if you wanna test it")