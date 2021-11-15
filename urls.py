from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views 

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name = "registration/login.html"), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "registration/logout.html"), name = "logout"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name = "registration/password_change.html"), name = "password_change"),
    path("register/", views.register, name = "register"),
    path("profile/", views.my_profile, name = "my_profile"),
    path("settings/", views.Settings, name = "settings"),

    # path("password_reset/", auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"), name = "password_reset"),
    # path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_done.html"), name = "password_reset_done"),
    # path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_confirm.html"), name = "password_reset_confirm"),
    # path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_complete.html"), name = "password_reset_complete"),
    path("profile/edit/", views.edit_profile, name = "edit_profile"),
    path("users/", views.search_users, name = "search_users"),
    path("<slug>/", views.user_profile_view, name = "profile_view"),
]
