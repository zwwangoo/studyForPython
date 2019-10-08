'''
$ python argparse_demo.py --help
$ python argparse_demo.py 2 -f -v 1 -mq
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int,
                    help="display the square of a given number")
# 指定默认值
parser.add_argument('-f', '--file', default='./input.csv', help='input file')
# 不需要带参数的短命令  action='store_true'
parser.add_argument(
    '-m', '--merge', help='merge all csv file.', action='store_true')
# 限定参数选定范围
parser.add_argument('-v', '--verbosity', type=int,
                    help='increase output verbosity', choices=[1, 2, 3])
# parser.add_argument('cmd', help='cmd select from "start", "stop"')

# 或
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quit', help='quit', action='store_true')
group.add_argument('-w', '--write', help='write', action='store_true')

args = parser.parse_args()
answer = args.square ** 2

if args.merge:
    print('merge')

if args.verbosity:
    print(args.verbosity)

if args.quit:
    print('quit')
if args.write:
    print('write')
