# from NewsCMS.models import lastNews
class Doct(object):
    __stopwords=None
    __dictionary=None

    @staticmethod
    def __loadFile(fname):
        words = set()
        f = open(fname, 'r', encoding='utf-8')  # 读文件
        lines = f.readlines()
        f.close()  # 记得关闭文件哦

        for line in lines:
            line = line.strip()  # 去掉两端的空白字符，如空格、回车等
            words.add(line)
        print('have load %s!'%(fname))
        return words
    @staticmethod
    def __loadDictionaries(fname):
        return Doct.__loadFile(fname)
    @staticmethod
    def __loadStopwords():
        stopwords = Doct.__loadFile('stoplist_utf8.txt')
        puncs = Doct.__loadFile('punctuation_utf8.txt')
        # print(stopwords)
        # print(puncs)
        stopwords = stopwords | puncs
        # print(stopwords)
        return list(stopwords)
    def __new__(cls, *args, **kwargs):
        if Doct.__stopwords is None:
            Doct.__stopwords=Doct.__loadStopwords()
        if Doct.__dictionary is None:
            Doct.__dictionary=Doct.__loadDictionaries('dictionary.txt')
        return object.__new__(cls)
    def __init__(self,obj=None):
        if obj is not None:
            self.obj=obj
            self.id=obj.hashid
            self.content=obj.title+obj.content
        # print('init')
    @staticmethod
    def fmm_seg(sentence):
        max_len = 7  # 最长词的长度
        result = []  # 结果列表，用于保存分词之后的结果
        start = 0  # 正向最大匹配，从0开始

        while start < len(sentence):
            end = min(start + max_len, len(sentence))  # 处理边界，句子的长度有数
            while end > 0:
                candidate = sentence[start:end]  # 获得一个候选
                # print("Candidate：", candidate)
                if candidate in Doct.__dictionary or end == start + 1:  # 判断候选是否在词典中，或者长度是否为1，满足任意条件都匹配
                    # print("找到一个词：", sentence[start: end])
                    result.append(candidate)
                    start = end  # 更新下次开始匹配的位置
                    break  # 当前匹配成功，跳出循环！
                else:
                    end -= 1

        return result

    """ 逆向最大匹配算法(backward maximum match, bmm)
        参数1：待分词的字符串，要求类型为unicode
        参数2：词典
    """
    @staticmethod
    def bmm_seg(sentence):
        max_len = 7  # 最长词的长度
        result = []
        end = len(sentence)  # 从后向前扫描，因此end表示结束位置
        while end > 0:
            start = max(end - max_len, 0)  # 从后向前决定起始位置，注意下标不要小于0
            while start < end:
                candidate = sentence[start:end]
                # print("candidate：", candidate)
                if candidate in Doct.__dictionary or end == start + 1:
                    # print("找到一个词：", sentence[start: end])
                    result.append(candidate)
                    end = start
                    break
                else:
                    start += 1

        result.reverse()  # 结果是逆序的，所以调转一下。用list自带的函数reverse，非常简单的呦！
        return result
    def ContentSplit(self):
        self.doct=self.fmm_seg(self.content)

    def removeStopwords(self):

        new_list = []

        for word in self.doct:
            if word not in self.__stopwords:
                new_list.append(word)

        self.removedDoct=new_list
        # print(self.removedDoct)
        return self
    @staticmethod
    def removeQueryStopwords(query):
        new_list = []

        for word in query:
            if word not in Doct.__stopwords:
                new_list.append(word)

        return new_list
    def getRemovedDoct(self):
        self.ContentSplit()
        self.removeStopwords()
        return [self.id,self.removedDoct]
    def display(self):
        print(self.id)
        print(self.content)
        print(self.doct)
        print(self.removedDoct)
        return self

    def mark(self):
        self.obj.MarkSearchlizate()
        print('News %s has marked!'%(self.id))
if __name__=='__main__':
    d=Doct('123','我是谁啊，被中国北京')
    # d.ContentSplit()
    # d.removeStopwords()
    # d.display()
    res=d.getRemovedDoct()
    print(res)
    d.mark()
