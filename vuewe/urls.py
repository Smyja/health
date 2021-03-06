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
from django.conf import settings
from django.contrib.auth import views
from django.urls import path, include,re_path
from django.views.static import serve
from django.contrib.auth import views as auth_views
from aview.core.views import *
from aview.dashboard.views import acceptapp, bookin


def trigger_error(request):
    division_by_zero = 1 / 0


handler404 = 'aview.core.views.pagerror'
handler500 = 'aview.core.views.pagerror2'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('dashboard/', include('aview.dashboard.urls')),
    path('approve/', acceptapp, name = 'approve'),
    path('addpatient/', addpatient, name='addpatient'),
    path('sentry-debug/', trigger_error),
    path('patient/', patients, name='patients'),
    path('book/', bookin, name='bookin'),
    path('signup/', signup_view, name="signup"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name = 'logout'),
    path('about/', about, name = 'about'),
    path('terms/', terms, name = 'terms'),
    path('hospitaladmin/', hospital , name='hospital'),
    path('privacy/', privacy, name='privacy'),
    path('admin/', admin.site.urls),
    path('forgot_password/',
         auth_views.PasswordResetView.as_view(
             template_name="core/forgotpassword.html"),
    name="reset_password"),
        path('forget/',
     auth_views.PasswordResetView.as_view(template_name="core/forgotpassword.html"), 
    name="resetPassword"),
    path('forgot_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ="core/paswordsent.html"), 
    name="password_reset_done"),
    path('forgot/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('forgot_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
