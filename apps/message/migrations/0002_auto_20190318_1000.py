# Generated by Django 2.1.7 on 2019-03-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户留言信息', 'verbose_name_plural': '用户留言信息'},
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='用户名'),
        ),
    ]