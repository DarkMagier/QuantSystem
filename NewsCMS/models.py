from django.db import models
import json
# Create your models here.
class lastNews(models.Model):
    hashid=models.CharField(max_length=64,unique=True)
    classify=models.CharField(max_length=32)
    title=models.CharField(max_length=255,unique=True)
    time=models.DateTimeField()
    url=models.URLField(max_length=256)
    content=models.TextField(max_length=4096)
    searchlization=models.CharField(max_length=2,default='N')

    def __str__(self):
        return self.title
    def __contentHighlight(self,content,highlightList):
        highlightList.sort(key=lambda x: len(x))
        highlightList.reverse()
        print(highlightList)
        for wd in highlightList:
            content = content.replace(wd, """<span style="color: red">%s</span>""" % (wd))
        return content
    def to_dict(self,content_max_length=None,highlightList=None):
        self_dict=dict()
        self_dict['id']=self.id
        self_dict['hashid']=self.hashid
        self_dict['classify']=self.classify
        self_dict['title']=self.title
        self_dict['time']=self.time.__str__()
        self_dict['url']=self.url
        self_dict['content']=self.content


        if content_max_length!=None:
            self_dict['content'] = self.content[0:content_max_length]
            # if highlightList != None:
            #     self_dict['title']=self.__contentHighlight(self.title,highlightList)
            #     self_dict['content'] = self.__contentHighlight(self.content,highlightList)[0:content_max_length]
            # else:
            #     self_dict['content'] = self.content[0:content_max_length]
        return self_dict

    def to_json(self):
        return json.dumps(self.to_dict())

    def MarkSearchlizate(self):
        self.searchlization='Y'
        print(self.id," have marked!")
        self.save()