from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

import accounts
import ticketSales.views
from Consert import settings
from ticketSales import views
from accounts.forms import ProfileRegisterForm, ProfileEditForm, UserEditForm
from accounts.models import ProfileModel


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                'username': username,
                'errorMessage': 'کاربر مورد نظر یافت نشد'
            }
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse(views.concert_list_view))


@login_required
def profile_view(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile.html', context)


def profile_register_view(request):
    if request.method == "POST":
        profile_register_form = ProfileRegisterForm(request.POST, request.FILES)
        if profile_register_form.is_valid():
            user = User.objects.create_user(username=profile_register_form.cleaned_data["username"],
                                            email=profile_register_form.cleaned_data['email'],
                                            password=profile_register_form.cleaned_data['password'],
                                            first_name=profile_register_form.cleaned_data['first_name'],
                                            last_name=profile_register_form.cleaned_data['last_name'])

            user.save()

            profileModel = ProfileModel(user=user,
                                        ProfileImage=profile_register_form.cleaned_data['ProfileImage'],
                                        Gender=profile_register_form.cleaned_data['Gender'],
                                        Credit=profile_register_form.cleaned_data['Credit'])

            profileModel.save()

            return HttpResponseRedirect(reverse(ticketSales.views.concert_list_view))
    else:
        profile_register_form = ProfileRegisterForm()

    context = {
        "formData": profile_register_form
    }

    return render(request, "accounts/profileRegister.html", context)


def profile_edit_view(request):
    if request.method == "POST":
        profileEditForm = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        userEditForm = UserEditForm(request.POST, instance=request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse(accounts.views.profile_view))
    else:
        profileEditForm = ProfileEditForm(instance=request.user.profile)
        userEditForm = UserEditForm(instance=request.user)

    context = {

        "profileEditForm": profileEditForm,
        "userEditForm": userEditForm,
        "ProfileImage": request.user.profile.ProfileImage,

    }

    return render(request, "accounts/profileEdit.html", context)
