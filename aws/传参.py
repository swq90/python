# import sys
# import argparse
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description='sum the integers at the command line')
#     parser.add_argument(
#         'integers', metavar='int', nargs='+', type=int,
#         help='an integer to be summed')
#     parser.add_argument(
#         '--log', default=sys.stdout, type=argparse.FileType('w'),
#         help='the file where the sum should be written')
#     args = parser.parse_args()
#     args.log.write('%s\n' % sum(args.integers))
#     args.log.close()

import sys
print(sys.argv)

if __name__ == '__main__':
    print
    "Program name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print
        "arg%d" % i, sys.argv[i]


# 最简单的方法： import osos.system("python filename")filename最好是全路径+文件名；
# 其他方法： execfile('xx.py')，括号内为py文件路径； 如果需要传参数，就用os.system()那种方法；
# 如果还想获得这个文件的输出，那就得用os.popen（）；