from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from django import forms


# Create your views here.
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        required=False,
        label="First name",
    )
    last_name = forms.CharField(
        required=False,
        label="Last name",
    )
    email = forms.CharField(
        required=False,
        label="Email",
    )

    class Meta(UserCreationForm.Meta):
        fields = (*UserCreationForm.Meta.fields, "first_name", "last_name", "email")


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'


class LoginView(auth_views.LoginView):
    template_name = "login.html"
