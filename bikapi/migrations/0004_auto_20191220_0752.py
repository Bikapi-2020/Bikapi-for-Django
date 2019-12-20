# Generated by Django 3.0.1 on 2019-12-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikapi', '0003_auto_20191220_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b_comment',
            name='b_comment_content',
            field=models.CharField(max_length=255, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='b_comment',
            name='b_comment_create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='b_integral',
            name='b_integral_num',
            field=models.IntegerField(default=-20, verbose_name='积分值'),
        ),
        migrations.AlterField(
            model_name='b_section',
            name='b_section_count',
            field=models.IntegerField(verbose_name='板块主题数'),
        ),
        migrations.AlterField(
            model_name='b_section',
            name='b_section_explanation',
            field=models.CharField(max_length=255, verbose_name='板块说明'),
        ),
        migrations.AlterField(
            model_name='b_section',
            name='b_section_name',
            field=models.CharField(max_length=64, verbose_name='板块'),
        ),
        migrations.AlterField(
            model_name='b_section',
            name='b_section_num',
            field=models.IntegerField(verbose_name='板块点击次数'),
        ),
        migrations.AlterField(
            model_name='b_up',
            name='b_is_up',
            field=models.BooleanField(verbose_name='是否点赞'),
        ),
        migrations.AlterField(
            model_name='b_zone',
            name='b_zone_name',
            field=models.CharField(max_length=32, verbose_name='分区'),
        ),
    ]
