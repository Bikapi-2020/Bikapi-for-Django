# Generated by Django 3.0 on 2019-12-17 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikapi', '0028_auto_20191217_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b_comment',
            name='b_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_User'),
        ),
        migrations.AlterField(
            model_name='b_section',
            name='b_section_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_User'),
        ),
        migrations.AlterField(
            model_name='b_topic',
            name='b_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_User'),
        ),
        migrations.AlterField(
            model_name='b_up',
            name='b_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bikapi.B_User'),
        ),
    ]
