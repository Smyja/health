"""vuewe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from aview.core.views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', include('aview.dashboard.urls')),
    path('signup/', signup_view, name="signup"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('forgot_password/',
     auth_views.PasswordResetView.as_view(template_name="core/forgotpassword.html"), 
    name="reset_password"),
    path('forgot_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ="core/paswordsent.html"), 
    name="password_reset_done"),
    path('forgot/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('forgot_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
