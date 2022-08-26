# Generated by Django 4.1 on 2022-08-24 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConcertModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='نام کسنرت')),
                ('SingerName', models.CharField(max_length=100, verbose_name='خواننده')),
                ('lenght', models.IntegerField()),
                ('Poster', models.ImageField(null=True, upload_to='concertImages/', verbose_name='پوستر')),
            ],
            options={
                'verbose_name': 'کنسرت',
                'verbose_name_plural': 'کنسرت ها',
            },
        ),
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='نام محل')),
                ('Address', models.CharField(default='تهران - برج میلاد', max_length=500, verbose_name='آدرس')),
                ('Phone', models.CharField(max_length=11, null=True, verbose_name='تلفن')),
                ('Capacity', models.IntegerField(verbose_name='ظرفیت')),
            ],
            options={
                'verbose_name': 'محل برگزاری',
                'verbose_name_plural': 'محل برگزاری',
            },
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='نام')),
                ('Family', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('ProfileImage', models.ImageField(upload_to='ProfileImages/', verbose_name='عکس')),
                ('Gender', models.IntegerField(choices=[('Male', 'مرد'), ('Female', 'زن')], verbose_name='جنسیت')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='TimeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDateTime', models.DateTimeField()),
                ('Seat', models.IntegerField()),
                ('Status', models.IntegerField(choices=[('Start', 'فروش بلیط شروع شده است'), ('End', 'فروش بلیط تمام شده است'), ('Cancel', 'این سانس لغو شده است'), ('Sale', 'درحال فروش بلیط')], verbose_name='وضعیت')),
                ('ConcertModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.concertmodel', verbose_name='کنسرت')),
                ('LocationModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.locationmodel', verbose_name='محل برگزاری')),
            ],
            options={
                'verbose_name': 'سانس',
                'verbose_name_plural': 'سانس ها',
            },
        ),
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketImage', models.ImageField(upload_to='TicketImages/', verbose_name='عکس')),
                ('Name', models.CharField(max_length=100, verbose_name='عنوان')),
                ('Price', models.IntegerField(verbose_name='مبلغ')),
                ('ProfileModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.profilemodel', verbose_name='کاربر')),
                ('TimeModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.timemodel', verbose_name='سانس')),
            ],
            options={
                'verbose_name': 'بلیط',
                'verbose_name_plural': 'بلیط ها',
            },
        ),
    ]
