
from django.urls import path
from django.contrib.auth import views as auth_virs
from . import views
urlpatterns = [
        path("sdff/", views.ddd, name="www"),
        path("logins/", auth_virs.LoginView.as_view(template_name = "logins.html"), name="logg"),
        path("registers/", views.register_user, name="register"),
        path("outs/", auth_virs.LogoutView.as_view(template_name = "logoutt.html"), name="out"),
        path("sdf/", views.saclogs, name="sss"),
        path("profile/", views.profile, name="po"),
        path("adds/", views.add_pro, name="cx"),
        

]