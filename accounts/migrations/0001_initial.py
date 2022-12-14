# Generated by Django 4.1 on 2022-08-25 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='نام')),
                ('Family', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('ProfileImage', models.ImageField(upload_to='ProfileImages/', verbose_name='عکس')),
                ('Gender', models.IntegerField(choices=[('Male', 'مرد'), ('Female', 'زن')], verbose_name='جنسیت')),
                ('Credit', models.IntegerField(default=0, verbose_name='اعتبار')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربری')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]
