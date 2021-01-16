from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import SignUpView


class LoginView(auth_views.LoginView):
    template_name = "login.html"


urlpatterns = [
    url(r"^login/$", LoginView.as_view(), name="login"),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^registration/$", SignUpView.as_view(), name="registration")
]
