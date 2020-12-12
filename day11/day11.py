import os


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return data.splitlines()


def count_occ2(grid, i, j, p2):
	count = 0
	dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
	for d in dirs:
		tempy, tempx = i + d[0], j + d[1]
		while 0 <= tempy < maxy and 0 <= tempx < maxx:
			if p2 and grid[tempy][tempx] == ".":
				tempy += d[0]
				tempx += d[1]
				continue
			elif grid[tempy][tempx] == "#":
				count += 1
				break
			elif grid[tempy][tempx] == "L": break
			if not p2: break
	return count


def simulate(oldgrid, p2 = False, tolerance = 4):
	while True:
		newgrid = [s[:] for s in oldgrid]
		for i, row in enumerate(newgrid):
			for j, seat in enumerate(row):
				if seat != ".":
					occ_count = count_occ2(oldgrid, i, j, p2)
					if seat == "L" and occ_count == 0: newgrid[i][j] = "#"
					elif seat == "#" and occ_count >= tolerance: newgrid[i][j] = "L"
		if oldgrid == newgrid: return sum(l.count("#") for l in oldgrid)
		oldgrid = newgrid


def anyways(data):
	oldgrid = [list(line) for line in data]
	global maxy, maxx
	maxy, maxx = len(oldgrid), len(oldgrid[0])
	print("part1", simulate([s[:] for s in oldgrid]))
	print("part2", simulate(oldgrid, True, 5))
	

anyways(readfile("input"))