# https://www.nowcoder.com/exam/oj/ta?tpId=37
# HJ1 字符串最后一个单词的长度
import sys
for line in sys.stdin:
    word=line.split()
    print(len(word[-1]))