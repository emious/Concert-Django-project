# Generated by Django 4.1 on 2022-08-25 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ticketSales', '0002_alter_timemodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='ProfileModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profilemodel', verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='Seat',
            field=models.IntegerField(verbose_name='تعداد صندلی'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='StartDateTime',
            field=models.DateTimeField(verbose_name='تاریخ برگزاری'),
        ),
        migrations.DeleteModel(
            name='ProfileModel',
        ),
    ]
