from django.db import models

# Create your models here.
class stockReport(models.Model):
    code=models.CharField(max_length=8)
    name=models.CharField(max_length=64)
    eps=models.CharField(max_length=32)
    eps_yoy=models.CharField(max_length=32)
    bvps=models.CharField(max_length=32)
    roe=models.CharField(max_length=32)
    epcf=models.CharField(max_length=32)
    net_profits=models.CharField(max_length=32)
    profits_yoy=models.CharField(max_length=32)
    distrib=models.CharField(max_length=64)
    report_date=models.CharField(max_length=16)
    season=models.CharField(max_length=16)

    def to_dict(self):
        self_dict=dict()
        self_dict['code']=self.code
        self_dict['name']=self.name
        self_dict['eps']=self.eps
        self_dict['eps_yoy']=self.eps_yoy
        self_dict['bvps']=self.bvps
        self_dict['roe']=self.roe
        self_dict['epcf']=self.epcf
        self_dict['net_profits']=self.net_profits
        self_dict['profits_yoy']=self.profits_yoy
        self_dict['distrib']=self.distrib
        self_dict['report_date']=self.report_date
        self_dict['season']=self.season
        return self_dict

class stockHistData(models.Model):
    code=models.CharField(max_length=8)
    date=models.DateField()
    open=models.CharField(max_length=16)
    high=models.CharField(max_length=16)
    close=models.CharField(max_length=16)

    low=models.CharField(max_length=16)
    volume=models.CharField(max_length=16)
    price_change=models.CharField(max_length=16)
    p_change=models.CharField(max_length=16)
    ma5=models.CharField(max_length=16)

    ma10=models.CharField(max_length=16)
    ma20=models.CharField(max_length=16)
    v_ma5=models.CharField(max_length=16)
    v_ma10=models.CharField(max_length=16)
    v_ma20=models.CharField(max_length=16)

    turnover=models.CharField(max_length=16,default='NULL')

    def to_dict(self):
        self_dict=dict()

        self_dict['code']=self.code
        self_dict['date']=self.date
        self_dict['open']=self.open
        self_dict['high']=self.high
        self_dict['close']=self.close

        self_dict['low']=self.low
        self_dict['volume']=self.volume
        self_dict['price_change']=self.price_change
        self_dict['p_change']=self.p_change
        self_dict['ma5']=self.ma5

        self_dict['ma10']=self.ma10
        self_dict['ma20']=self.ma20
        self_dict['v_ma5']=self.v_ma5
        self_dict['v_ma10']=self.v_ma10
        self_dict['v_ma20']=self.v_ma20

        self_dict['turnover']=self.turnover