import os


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return data.splitlines()


def rotate(rot):
	if rot == [0, 1]: return [-1, 0]
	elif rot == [-1, 0]: return [0, -1]
	elif rot == [0, -1]: return [1, 0]
	elif rot == [1, 0]: return [0, 1]


def reverserotate(rot):
	if rot == [0, 1]: return [1, 0]
	elif rot == [1, 0]: return [0, -1]
	elif rot == [0, -1]: return [-1, 0]
	elif rot == [-1, 0]: return [0, 1]


def p2rotate(rot):
	if rot == [1, 1]: return [-1, 1]
	elif rot == [-1, 1]: return [-1, -1]
	elif rot == [-1, -1]: return [1, -1]
	elif rot == [1, -1]: return [1, 1]


def p2reverserotate(rot):
	if rot == [1, 1]: return [1, -1]
	elif rot == [1, -1]: return [-1, -1]
	elif rot == [-1, -1]: return [-1, 1]
	elif rot == [-1, 1]: return [1, 1]


def anyways(data):
	ypos, xpos = 0, 0
	rot = [0, 1]
	for line in data:
		action = line[0]
		val = int(line[1:])
		if action == "N":
			ypos += val
		elif action == "E":
			xpos += val
		elif action == "S":
			ypos -= val
		elif action == "W":
			xpos -= val
		elif action == "F":
			ypos += rot[0] * val
			xpos += rot[1] * val
		elif action == "R":
			for i in range(val//90):
				rot = rotate(rot)
		elif action == "L":
			for i in range(val//90):
				rot = reverserotate(rot)
	print("part1", abs(ypos) + abs(xpos))

	ypos, xpos = 0, 0
	wypos, wxpos = 1, 10
	rot = [1, 1]
	for line in data:
		action = line[0]
		val = int(line[1:])
		if action == "N":
			wypos += val
		elif action == "E":
			wxpos += val
		elif action == "S":
			wypos -= val
		elif action == "W":
			wxpos -= val
		elif action == "F":
			ypos += wypos * val
			xpos += wxpos * val
		elif action == "R":
			for i in range(val//90):
				rot = p2rotate(rot)
				tempypos = wypos
				wypos = abs(wxpos) * rot[0]
				wxpos = abs(tempypos) * rot[1]
				# print(wypos, wxpos, rot)
		elif action == "L":
			for i in range(val//90):
				rot = p2reverserotate(rot)
				tempypos = wypos
				wypos = abs(wxpos) * rot[0]
				wxpos = abs(tempypos) * rot[1]
				# print(wypos, wxpos)
		absy = abs(wypos)
		absx = abs(wxpos)
		rot[0] = wypos // absy if absy != 0 else rot[0]
		rot[1] = wxpos // absx if absx != 0 else rot[1]
		
		# print(ypos, xpos, rot, wypos, wxpos)
	print("part2", abs(ypos) + abs(xpos))
	

anyways(readfile("input"))