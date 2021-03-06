# Generated by Django 3.0.1 on 2019-12-20 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikapi', '0004_auto_20191220_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b_comment',
            name='b_comment_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='评论ID'),
        ),
        migrations.AlterField(
            model_name='b_comment',
            name='b_comment_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_Comment', verbose_name='父ID'),
        ),
        migrations.AlterField(
            model_name='b_comment',
            name='b_comment_topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_Topic', verbose_name='帖子ID'),
        ),
        migrations.AlterField(
            model_name='b_comment',
            name='b_comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_User', verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='b_manager',
            name='b_manage_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='管理员ID'),
        ),
        migrations.AlterField(
            model_name='b_section',
            name='b_section_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='板块ID'),
        ),
        migrations.AlterField(
            model_name='b_section',
            name='b_section_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_User', verbose_name='版主编号'),
        ),
        migrations.AlterField(
            model_name='b_section',
            name='b_section_zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bikapi.B_Zone', verbose_name='分区ID'),
        ),
        migrations.AlterField(
            model_name='b_tag',
            name='b_tag_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='标签ID'),
        ),
        migrations.AlterField(
            model_name='b_topic',
            name='b_topic_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='帖子ID'),
        ),
        migrations.AlterField(
            model_name='b_topic',
            name='b_topic_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_Section', verbose_name='板块ID'),
        ),
        migrations.AlterField(
            model_name='b_topic',
            name='b_topic_tag',
            field=models.ManyToManyField(through='bikapi.B_Topic2Tag', to='bikapi.B_Tag', verbose_name='外键-标签'),
        ),
        migrations.AlterField(
            model_name='b_topic',
            name='b_topic_tuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_User', verbose_name='帖子作者ID'),
        ),
        migrations.AlterField(
            model_name='b_up',
            name='b_up_topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_Topic', verbose_name='帖子ID'),
        ),
        migrations.AlterField(
            model_name='b_up',
            name='b_up_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_User', verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='b_user',
            name='b_user_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='b_zone',
            name='b_zone_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='分区ID'),
        ),
    ]
