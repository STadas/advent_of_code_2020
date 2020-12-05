import os, re

req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eclrs = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def readfile(input):
	with open(os.path.dirname(os.path.abspath(__file__)) + '/' + input, 'r') as f:
		data = f.read()
		f.close()
	return data


def anyways(data):
	p1 = 0
	p2 = 0

	for line in data.split("\n\n"):
		line = line.replace("\n", " ").split(" ")
		if len(line) < 7:
			continue
		c1 = 0
		c2 = 0
		
		for field in line:
			if ':' not in field: continue
			key, val = field.split(":")
			
			if key == "cid" and len(line) == 7:
				break
			
			if any(key == r for r in req):
				c1 += 1

			try:
				if key == req[0] and int(val) in range(1920, 2003): c2 += 1
				elif key == req[1] and int(val) in range(2010, 2021): c2 += 1
				elif key == req[2] and int(val) in range(2020, 2031): c2 += 1
				elif key == req[3]:
					if val[-2:] == "cm" and int(val[:-2]) in range(150, 194): c2 += 1
					elif val[-2:] == "in" and int(val[:-2]) in range(59, 77): c2 += 1
				elif key == req[4] and re.match("#[0-9|a-f]+", val): c2 += 1
				elif key == req[5] and any(val == ecl for ecl in eclrs): c2 += 1
				elif key == req[6] and len(val) == 9 and val.isdigit(): c2 += 1
			except ValueError:
				continue
			
		if c1 == 7: p1 += 1
		if c2 == 7: p2 += 1

	print("part1", p1)
	print("part2", p2)


anyways(readfile("input"))
print("--- bb ---")
anyways(readfile("bb"))