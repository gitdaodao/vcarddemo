from django.db import models
import reprlib

# Create your models here.

class Message(models.Model):
    name=models.CharField('姓名',max_length=55)
    email=models.EmailField('邮箱',max_length=100)
    message=models.TextField('消息')
    active=models.BooleanField('是否有效',default=True)
    posted_time=models.DateTimeField('提交时间',auto_now_add=True)


    def __str__(self):
        # reprlib.repr(xx) 截取首尾 留空中间为......
        return f'{self.name},{reprlib.repr(self.message)}'