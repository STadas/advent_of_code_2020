import os


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return [int(l) for l in data.splitlines()]


def anyways(data):
	p1 = 0
	preamble = []
	for num in data:
		if len(preamble) >= 25 and not any(preamble[i] + preamble[j] == num for i in range(len(preamble)) for j in range(i+1, len(preamble))):
			p1 = num
			break

		if len(preamble) >= 25: del preamble[0]
		preamble.append(num)
	print("part1", p1)

	for l in range(len(data)):
		min_n = data[l]
		max_n = data[l]
		sum_n = min_n
		for k in range(l+1, len(data)):
			if data[k] < min_n: min_n = data[k]
			if data[k] > max_n: max_n = data[k]
			if sum_n + data[k] == p1:
				print("part2", min_n + max_n)
				return
			elif sum_n + data[k] > p1:
				break
			sum_n += data[k]


anyways(readfile("input"))