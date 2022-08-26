from django import forms
from ticketSales.models import ConcertModel


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=100, label='نام کنسرت', required=False)


class ConcertForm(forms.ModelForm):
    class Meta:
        model = ConcertModel
        fields = ['Name', 'SingerName', 'lenght', 'Poster']

        #exclude be dard ine mikhore ke hame filed haro baraye edit niaz
        # darim vali list exclude ro niaz ndrim baraxe fields
        #exclude = ["poster"]
