# Generated by Django 4.1 on 2022-08-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemodel',
            name='Status',
            field=models.IntegerField(choices=[(1, 'فروش بلیط شروع شده است'), (2, 'فروش بلیط تمام شده است'), (3, 'این سانس لغو شده است'), (4, 'درحال فروش بلیط')], verbose_name='وضعیت'),
        ),
    ]
