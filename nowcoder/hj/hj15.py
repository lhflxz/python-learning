# https://www.nowcoder.com/practice/440f16e490a0404786865e99c6ad91c9
# HJ15 求int型正整数在内存中存储时1的个数
import sys

for line in sys.stdin:
    a = line.split()
    print(bin(int(a[0])).count('1'))
