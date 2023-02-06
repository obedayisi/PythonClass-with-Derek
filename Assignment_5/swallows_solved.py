#!/usr/bin/python3

#import os
actors = {}
for line in open("swallows.txt"):
    if ":" in line:
        parts = line.split(":")
        key = parts.pop(0)
        if key in actors:
            actors[key].append(parts)
        else:
            actors[key] = []
            actors[key].append(parts)

for key in actors:
    print(key)
    for items in actors[key]:
        print (items)