# coding:utf-8
from nltk.corpus import brown
import nltk
# a. 哪些名词常以它们复数形式而不是它们的单数形式出现？（只考虑常规的复数形式，-s 后缀形式的）这里我将复数形式出现次数是单数形式的10倍以上输出
def Q11():
    word_fd=nltk.FreqDist([w for (w,t) in brown.tagged_words(tagset='universal') if t=='NOUN'])
    word_tag_fd=nltk.FreqDist(brown.tagged_words())
    wordList=[w for (w,t) in word_tag_fd if t=='NNS' and w[-2]!='\'' and w[-1]=='s' and word_tag_fd[w[:-1]]*10<word_fd[w]]
    print set(wordList)
    print len(wordList)
#b. 哪个词的不同词性标记数目最多?为了减少计算量 这里指定分类为news运行结果为'to',有6种
def Q12():
    from operator import itemgetter
    # word_tag_fd=nltk.FreqDist(brown.tagged_words())
    fd=nltk.FreqDist(brown.words(categories='news'))
    cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    newList=[(w,len(cfd[w])) for w in fd.keys()]
    newList.sort(key=lambda x:x[1])
    # pnewList,key=lambda x:x[1])[-1]
    print newList[-1]
    # print most_freq_words
# c. 按频率递减的顺序列出标记。前20 个最频繁的词性标记代表什么？同样为了减少计算机这里指定分类为news
# 运行结果为[u'NN'（名词）, u'IN（介词）', u'AT', u'NP(名词短语)', u',', u'NNS'（复数名词）, u'.', u'JJ（形容词）', u'CC（并列连词）', u'VBD(动词过去式）', u'NN-TL', u'VB(动词基本形式）', u'VBN(动词过去分词）', u'RB（副词）', u'CD(指数量词）', u'CS', u'VBG(动词现在分词或动名词）', u'TO', u'PPS', u'PP$']分别代表
def Q13():
    from collections import defaultdict
    counts=defaultdict(int)
    from nltk.corpus import brown 
    for (word,tag) in brown.tagged_words(categories='news'):
        counts[tag]+=1
    from operator import itemgetter
    ans=[w for (w,t) in sorted(counts.items(),key=itemgetter(1),reverse=True)]
    print ans[:20]
# d. 名词后面最常见的是哪些词性标记？这些标记代表什么？(结果如下)
#   .(标点符号)ADP(介词)   VERB(动词)  NOUN(名词)  CONJ(连词)  ADV（副词） PRON(代词)  PRT(虚词)  DET（限定词）  ADJ(形容词)  NUM(number)   X 
#   78192 67429 43741 41287 16426 7300 5488 4934 4491 3602 2255   99 

def Q14():
    brown_lrnd_tagged=brown.tagged_words(tagset='universal')
    tags=[b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[1]=='NOUN']
    # for (a,b) in nltk.bigrams(brown_lrnd_tagged):
        # if a[1]=='NOUN':
            # print (a,b)
            # break
    # print tags
    fd=nltk.FreqDist(tags)
    # print sorted(fd)
    print fd.tabulate()
# 例5-4 绘制曲线显示查找标注器的性能随模型的大小增加的变化。绘制当训练数据量变化时unigram 标注器的性能曲线。对于查找标注器，我按照书上的示例代码进行。对于一元标注器我采用分别用10%,20%,..90%的数据进行训练，而标记则是固定使用后10%的数据
def Q2():
    def performance(cfd, wordlist):
        lt = dict((word, cfd[word].max()) for word in wordlist)
        baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
        return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))
    def display():
        import pylab
        word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
        words_by_freq = [w for (w, _) in word_freqs]
        cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
        sizes = 2 ** pylab.arange(15)
        perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
        pylab.plot(sizes, perfs, '-bo')
        pylab.title('Lookup Tagger Performance with Varying Model Size')
        pylab.xlabel('Model Size')
        pylab.ylabel('Performance')
        pylab.show()
    def unigramPerformance(brown_tagged_sents,size,test_sents):
        train_sents=brown_tagged_sents[:size]
        unigram_tagger=nltk.UnigramTagger(train_sents)
        return unigram_tagger.evaluate(test_sents)
    def unigramDisplay():
        import pylab
        brown_tagged_sents=brown.tagged_sents(categories='news')
        test_sents=brown_tagged_sents[int(-0.1*len(brown_tagged_sents)):]
        size=len(brown_tagged_sents)
        sizeList=[int((x*1./10)*size) for x in range(1,10)]
        perfs=[unigramPerformance(brown_tagged_sents,x,test_sents) for x in sizeList]
        pylab.plot(sizeList,perfs,'-bo')
        pylab.title('Unigram tagger Performance with Varying trainsents size')
        pylab.xlabel('trainSentsSize')
        pylab.ylabel('Performance')
        pylab.show()
    display()
    unigramDisplay()
if __name__ == '__main__':
    Q11()
    Q12()
    Q13()
    Q14()
    Q2()
# 