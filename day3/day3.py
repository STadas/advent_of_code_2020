import os


def readfile(input):
	with open(input, 'r') as f:
		data = f.read()
		f.close()
	
	splitdata = data.splitlines()

	return data, splitdata, len(splitdata[0]), len(splitdata)
	

def findtrees(right: int, down: int):
	count = 0
	x = 0
	for y in range(0, datalen, down):
		if splitdata[y][x] == "#":
			count += 1
		x = (x + right) % linelen
	return count


data, splitdata, linelen, datalen = readfile(os.path.dirname(os.path.abspath(__file__)) + '/input')
print("part1", findtrees(3, 1))
print("part2", findtrees(1, 1)*findtrees(3, 1)*findtrees(5, 1)*findtrees(7, 1)*findtrees(1, 2))

# bb
right_list = [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 32, 36, 48, 54, 64]
down_list = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 47]
data, splitdata, linelen, datalen = readfile(os.path.dirname(os.path.abspath(__file__)) + '/bb')
print("--- bb ---")
bbsum = 1
for r in right_list:
	for d in down_list:
		bbsum *= findtrees(r, d)
print(bbsum)