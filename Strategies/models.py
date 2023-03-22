from django.db import models

# Create your models here.

class userStrategies(models.Model):
    id=models.CharField(max_length=32,unique=True,primary_key=True)
    userid=models.CharField(max_length=16)
    strategyName=models.CharField(max_length=32)
    strategyScript=models.CharField(max_length=4096)
    createTime=models.DateField(auto_now_add=True)
    lastEditTime=models.DateField(auto_now=True)
    status=models.CharField(max_length=16)

    def to_dict(self,haveScript=True):
        self_dict=dict()
        self_dict['id']=self.id
        self_dict['userid']=self.userid
        self_dict['strategyName']=self.strategyName
        if haveScript is True:
            self_dict['strategyScript']=self.strategyScript
        self_dict['createTime']=self.createTime.__str__()
        self_dict['lastEditTime']=self.lastEditTime.__str__()
        self_dict['status']=self.status
        return self_dict

