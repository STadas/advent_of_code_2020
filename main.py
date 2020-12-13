#!/bin/python3
import os, importlib, re
dirs = [f.name for f in os.scandir(os.path.dirname(os.path.abspath(__file__))) if f.is_dir() and f.name[0] != "." and f.name != "funnies"]
dirs.sort(key = lambda x: int(re.sub("\D", "", x)))
for d in dirs:
	print("------", d, "------")
	importlib.import_module(f"{d}.{d}")
	print()