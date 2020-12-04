import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/input', 'r') as f:
	data = f.read()
	f.close()

req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
hex = "abcdef0123456789"
eclrs = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
nums = "0123456789"
p1 = 0
p2 = 0

for line in data.split("\n\n"):
	c1 = 0
	c2 = 0

	line = line.replace("\n", " ")
	for field in line.split(" "):
		if ':' not in field: continue
		key, val = field.split(":")
		
		if any(key == r for r in req):
			c1 += 1

		if key == req[0] and int(val) in range(1920, 2003): c2 += 1
		elif key == req[1] and int(val) in range(2010, 2021): c2 += 1
		elif key == req[2] and int(val) in range(2020, 2031): c2 += 1
		elif key == req[3]:
			if val[-2:] == "cm" and int(val[:-2]) >= 150 and int(val[:-2]) <= 193: c2 += 1
			elif val[-2:] == "in" and int(val[:-2]) >= 59 and int(val[:-2]) <= 76: c2 += 1
		elif key == req[4] and val[0] == "#" and len(val[1:]) == 6 and all(any(char == h for h in hex) for char in val[1:]): c2 += 1
		elif key == req[5] and any(val == ecl for ecl in eclrs): c2 += 1
		elif key == req[6] and len(val) == 9 and all(any(char == n for n in nums) for char in val): c2 += 1
		
	if c2 == len(req): p2 += 1
	if c1 == len(req): p1 += 1

print("part1", p1)
print("part2", p2)