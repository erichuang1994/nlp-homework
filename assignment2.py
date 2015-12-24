# -*- coding: UTF-8 -*- 
from __future__ import print_function
import nltk
from nltk import *
import operator
import random
def generate_model(cfdist,word,num=15):
    reminderList=list()
    for i in range(num):
        print(word,end=' ')
        reminder=random.random()
        reminderList.append(reminder)
        # print reminder
        tempDict=cfdist[word]
        # print(dict(tempDict))
        valueSum=sum([tempDict[w] for w in tempDict])
        # reminder=num%sum
        for x in tempDict:
            reminder=reminder-tempDict[x]*1.0/valueSum
            # print(reminder)
            if reminder<0:
                word=x
                break
    print()
    # print(reminderList)
    # random.randint()
def Q1():
    emma=nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
    # 总词数 192427
    print(len(emma))
    # 不同的词的个数 7811
    print(len(set(emma)))
def Q2():
    emma=nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
    bigrams=nltk.bigrams(list(emma))
    # 为了让结果更有意义，去除标点符号
    punctuation=[',','.','"','--','."',',"','!','\'','.--','?--','-','?','!--',';']
    stopwords=nltk.corpus.stopwords.words('english')
    stopwords.extend(punctuation)
    bigrams=[w for w in bigrams if w[0] not in stopwords and w[1] not in stopwords]
    fdist1=FreqDist(bigrams).most_common(50)
    print(fdist1)
def Q3():
    # Q3
    text=nltk.corpus.genesis.words('english-kjv.txt')
    bigrams=nltk.bigrams(text)
    cfd=nltk.ConditionalFreqDist(bigrams)
    # print(len(cfd['love']))
    # print(cfd['love'])
    # for x in cfd['living']:
        # print(x,cfd['living'][x])
    generate_model(cfd,'living')  
    generate_model(cfd,'Now')
    generate_model(cfd,'living')
if __name__ == '__main__':
    # emma=nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
    
    # # Q1
    # # 总词数 192427
    # print(len(emma))
    # # 不同的词的个数 7811
    # print(len(set(emma)))

    # # Q2
    # bigrams=nltk.bigrams(list(emma))
    # # 为了让结果更有意义，去除标点符号
    # punctuation=[',','.','"','--','."',',"','!','\'','.--','?--','-','?','!--',';']
    # stopwords=nltk.corpus.stopwords.words('english')
    # stopwords.extend(punctuation)
    # bigrams=[w for w in bigrams if w[0] not in stopwords and w[1] not in stopwords]
    # fdist1=FreqDist(bigrams).most_common(50)
    # print(fdist1)
    
    # # Q3
    # text=nltk.corpus.genesis.words('english-kjv.txt')
    # bigrams=nltk.bigrams(text)
    # cfd=nltk.ConditionalFreqDist(bigrams)
    # print(len(cfd['love']))
    # # print(cfd['love'])
    # for x in cfd['living']:
    #     print(x,cfd['living'][x])
    # generate_model(cfd,'living')    
    Q3()

