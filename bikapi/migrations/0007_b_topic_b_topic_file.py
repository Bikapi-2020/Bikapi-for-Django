# Generated by Django 3.0.1 on 2019-12-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikapi', '0006_auto_20191226_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='b_topic',
            name='b_topic_file',
            field=models.FileField(blank=True, upload_to='static/images/', verbose_name='附件'),
        ),
    ]
