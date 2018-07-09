# Generated by Django 2.0.6 on 2018-07-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='姓名')),
                ('email', models.EmailField(max_length=100, verbose_name='邮箱')),
                ('message', models.TextField(verbose_name='消息')),
                ('active', models.BooleanField(verbose_name='是否有效')),
                ('posted_time', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
            ],
        ),
    ]
