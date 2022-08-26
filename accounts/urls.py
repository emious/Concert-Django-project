from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('profile/', views.profile_view),
    path('profileRegister/', views.profile_register_view),
    path('Edit/', views.profile_edit_view),

]
