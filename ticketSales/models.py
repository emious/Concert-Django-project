from django.db import models
from jalali_date import date2jalali,datetime2jalali

# Create your models here.
from accounts.models import ProfileModel


class ConcertModel(models.Model):

    class Meta:
        verbose_name = 'کنسرت'
        verbose_name_plural = "کنسرت ها"

    Name = models.CharField(max_length=100, verbose_name='نام کسنرت')
    SingerName = models.CharField(max_length=100, verbose_name='خواننده')
    lenght = models.IntegerField()
    Poster = models.ImageField(upload_to='concertImages/', null=True, verbose_name='پوستر')

    def __str__(self):
        return self.SingerName


class LocationModel(models.Model):
    class Meta:
        verbose_name = "محل برگزاری"
        verbose_name_plural = "محل برگزاری"

    Name = models.CharField(max_length=100, verbose_name='نام محل')
    Address = models.CharField(max_length=500, default= "تهران - برج میلاد", verbose_name='آدرس')
    Phone = models.CharField(max_length=11, null=True, verbose_name='تلفن')
    Capacity = models.IntegerField(verbose_name='ظرفیت')

    def __str__(self):
        return self.Name


class TimeModel(models.Model):

    class Meta:
        verbose_name = "سانس"
        verbose_name_plural = "سانس ها"


    ConcertModel = models.ForeignKey('ConcertModel', on_delete=models.PROTECT, verbose_name='کنسرت')
    LocationModel = models.ForeignKey('LocationModel', on_delete=models.PROTECT, verbose_name='محل برگزاری')
    StartDateTime = models.DateTimeField(verbose_name='تاریخ برگزاری')
    Seat = models.IntegerField(verbose_name='تعداد صندلی')

    Start = 1
    End = 2
    Cancel = 3
    Sale = 4
    StatusChoices = ((Start, 'فروش بلیط شروع شده است'),
                      (End, 'فروش بلیط تمام شده است'),
                      (Cancel, 'این سانس لغو شده است'),
                      (Sale, 'درحال فروش بلیط'))

    Status = models.IntegerField(choices=StatusChoices, verbose_name='وضعیت')

    def __str__(self):
        return "time: {} ConcertName: {} Location: {} ".format(self.StartDateTime,
                                                               self.ConcertModel.Name,
                                                               self.LocationModel.Name)

    def get_jalali_date(self):
        return datetime2jalali(self.StartDateTime)


class TicketModel (models.Model):

    class Meta:
        verbose_name = 'بلیط'
        verbose_name_plural = 'بلیط ها'

    ProfileModel = models.ForeignKey(ProfileModel, on_delete=models.PROTECT, verbose_name='کاربر')
    TimeModel = models.ForeignKey('TimeModel', on_delete=models.PROTECT, verbose_name='سانس')
    TicketImage = models.ImageField(upload_to='TicketImages/', verbose_name='عکس')
    Name = models.CharField(max_length=100, verbose_name='عنوان')
    Price = models.IntegerField(verbose_name='مبلغ')

    def __str__(self):
        return "TicketInfo: Profile :{} ConcertInfo : {} {} {} ".format(ProfileModel.__str__(), TimeModel.__str__())