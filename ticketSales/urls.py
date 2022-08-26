from django.urls import path
from ticketSales import views

urlpatterns = [
    path('concert/list', views.concert_list_view),
    path('location/list', views.location_list_view),
    path('consert/<int:id>', views.concert_detail_view),
    path('time/list', views.time_view),
    path('consertEdit/<int:id>', views.concert_edit_view),

]
