#!/usr/bin/env python

import argparse, json

parser=argparse.ArgumentParser()
parser.add_argument('bundles', nargs="*")
args=parser.parse_args()

# print(f"Number of arguments passed {len(args.bundles)}")
# print(f"type for args.bundles: {type(args.bundles)}")
# print(f"Bundles are {args.bundles}")

try:
    with open("./inventory.json", "r") as f:
        available_bundles=json.load(f)
except Exception as e:
    print(e)

valid_bundles = list(available_bundles.keys())

if len(args.bundles) == 0:
    print(f"You are required to enter at least one of the valid bundles\n")
    print(*valid_bundles)
    exit()
else:
    diff = set(args.bundles) - set(valid_bundles)
    if len(diff) > 0:
        print(f"Bundles requested but not in valid_bundles")
        print(*diff)
        print(f"\nAll selected bundles must be in the list of valid bundles below\n")
        print(*valid_bundles)
        exit()


for bundle in args.bundles:
    if bundle in valid_bundles:
        # print(f"Bundle is {bundle}")
        # print(available_bundles[bundle]['packages'])
        packages = [package.get('name') for package in available_bundles[bundle]['packages']]
        # packages=list(iter(available_bundles[bundle]['packages']))
        print(*packages)

