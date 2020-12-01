import sys, os

input = os.path.dirname(os.path.abspath(__file__)) + '/input'


def anyways():
	a = 0
	p1 = 0
	for a in range(num_len):
		b = a + 1
		for b in range(num_len):
			if nums[a] + nums[b] == 2020 and p1 == 0:
				p1 = nums[a] * nums[b]
				print("part1", p1)
			for c in range(num_len):
				if nums[a] + nums[b] + nums[c] == 2020:
					print("part2", nums[a] * nums[b] * nums[c])
					return


with open(input, 'r') as f:
	nums = [int(l) for l in f.readlines()]
	num_len = len(nums)
	f.close()
anyways()