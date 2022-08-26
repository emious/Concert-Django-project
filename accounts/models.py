from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ProfileModel (models.Model):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربری', related_name='profile')

    #Name = models.CharField(max_length=100, verbose_name='نام')
    #Family = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    ProfileImage = models.ImageField(upload_to='ProfileImages/', verbose_name='عکس')

    Male = 1
    Female = 2
    GenderChoices = ((Male, 'مرد'), (Female, 'زن'))

    Gender = models.IntegerField(choices=GenderChoices, verbose_name='جنسیت')
    Credit = models.IntegerField(verbose_name='اعتبار', default=0)

