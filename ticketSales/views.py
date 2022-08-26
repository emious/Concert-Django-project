from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import ticketSales
from .models import ConcertModel, LocationModel, TimeModel
from ticketSales.forms import SearchForm, ConcertForm
from django.db.models import Q


# Create your views here.

def concert_list_view(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        concerts = ConcertModel.objects.filter(Q(SingerName__contains=search_text) | Q(Name__contains=search_text))
    else:
        concerts = ConcertModel.objects.all()

    context = {
        'concertlist': concerts,
        'concertcount': concerts.count(),
        'search_form': search_form
    }
    return render(request, 'ticketSales/concertlist.html', context)


@login_required
def location_list_view(request):
    locations = LocationModel.objects.all()
    context = {
        'locationlist': locations,
    }
    return render(request, 'ticketSales/locationList.html', context)


def concert_detail_view(request, id):
    detail = ConcertModel.objects.get(pk=id)
    context = {
        'detail': detail,
    }
    return render(request, 'ticketSales/concertDetails.html', context)


@login_required
def time_view(request):
    # if request.user.is_authenticated and request.user.is_active:
    times = TimeModel.objects.all()
    context = {
        'timelist': times,
    }
    return render(request, 'ticketSales/timelist.html', context)


# else:
#     return HttpResponseRedirect(reverse(accounts.views.login_view))

def concert_edit_view(request, id):
    detail = ConcertModel.objects.get(pk=id)

    if request.method == "POST":
        concert_form = ConcertForm(request.POST, request.FILES, instance=detail)

        if concert_form.is_valid:
            concert_form.save()
            return HttpResponseRedirect(reverse(ticketSales.views.concert_list_view))
        else:
            concert_form = ConcertForm(instance=detail)
    else:
        concert_form = ConcertForm(instance=detail)

    context = {
        'concert_form': concert_form,
        'Poster': detail.Poster
    }
    return render(request, 'ticketSales/concertEdit.html', context)
