#!/usr/bin/env python
import argparse, random

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="number of words to print, default=6", default=6)
args = parser.parse_args()

r = random.SystemRandom()
with open('eff_large_wordlist.txt') as f:
    lines = f.readlines()
    print(' '.join(r.choice(lines).split()[1] for i in range(args.n)))
