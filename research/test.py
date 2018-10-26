import argparse
from sys import argv

print(argv.__len__())
print(argv)

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')


args = parser.parse_args(['7', "-1", "42", '--sum'])

print(args)
print(args.integers)
print(args.accumulate)

print(args.accumulate(args.integers))
