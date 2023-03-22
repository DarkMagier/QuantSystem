from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#
class User(AbstractUser):
# class User(models.Model):

    uid=models.CharField(max_length=16)
    # username=models.CharField(max_length=16,unique=True)
    # password=models.CharField(max_length=32,)
    nickname = models.CharField(max_length=32, unique=True)
    phone=models.CharField(max_length=16)
    # email=models.EmailField()

    def to_dict(self):
        user_dict=dict()
        print(user_dict)
        user_dict['uid']=self.uid
        user_dict['username']=self.username
        user_dict['nickname']=self.nickname
        user_dict['phone']=self.phone
        user_dict['email']=self.email

        return user_dict
