# from Search.inverted_index.Doct import Doct
try:
    from Search.inverted_index.Doct import Doct
    import time
except:
    import tushare as ts
    import os, django
    import time
    import hashlib
    from Doct import Doct
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuantSystem.settings")
    django.setup()
from NewsCMS.models import lastNews
import pickle
class Inverted_Index(object):
    __instance=None
    def __new__(cls, *args, **kwargs):
        if Inverted_Index.__instance is None:
            Inverted_Index.__instance=object.__new__(cls,*args,**kwargs)
            # Inverted_Index.__instance.__setattr__('name','test')

            Inverted_Index.all_words = []  # 词的顺序列表
            Inverted_Index.word2id = {}  # 词到ID的映射
            Inverted_Index.word2docs = {}  # 记录包含词的文档集合
            Inverted_Index.inverted_index = []  # 记录包含词的文档集合
            print('create a new invert_index object')
        return Inverted_Index.__instance
    def __init__(self,*args,**kwargs):
        pass
    def init(self):
        self.load()
        Doct()
        self.newDetect()
        from NewsCMS import models
        # doct1=Doct('123','永泰能源780亿债务爆雷幕后：视一切规则如儿戏')
        # doct2=Doct('124','昔日"超募王"奥康衰落 募投项目2012年至今尚未…')
        # docts = models.lastNews.objects.filter(searchlization='N').all()
        # for doct in docts:
        #     d = Doct(doct)
        #     self.updateSingeDoct( d)

    def updateSingeDoct(self,doct):
        timeshift=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print("[%s]信息检索系统>>:正在收录--%s"%(timeshift,doct.obj.title))
        doct.getRemovedDoct()
        print("!!!")
        self.buildSingleDoctDictionary(doct)
        self.buildSingleinvertedIndex(doct)
        print("[%s]信息检索系统>>:收录成功！--%s" % (timeshift, doct.obj.title))
        doct.mark()


    def buildSingleDoctDictionary(self,doct):
        '''
        建立词典，并返回相关数据对象
        '''

        for w in doct.removedDoct:
            if w not in self.word2id:  # 如果遇到一个新的、未见过的词
                self.all_words.append(w)  # 加入词列表
                self.word2id[w] = len(self.word2id)  # 分配编号

            if w not in self.word2docs:  # 如果遇到一个新词，为其建立包含它的文档集合
                self.word2docs[w] = set()

            self.word2docs[w].add(doct.id)


    def buildSingleinvertedIndex(self, doct):
        '''
        建立倒排索引的倒排表。需要与词典等信息配合使用。
        '''
        # inverted_index = [[] for i in range(len(word2id))]
        c1=len(self.inverted_index)
        c2=len(self.word2id)
        temp=[[] for i in range(c2-c1)]
        self.inverted_index.extend(temp)


        for w in set(doct.removedDoct):  # 每个词处理一次，用Set
            tf = doct.removedDoct.count(w)
            wid = self.word2id[w]
            # print('wid:',wid)
            self.inverted_index[wid].append((doct.id, tf))


    def update(self,docts):
        for doct in docts:
            self.updateSingeDoct(Doct(doct))
        self.save()

    def fetch_doclist_by_word(self,wordid):
        '''
        从倒排索引中取出包含词word的文档列表
        '''
        return self.inverted_index[wordid]

    def scores(self,query):

        q1=Doct.fmm_seg(query)
        q2=Doct.bmm_seg(query)

        q=[query]
        q.extend(q1)
        q.extend(q2)
        q=Doct.removeQueryStopwords(q)
        query_list=list(set(q))
        query_list.sort(key=lambda x: len(x))
        query_list.reverse()
        print('query words:',query_list)

        doc2score = {}  # 记录文档分数

        for w in query_list:  #
            # print('querying words:', w)
            if w not in self.word2id:
                continue
            wordid = self.word2id[w]
            doc_tf_list = self.fetch_doclist_by_word(wordid)
            for (doc, tf) in doc_tf_list:
                if doc not in doc2score:
                    doc2score[doc] = tf
                else:
                    doc2score[doc] += tf

        doc_score_list = doc2score.items()
        sorted_docs_by_score = sorted(doc_score_list, key=lambda item: item[1], reverse=True)
        return query_list,sorted_docs_by_score


    def query(self,query):

        '''
        query: 关键词列表
        df: 词项文档统计
        scorer从倒排索引inverted_index中获取文档并对文档进行相关性评分
        返回排在最前面的文档
        排序函数的计算方法是：文档和查询向量中词的权重为词的频率，采用内积计算相似度
        '''


        # 排序

        query_list,sorted_docs_by_score=self.scores(query)

        docts_list=[]
        # for item in sorted_docs_by_score:
        #     docts_list.append(item[0])
        # res=lastNews.objects.filter(hashid__in=docts_list)

        for item in sorted_docs_by_score:
            docts_list.append(lastNews.objects.filter(hashid=item[0]).first())
        res=docts_list


        result_list=[]
        for item in res:
            result_list.append(item.to_dict(content_max_length=200,highlightList=query_list))



        return query_list,result_list


    def save(self):
        data=[self.all_words,self.word2id,self.word2docs,self.inverted_index]
        with open('inverted_save.pik','wb')as f:
            pickle.dump(data,f)
        print("[%s]信息检索系统>>:倒排索引已经保存！"%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
    def load(self):
        try:
            with open('inverted_save.pik', 'rb')as f:
                data=pickle.load(f)
        # print(data)
        # print(type(data[0]),len(data[0]),type(self.__instance.all_words),len(self.__instance.all_words))
            self.__instance.all_words.extend(data[0])
            self.__instance.word2id.update(data[1])
            self.__instance.word2docs.update(data[2])
            self.__instance.inverted_index.extend(data[3])
        except Exception as e:
            print(e)


    def newDetect(self):
        from QuantSystem.settings import SearchSystemDetectTime
        if SearchSystemDetectTime is None:
            return
        def detectNews():
            print("[%s]信息检索系统>>:系统开始运行!"%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
            while True:
                try:
                    print("[%s]信息检索系统>>:开始探测！" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                    newDocts=lastNews.objects.filter(searchlization='N').all()
                    l=len(newDocts)
                    if l!=0:
                        print("[%s]信息检索系统>>:发现%s条新闻未收录，开始收录" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),l))
                        self.update(newDocts)
                        print("[%s]信息检索系统>>:收录成功，共收录%s条!" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),l))
                    else:
                        print("[%s]信息检索系统>>:新闻都已经收录了!" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                    time.sleep(SearchSystemDetectTime)
                except Exception as e:
                    print(e)
                    time.sleep(SearchSystemDetectTime)

        import threading
        t=threading.Thread(target=detectNews)
        t.start()
        # from multiprocessing import Process
        # t=Process(target=detectNews)
        # t.run()


    def display(self):
        print(self.__all_words)
        print(self.__word2docs)
        print(self.__word2id)
        print(self.__in)


if __name__=='__main__':

    # print('test')
    v=Inverted_Index()

    from NewsCMS import models
    # doct1=Doct('123','永泰能源780亿债务爆雷幕后：视一切规则如儿戏')
    # doct2=Doct('124','昔日"超募王"奥康衰落 募投项目2012年至今尚未…')
    docts=models.lastNews.objects.filter(searchlization='N').all()
    for doct in docts:
        v.updateSingeDoct(Doct(doct))
    # v.updateSingeDoct(doct1)
    # v.updateSingeDoct(doct2)
    #
    v.save()
    # print(v.word2id)
    # res=v.query(['俄罗斯'])
    # print(res)
    # for item in res:
    #     t=models.lastNews.objects.filter(hashid=item[0]).first()
    #     print(t.title)