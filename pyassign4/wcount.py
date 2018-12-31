"""wcount.py: count words from an Internet file.
__author__ = "YuZhongtian"
__pkuid__  = "1800011813"
__email__  = "1800011813@pku.edu.cn"
"""

import sys#引入导入url的模块
from urllib.request import urlopen
import urllib.error
def wcount(lines, topn=10):
    import copy#引入复制函数
    lines1 = copy.copy(lines)  #输入的内容复制一遍
    for letter in lines:
        if not (65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122):
            lines1 = lines1.replace(letter, ' ', 1)  # 换掉文本中不是字母的文本以防纳入统计
    lst = lines1.split()#将文本转换成可统计的列表
    counts = {}#建立空字典来统计单词
    for word in lst:
        counts[word] = counts.get(word, 0) + 1  # 用字典进行统计
    tem_list = list(counts.items())
    sorted_list = sorted(tem_list, key=lambda t: t[1])#给字典按照字数多少进行排序
    if topn >= len(sorted_list):
        out_list = sorted_list[::-1]
    else:
        out_list = []
        for a in range(1, topn + 1):
            out_list.append(sorted_list[-a])  # 递归，利用列表对结果进行排序
    out_dict = dict(out_list)
    return out_dict  # 返回输出字典，得到统计的结果
    pass
def main():#创建main主函数
    try:
        doc = urlopen(sys.argv[1])
    except urllib.error.HTTPError:
        print('Please input a valid URL')  # 当网址有问题的时候返回的结果
    except urllib.error.URLError:
        print('Please check you Internet connection')#当网络连接有问题的时候返回的结果
    else:
        doc = urlopen(sys.argv[1])
        lines = doc.read().decode()
        lines = lines.lower()  # 把url的返回值解码，转变成小写
        if len(sys.argv) <= 2:
            topn = 10
        else:
            topn = int(sys.argv[2])
        dic = wcount(lines, topn)
        for i in dic:
            print(i.ljust(15) + str(dic[i]))  # 输出统计的结果
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('url: URL of the txt file to analyze ')
        print('topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    else:
        main()
