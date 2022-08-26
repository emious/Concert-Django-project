from django.contrib import admin
from ticketSales.models import ConcertModel, LocationModel, TimeModel, TicketModel
# Register your models here.

admin.site.register(ConcertModel)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
admin.site.register(TicketModel)
