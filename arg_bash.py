import sys
import argparse

#print all arguments passed when program is ran
# print(sys.argv)
# name = sys.argv[1]
# print('Hello ' +name)

parser = argparse.ArgumentParser(
  description='This program prints the name of my dogs '
)

parser.add_argument('-c', '--color', metavar='', required=True,
help='the color to search for', choices={'Red', 'Yellow', })

args = parser.parse_args()

print(args.color)
