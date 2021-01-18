from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from .views import SignUpView, LoginView


urlpatterns = [
    url(r"^login/$", LoginView.as_view(), name="login"),
    url(r"^logout/$", LogoutView.as_view(), name="logout"),
    url(r"^registration/$", SignUpView.as_view(), name="registration"),
    url(r"^", include("social_django.urls", namespace="social")),
]
