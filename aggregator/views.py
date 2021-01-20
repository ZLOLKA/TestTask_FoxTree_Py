from django.shortcuts import render
from .models import BankRate


# Create your views here.
def home_view(request):
    rates = BankRate.objects.all()
    context = {
        "rates": rates,
    }
    return render(request, "Home.html", context)
