import core
from mm_seg import fmm_seg,bmm_seg,dictionary
from corpus_reader import document_texts,remove_stopwords,getStopwords



def search(wd):


	query=[]
	query_1=wd.split(" ")
	temp=wd.replace(" ","")
	# print(query,temp)
	results_bmm = bmm_seg(wd, dictionary)
	results_fmm = fmm_seg(wd, dictionary)

	query.extend(query_1)
	query.extend(results_bmm)
	query.extend(results_fmm)
	query=list(set(query))
	if ' ' in query:
		query.remove(' ')
	if '' in query:
		query.remove('')

	query_init=query.copy()
	stopwords=getStopwords()
	# print(stopwords)
	# print('before',len(query),query)
	query=remove_stopwords(query,stopwords)
	# print('after',len(query), query)
	res=core.getSearchResult(query)
	# print(res)
	if len(res)==0:
		res=core.getSearchResult(query_init,query_init)
		query=query_init

	return res

if __name__ == '__main__':
	while True:
		query=input("请输入要查询的单词：")
		res=search(query)
		k=len(res)
		print("共%d条检索结果："%(k))
		for count in range(k):
			print("检索结果%d,评分%s>>:%s"%(count,res[count][0],res[count][1]))
		print("\n****************************************\n")