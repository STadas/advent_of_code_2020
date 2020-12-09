import os


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return data.splitlines()


def mmmyesrecursive(color):
	return sum(c + (c * mmmyesrecursive(b)) for b, c in bags[color].items()) # it just works™️


def anyways(data):
	for line in data:
		out, ins = line.split(" bags contain ")
		if "no other" in ins:
			bags[out] = {}
		else:
			for b in ins[:-1].split(", "):
				n, b1, b2, _ = b.split()
				bags.setdefault(out, {})[b1 + " " + b2] = int(n)

	to_check = ["shiny gold"]
	checked = ["shiny gold"]
	while to_check:
		b = to_check.pop(0)
		for out, ins in bags.items():
			if b in ins.keys() and out not in checked:
				checked.append(out)
				to_check.append(out)

	print("part1", len(checked) - 1) # THE -1 REEEEEEEEEEEEEEEEEEEEEEE
	print("part2", mmmyesrecursive("shiny gold"))


bags = {}
anyways(readfile("input"))
print("--- bb ---")
try:
	# bags = {}
	# anyways(readfile("bigboi.txt"))
	print("too slow, dont bother")
except FileNotFoundError:
	print("(>100MB) unzip it if you wanna test it")