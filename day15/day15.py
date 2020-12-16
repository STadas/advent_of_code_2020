import os


def anyways(data, thnum):
	data_dict = {num: i for i, num in enumerate(data)}
	index = len(data) - 1
	currnum = data[-1]

	ans = 0
	while index < thnum:
		ans = currnum
		if data_dict[currnum] != index:
			nextnum = index - data_dict[currnum]
			data_dict[currnum] = index
			if nextnum not in data_dict:
				data_dict[nextnum] = index + 1
			currnum = nextnum
		else:
			currnum = 0
		index += 1
	return ans


data = [0, 13, 1, 16, 6, 17]
print("part1", anyways(data, 2020))
print("part2", anyways(data, 30000000))
