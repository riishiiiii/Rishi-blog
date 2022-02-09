from django.urls import path
from users import views
from django.contrib.auth import views as auth_view
urlpatterns = [
  
    path('signup', views.register , name= 'users-signup'),
    path('profile', views.profile , name= 'users-profile'),
    path('',views.login_attempt, name= 'user-login'),
    path('verify', views.login_otp,name='user-login-otp'),
    path('logout',auth_view.LogoutView.as_view(template_name='users/logout.html'),name= 'user-logout'),
    path("resendotp",views.resend_otp,name="resend-otp")
#     path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),
#          name='password_reset'),
#     path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
#          name='password_reset_done'),
#     path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
#          name='password_reset_confirm'),
#     path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
#          name='password_reset_complete')

]