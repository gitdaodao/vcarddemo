from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    Mobile=models.CharField(max_length=20,blank=True)
    photo=models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return f'用户{self.user.username}的个人资料~'