#!/usr/bin/env python
import argparse, random

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="number of words to print, default=6", default=6)
args = parser.parse_args()

words = []
r = random.SystemRandom()
with open('eff_large_wordlist.txt') as f:
    lines = f.readlines()
    for x in range(args.n):
        words.append(r.choice(lines).split()[1])
print(' '.join(words))
