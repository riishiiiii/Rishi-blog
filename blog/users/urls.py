from django.urls import path
from users import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("signup", views.register, name="users-signup"),
    path("profile", views.profile, name="users-profile"),
    path("", views.login_attempt, name="user-login"),
    path("verify", views.login_otp, name="user-login-otp"),
    path(
        "logout",
        auth_view.LogoutView.as_view(template_name="users/logout.html"),
        name="user-logout",
    ),
    path("resendotp", views.resend_otp, name="resend-otp"),
]
