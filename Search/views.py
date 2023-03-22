from django.shortcuts import render
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
import json
from Search.settings import search_engerine
search_engerine.init()
# Create your views here.

def Search_index(request):
    if request.method=='GET':
        wd=request.GET.get('wd',None)
        # print(type(wd))
        print('get',wd)
        # return render('search.html',search_wd=wd)
        # return render_template('search.html',search_wd=wd)
    elif request.method=='POST':
        wd = request.form.get('wd')
        read_to_search=request.form.get('read_to_search')
        print('post', wd,read_to_search)

    query_list,res=search_engerine.query(wd)
    # print(res)
    #
    #     if read_to_search!=None:
    #         return render('search.html', search_wd=wd)
    #
    #     query=[]
    #     query_1=wd.split(" ")
    #     temp=wd.replace(" ","")
    #     print(query,temp)
    #     results_bmm = bmm_seg(wd, dictionary)
    #     results_fmm = fmm_seg(wd, dictionary)
    #
    #     query.extend(query_1)
    #     query.extend(results_bmm)
    #     query.extend(results_fmm)
    #     query=list(set(query))
    #     if ' ' in query:
    #         query.remove(' ')
    #     if '' in query:
    #         query.remove('')
    #
    #     query_init=query.copy()
    #     stopwords=getStopwords()
    #     # print(stopwords)
    #     # print('before',len(query),query)
    #     query=remove_stopwords(query,stopwords)
    #     print('after',len(query), query)
    #     res=core.getSearchResult(query,query_init)
    #     print(res)
    #     if len(res)==0:
    #         res=core.getSearchResult(query_init,query_init)
    #         query=query_init
    #     resp={
    #         'wd_split':query,
    #         'data':res,
    #     }
    #
    #     return json.dumps(resp)

    return render(request,"search_result.html",{'search_wd':wd,'lastNewsList':res,'highlight_wds':",".join(query_list)})
