import sys, os
input = os.path.dirname(os.path.abspath(__file__)) + '/input'


def anyways():
	p1 = False
	p2 = False
	s = set()
	for a in range(num_len):
		if p1 and p2:
			print("part1", p1)
			print("part2", p2)
			return
		if p1 is False and (2020 - nums[a] in s):
			p1 = nums[a] * (2020 - nums[a])
		s.add(nums[a])
		for b in range(a + 1, num_len):
			for c in range(b + 1, num_len):
				if nums[a] + nums[b] + nums[c] == 2020:
					p2 = nums[a] * nums[b] * nums[c]


with open(input, 'r') as f:
	nums = [int(l) for l in f.readlines()]
	num_len = len(nums)
	f.close()
anyways()