from django.urls import path
from .views import user_login, log_out, sign_up

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", log_out, name="logout"),
    path("", sign_up, name="signup"),
]
