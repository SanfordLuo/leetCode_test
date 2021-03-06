"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:   输入: haystack = "hello", needle = "ll"   输出: 2
示例 2:   输入: haystack = "aaaaa", needle = "bba"  输出: -1
说明: 当 needle 是空字符串时，我们应当返回 0

"""


def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    elif needle not in haystack:
        return -1
    return haystack.index(needle)


if __name__ == '__main__':
    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack, needle))
