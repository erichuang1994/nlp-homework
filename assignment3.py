
# -*- coding:UTF-8 -*-
def Q1():
    print '''(1)匹配任意连续的字母组合；(2)匹配首字母大写之后小写的字母组合（可以仅有一个大写字母）；(3)匹配首字母为p尾字母为t中间为少于等于两个小写元音字母的字母串；(4)匹配一个数，若其有小数部分将小数部分分组(5)匹配3k+1为非小写元音字母3k+2为小写元音字母3k+3为非小写元音字母的字符串，同时将前三个字母分组（可以匹配空串）;(6)匹配多个（大于等与1）数字与字母组成或者全由不含数字、字母以及空格符所组成的长度不小于1的字符串。'''
#Q1
# (1)匹配任意连续的字母组合；(2)匹配首字母大写之后小写的字母组合（可以仅有一个大写字母）；(3)匹配首字母为p尾字母为t中间为少于等于两个小写元音字母的字母串；(4)匹配一个数，若其有小数部分将小数部分分组(5)匹配3k+1为非小写元音字母3k+2为小写元音字母3k+3为非小写元音字母的字符串，同时将前三个字母分组（可以匹配空串）;(6)匹配多个（大于等与1）数字与字母组成或者全由不含数字、字母以及空格符所组成的长度不小于1的字符串。
def Q2():
    # 一种方法
    # data=[ [w.split()[0],int(w.split()[1])] for w in open('data.txt','r').readlines()]
    # 另一种方法
    data=map(lambda x:[x.split()[0],int(x.split()[1])],open('data.txt','r').readlines())
    print data
def Q3():
    silly='newly formed bland ideas are inexpressible in an infuriating way'
    # 分割
    bland=silly.split()
    print bland
    # 得到'eoldrnnnna'
    str1=''.join(map(lambda x:x[1],bland))
    print str1
    # 组装
    str2=' '.join(bland)
    print str2
if __name__=="__main__":
    Q1()
    Q2()
    Q3()
