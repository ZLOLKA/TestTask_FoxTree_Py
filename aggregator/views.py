from django.shortcuts import render
from django import forms
from django.core.exceptions import ValidationError
from datetime import date

from .models import BankRate
from .tasks import get_exchange_rates


class DateForm(forms.Form):
    from_date = forms.DateField(
        required=False,
        label="from_date",
    )
    to_date = forms.DateField(
        required=False,
        label="to_date",
    )

    def clean_from_date(self):
        data = self.cleaned_data["from_date"]

        if data is None:
            data = date(1, 1, 1)  # Create min Date

        return data

    def clean_to_date(self):
        data = self.cleaned_data["to_date"]

        if data is None:
            today = date.today()
            if self.cleaned_data["from_date"] == today:
                data = date(today.year, today.month, today.day+1)  # Create date for correct work date__range filter
            else:
                data = today
        if data < self.cleaned_data["from_date"]:
            raise ValidationError("Date to earlier than date from")

        return data


# Create your views here.
def home_view(request):
    rates = []
    all = True
    if request.method == "POST":
        form = DateForm(request.POST)

        if form.is_valid():
            from_date = form.cleaned_data["from_date"]
            to_date = form.cleaned_data["to_date"]

            rates = BankRate.objects.filter(date__range=(from_date, to_date))
    else:
        if request.user.is_authenticated:
            if request.GET.get("now", False):
                rates = [get_exchange_rates(periodic=False)]
                all = False
            else:
                rates = BankRate.objects.all()
        else:
            rates = [get_exchange_rates(periodic=False)]
    context = {
        "rates": rates,
        "all": all,
    }
    return render(request, "Home.html", context)
