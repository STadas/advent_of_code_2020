import os


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()

		f.close()
	return data.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0").splitlines()


def anyways(data):
	p1 = 0
	p2 = 0
	sids = []
	for line in data:
		sid = int(line, 2)
		sids.append(sid)
		p1 = sid if sid > p1 else p1
	
	print("part1", p1)

	sids.sort()
	
	for i in range(len(sids)):
		if sids[i] - 1 > sids[i - 1]:
			p2 = sids[i] - 1
			break
		
	print("part2", p2)


anyways(readfile("input"))
print("--- bb ---")
anyways(readfile("bb"))